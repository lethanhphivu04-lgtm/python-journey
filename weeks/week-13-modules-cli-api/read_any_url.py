"""Doc va trich xuat tin tuc tu trang Bao Moi (baomoi.com) hoac bat ky URL nao."""

import json
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

# Dam bao in tieng Viet UTF-8 dep
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_DIR = Path(__file__).resolve().parent / ".learner-output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def doc_trang_web(url: str = "https://baomoi.com/") -> None:
    print("=" * 65)
    print(f"[*] DANG KET NOI VA TAI DU LIEU TU: {url}")
    print("=" * 65)

    # Gia lap trinh duyet Chrome de trang web chap nhan ket noi
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    req = Request(url, headers=headers)

    try:
        with urlopen(req, timeout=15) as resp:
            ma_trang_thai = resp.status
            raw_html = resp.read().decode("utf-8", errors="ignore")

            print(f"[+] Ma trang thai HTTP: {ma_trang_thai} (Ket noi thanh cong!)")
            print(f"[+] Kich thuoc trang web: {len(raw_html):,} bytes (~{len(raw_html)//1024} KB)")

            # 1. Trich xuat tieu de trang (<title>)
            match_title = re.search(r"<title>(.*?)</title>", raw_html, re.IGNORECASE | re.DOTALL)
            tieu_de_web = match_title.group(1).strip() if match_title else "Khong co tieu de"
            print(f"[+] Tieu de trang: {tieu_de_web}")

            # 2. Trich xuat cac tieu de tin tuc noi bat
            # Tim cac the chua tieu de tin tren Bao Moi
            cac_tin = []
            # Pattern 1: the a co thuoc tinh title dai hon 20 ky tu
            candidates = re.findall(r'<a[^>]+title=["\']([^"\']{20,})["\']', raw_html)
            for c in candidates:
                c_clean = c.strip()
                if c_clean not in cac_tin and not any(kw in c_clean.lower() for kw in ["báo mới", "baomoi", "logo", "trang chủ"]):
                    cac_tin.append(c_clean)

            print("\n" + "=" * 65)
            print("📰 CAC TIN TUC MOI NHAT VUA DOC DUOC TU BAOMOI.COM:")
            print("=" * 65)

            if cac_tin:
                for i, tin in enumerate(cac_tin[:10], start=1):
                    print(f"{i:2d}. {tin}")
            else:
                print("Da tai duoc HTML nhung can parser chuyen dung de boc tach the.")

            # 3. KET HOP PERSISTENCE (TUAN 10): Luu danh sach tin tuc nay xuong file
            file_luu = OUTPUT_DIR / "tin_tuc_baomoi.txt"
            noi_dung_luu = f"TIEU DE: {tieu_de_web}\nNGUON: {url}\n\nDANH SACH TIN TUC:\n"
            for i, tin in enumerate(cac_tin[:20], start=1):
                noi_dung_luu += f"{i}. {tin}\n"

            file_luu.write_text(noi_dung_luu, encoding="utf-8")
            print("\n" + "=" * 65)
            print(f"-> DA LUU TOAN BO TIN TUC XUONG FILE: {file_luu.name}")
            print(f"   (Duong dan: {file_luu})")
            print("=" * 65)

    except Exception as e:
        print(f"[!] Loi khi doc URL: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        target_url = "https://baomoi.com/"

    doc_trang_web(target_url)
