"""Demo: Doc API thoi tiet truc tiep tai TP.HCM qua Open-Meteo API.
Mien phi 100%, khong can API key hay dang ky tai khoan.
"""

import json
import sys
from urllib.request import urlopen

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def xem_thoi_tiet_hcm() -> None:
    # Toa do cua TP. Ho Chi Minh: vi do 10.8231, kinh do 106.6297
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        "latitude=10.8231&longitude=106.6297&"
        "current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day"
    )

    print("=" * 60)
    print("[*] DANG KET NOI VAO API THOI TIET (OPEN-METEO)...")
    print(f"[*] URL: {url}")
    print("=" * 60)

    with urlopen(url, timeout=10) as phan_hoi:
        data = json.loads(phan_hoi.read().decode("utf-8"))
        current = data["current"]

        nhiet_do = current["temperature_2m"]
        do_am = current["relative_humidity_2m"]
        cam_giac_nhu = current["apparent_temperature"]
        ban_ngay = "Ban ngay" if current["is_day"] == 1 else "Ban dem"

        print("[+] KET NOI THANH CONG!")
        print("\n--- THOI TIET HIEN TAI TAI TP. HO CHI MINH ---")
        print(f"- Thoi diem       : {ban_ngay}")
        print(f"- Nhiet do thuc te: {nhiet_do} do C")
        print(f"- Cam giac nhu    : {cam_giac_nhu} do C")
        print(f"- Do am khong khi : {do_am} %")
        print("=" * 60)


if __name__ == "__main__":
    xem_thoi_tiet_hcm()
