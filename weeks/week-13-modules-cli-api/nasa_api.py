"""Trung tam Kham pha Vu tru (NASA & ISS Space Explorer) - Ultimate Edition.
Tich hop toan dien:
- ISS Real-time Tracker (Tram vu tru quoc te)
- NASA APOD (Anh thien van hang ngay + Tu dong tai anh HD ve may)
- NASA Mars Rover Photos (Anh xe tu hanh Curiosity tren Sao Hoa)
- NASA Asteroids NeoWs (Theo doi thien thach ap sat Trai Dat)
- Local Cache JSON (Tiet kiem luot goi API, tranh bi rate-limit)
- CLI Arguments (argparse) + Menu tuong tac hai chieu (Interactive Console)
- Kien truc OOP san sang lam ban dap cho Tuan 14 & 15.
Hoat dong 100% bang thu vien chuan Python (urllib, json, pathlib, datetime, argparse).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# Dam bao in tieng Viet UTF-8 dep tren terminal Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_DIR = Path(__file__).resolve().parent / ".learner-output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CACHE_FILE = OUTPUT_DIR / "nasa_cache.json"


class NasaClient:
    """Client giao tiep voi Open APIs cua NASA va Tram vu tru ISS co ho tro Cache."""

    def __init__(self, api_key: str = "DEMO_KEY", timeout: int = 15) -> None:
        self.api_key = api_key
        self.timeout = timeout
        self.headers = {"User-Agent": "Python-Space-Explorer/2.0"}
        self._cache = self._load_cache()

    def _load_cache(self) -> dict:
        if CACHE_FILE.exists():
            try:
                return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
            except Exception:
                return {}
        return {}

    def _save_cache(self) -> None:
        try:
            CACHE_FILE.write_text(json.dumps(self._cache, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            print(f"[!] Canh bao: Khong the luu cache: {e}")

    def _fetch_json(self, url: str, cache_key: str | None = None) -> dict | None:
        """Goi HTTP GET lay du lieu JSON, tu dong su dung cache neu co."""
        if cache_key and cache_key in self._cache:
            return self._cache[cache_key]

        req = Request(url, headers=self.headers)
        try:
            with urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if cache_key:
                    self._cache[cache_key] = data
                    self._save_cache()
                return data
        except HTTPError as e:
            print(f"[!] Loi HTTP tu Server: {e.code} - {e.reason}")
        except URLError as e:
            print(f"[!] Loi mang hoac timeout: {e.reason}")
        except json.JSONDecodeError:
            print("[!] Loi: Du lieu nhan ve khong phai JSON hop le.")
        except Exception as e:
            print(f"[!] Loi khong xac dinh: {e}")
        return None

    def get_iss_position(self) -> dict | None:
        """Lay vi tri thoi gian thuc cua Tram vu tru quoc te ISS."""
        url = "http://api.open-notify.org/iss-now.json"
        return self._fetch_json(url, cache_key=None)

    def get_apod(self, date_str: str | None = None) -> dict | None:
        """Lay anh thien van hoc cua ngay (NASA APOD)."""
        date_param = f"&date={date_str}" if date_str else ""
        cache_key = f"apod_{date_str or 'today'}"
        url = f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}{date_param}"
        return self._fetch_json(url, cache_key=cache_key)

    def get_mars_photos(self, sol: int = 1000) -> list[dict]:
        """Lay anh chup tu xe tu hanh Curiosity tren Sao Hoa (sol: ngay sao hoa)."""
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={self.api_key}"
        cache_key = f"mars_curiosity_sol_{sol}"
        res = self._fetch_json(url, cache_key=cache_key)
        if res and "photos" in res:
            return res["photos"]
        return []

    def get_near_earth_asteroids(self) -> list[dict]:
        """Lay danh sach thien thach dang ap sat Trai Dat trong ngay hom nay."""
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={today}&api_key={self.api_key}"
        cache_key = f"neo_{today}"
        res = self._fetch_json(url, cache_key=cache_key)
        if not res or "near_earth_objects" not in res:
            return []

        asteroids = []
        objects_by_date = res["near_earth_objects"]
        for _, items in objects_by_date.items():
            for item in items:
                diameter = item.get("estimated_diameter", {}).get("meters", {})
                close_data = item.get("close_approach_data", [{}])[0]
                velocity = close_data.get("relative_velocity", {}).get("kilometers_per_hour", "N/A")
                miss_km = close_data.get("miss_distance", {}).get("kilometers", "N/A")

                asteroids.append({
                    "name": item.get("name"),
                    "danger": item.get("is_potentially_hazardous_asteroid", False),
                    "min_diameter_m": round(diameter.get("estimated_diameter_min", 0), 1),
                    "max_diameter_m": round(diameter.get("estimated_diameter_max", 0), 1),
                    "speed_kmh": round(float(velocity), 1) if velocity != "N/A" else "N/A",
                    "miss_distance_km": f"{float(miss_km):,.0f}" if miss_km != "N/A" else "N/A",
                    "nasa_url": item.get("nasa_jpl_url"),
                })
        return asteroids

    def download_image(self, img_url: str, destination_name: str) -> Path | None:
        """Tai file anh tu URL va luu xuong thu muc .learner-output."""
        target_path = OUTPUT_DIR / destination_name
        req = Request(img_url, headers=self.headers)
        try:
            print(f"[*] Dang tai anh ve: {destination_name}...")
            with urlopen(req, timeout=30) as resp:
                content = resp.read()
                target_path.write_bytes(content)
                print(f"[+] Da tai xong! Dung luong: {len(content) // 1024} KB")
                print(f"    Vi tri file: {target_path}")
                return target_path
        except Exception as e:
            print(f"[!] Khong the tai anh: {e}")
            return None


# ==============================================================================
# CAC HAM HIEN THI DU LIEU (DISPLAY / CLI VIEW)
# ==============================================================================

def display_iss(client: NasaClient) -> None:
    print("\n" + "=" * 68)
    print("🛰️  THEO DOI TRAM VU TRU QUOC TE ISS (REAL-TIME)")
    print("=" * 68)
    data = client.get_iss_position()
    if not data or data.get("message") != "success":
        print("[!] Khong the lay du lieu vi tri ISS luc nay.")
        return

    pos = data["iss_position"]
    lat, lon = float(pos["latitude"]), float(pos["longitude"])
    ts = datetime.fromtimestamp(data["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")

    print("[+] Ket noi thanh cong!")
    print(f"- Thoi gian do      : {ts}")
    print(f"- Toa do hien tai   : Vi do {lat}°, Kinh do {lon}°")
    print(f"- Van toc quy dao   : ~27,600 km/h (bay 1 vong Trai Dat mat 90 phut)")
    print(f"- Xem truc tiep vi tri tren Google Maps:\n  👉 https://www.google.com/maps?q={lat},{lon}")
    print("=" * 68)


def display_apod(client: NasaClient, date_str: str | None = None, auto_download: bool = False) -> None:
    print("\n" + "=" * 68)
    print("🌌 ANH THIEN VAN HOC CUA NGAY (NASA APOD)")
    print("=" * 68)
    data = client.get_apod(date_str)
    if not data:
        return

    title = data.get("title", "Khong co tieu de")
    date_val = data.get("date", "N/A")
    copyright_val = data.get("copyright", "NASA Public Domain").replace("\n", " ").strip()
    media_type = data.get("media_type", "image")
    img_url = data.get("hdurl") or data.get("url")

    print(f"- Tieu de anh    : {title}")
    print(f"- Ngay cong bo   : {date_val}")
    print(f"- Tac gia / Quyen: {copyright_val}")
    print(f"- Dinh dang      : {media_type.upper()}")
    print(f"- Link xem anh   : {img_url}")

    explanation = data.get("explanation", "")
    if explanation:
        print(f"\n📖 Giai thich khoa hoc tu NASA:\n{explanation[:300]}...")

    if auto_download and media_type == "image" and img_url:
        ext = "jpg" if ".jpg" in img_url.lower() or ".jpeg" in img_url.lower() else "png"
        filename = f"apod_{date_val}.{ext}"
        client.download_image(img_url, filename)

    print("=" * 68)


def display_mars(client: NasaClient, sol: int = 1000, auto_download: bool = False) -> None:
    print("\n" + "=" * 68)
    print(f"🔴 ANH CHUP TU XE TU HANH CURIOSITY TREN SAO HOA (SOL {sol})")
    print("=" * 68)
    photos = client.get_mars_photos(sol)
    if not photos:
        print(f"[!] Khong tim thay anh chup trong ngay sao hoa Sol {sol}.")
        return

    print(f"[+] Tim thay tong cong {len(photos)} buc anh tu Sao Hoa!")
    top_photos = photos[:3]

    for idx, p in enumerate(top_photos, start=1):
        camera = p.get("camera", {}).get("full_name", "Unknown Camera")
        img_url = p.get("img_src")
        earth_date = p.get("earth_date")
        print(f"\n📸 Anh {idx}:")
        print(f"  - Camera      : {camera}")
        print(f"  - Ngay Trai Dat: {earth_date}")
        print(f"  - Link xem anh: {img_url}")

        if auto_download and idx == 1 and img_url:
            filename = f"mars_sol{sol}_photo1.jpg"
            client.download_image(img_url, filename)

    print("=" * 68)


def display_asteroids(client: NasaClient) -> None:
    print("\n" + "=" * 68)
    print("☄️  THEO DOI THIEN THACH AP SAT TRAI DAT HOM NAY (NASA NeoWs)")
    print("=" * 68)
    asteroids = client.get_near_earth_asteroids()
    if not asteroids:
        print("[*] Khong co thien thach nao dang chu y hoac khong the lay du lieu.")
        return

    print(f"[+] Phat hien {len(asteroids)} thien thach bay qua gan quy dao Trai Dat:")
    for idx, ast in enumerate(asteroids[:5], start=1):
        danger_icon = "⚠️ NGUY HIEM TIEM TANG" if ast["danger"] else "✅ An toan"
        print(f"\n{idx}. Thien thach: {ast['name']} [{danger_icon}]")
        print(f"   - Duong kinh uoc tinh : {ast['min_diameter_m']}m - {ast['max_diameter_m']}m")
        print(f"   - Van toc bay          : {ast['speed_kmh']} km/h")
        print(f"   - Khoang cach toi thieu: {ast['miss_distance_km']} km")
    print("=" * 68)


def interactive_menu(client: NasaClient) -> None:
    """Menu tuong tac terminal truc quan."""
    while True:
        print("\n" + "=" * 68)
        print("🌌 TRUNG TAM KHAM PHA VU TRU NASA & ISS (INTERACTIVE MENU)")
        print("=" * 68)
        print("1. 🛰️  Xem vi tri Tram Vu Tru Quoc Te ISS (Real-time)")
        print("2. 🌌  Xem anh thien van hom nay (NASA APOD)")
        print("3. 📅  Xem va tai anh thien van theo ngay tuy chon (YYYY-MM-DD)")
        print("4. 🔴  Xem anh chup tu xe tu hanh Sao Hoa Curiosity")
        print("5. ☄️   Theo doi cac thien thach dang ap sat Trai Dat")
        print("0. 🚪  Thoat")
        print("=" * 68)

        choice = input("👉 Chon chuc nang (0-5): ").strip()
        if choice == "0":
            print("👋 Tam biet! Chuc ban co nhung hanh trinh kham pha thu vi.")
            break
        elif choice == "1":
            display_iss(client)
        elif choice == "2":
            dl = input("Ban co muon tai anh nay ve may khong? (y/n): ").strip().lower() == "y"
            display_apod(client, auto_download=dl)
        elif choice == "3":
            user_date = input("Nhap ngay can xem (dinh dang YYYY-MM-DD, vd: 2024-07-20): ").strip()
            dl = input("Ban co muon tai anh nay ve may khong? (y/n): ").strip().lower() == "y"
            display_apod(client, date_str=user_date, auto_download=dl)
        elif choice == "4":
            sol_input = input("Nhap ngay Sao Hoa (Sol, mac dinh 1000): ").strip()
            sol_val = int(sol_input) if sol_input.isdigit() else 1000
            dl = input("Ban co muon tai buc anh dau tien ve may khong? (y/n): ").strip().lower() == "y"
            display_mars(client, sol=sol_val, auto_download=dl)
        elif choice == "5":
            display_asteroids(client)
        else:
            print("[!] Lua chon khong hop le, vui long chon tu 0 den 5.")


def main() -> None:
    parser = argparse.ArgumentParser(description="NASA & ISS Space Explorer CLI")
    parser.add_argument("--iss", action="store_true", help="Xem vi tri tram vu tru ISS")
    parser.add_argument("--apod", action="store_true", help="Xem anh thien van NASA APOD")
    parser.add_argument("--date", type=str, help="Chon ngay xem APOD (dinh dang YYYY-MM-DD)")
    parser.add_argument("--mars", action="store_true", help="Xem anh xe tu hanh Sao Hoa")
    parser.add_argument("--sol", type=int, default=1000, help="Ngay Sao Hoa Sol cho Mars Rover (mac dinh: 1000)")
    parser.add_argument("--asteroids", action="store_true", help="Xem danh sach thien thach ap sat Trai Dat")
    parser.add_argument("--download", action="store_true", help="Tu dong tai anh ve thu muc .learner-output")

    args = parser.parse_args()
    client = NasaClient()

    # Neu co tham so dong lenh -> Chay che do CLI chuyen nghiep
    has_flags = any([args.iss, args.apod, args.mars, args.asteroids, args.date])
    if has_flags:
        if args.iss:
            display_iss(client)
        if args.apod or args.date:
            display_apod(client, date_str=args.date, auto_download=args.download)
        if args.mars:
            display_mars(client, sol=args.sol, auto_download=args.download)
        if args.asteroids:
            display_asteroids(client)
    else:
        # Neu nguoi dung chay truc tiep: `python nasa_api.py` -> Bat menu tuong tac
        interactive_menu(client)


if __name__ == "__main__":
    main()

