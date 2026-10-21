"""Demo: Doc du lieu tu mot duong link URL tren Internet va luu xuong dia.
Su dung thu vien chuan urllib va json (khong can cai them bat ky thu vien nao).
"""

import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def doc_du_lieu_tu_url(url: str) -> dict | None:
    print("=" * 60)
    print(f"[*] DANG KET NOI VA DOC DU LIEU TU URL:")
    print(f"    {url}")
    print("=" * 60)

    # Tao mot Request voi User-Agent tieu chuan
    req = Request(url, headers={"User-Agent": "Python-Journey-Learner/1.0"})

    try:
        # 1. Mo ket noi va tai du lieu qua mang Internet
        with urlopen(req, timeout=10) as response:
            status_code = response.status
            body_bytes = response.read()

            print(f"[+] Ma trang thai HTTP: {status_code} (OK - Thanh cong)")
            print(f"[+] Kich thuoc du lieu tai ve: {len(body_bytes)} bytes")

            # 2. Giai ma UTF-8 va parse JSON thanh Python Dictionary
            noi_dung_chu = body_bytes.decode("utf-8")
            data = json.loads(noi_dung_chu)
            return data

    except HTTPError as e:
        print(f"[!] Loi HTTP tu Server: {e.code} - {e.reason}")
    except URLError as e:
        print(f"[!] Loi mang hoac khong co Internet: {e.reason}")
    except json.JSONDecodeError:
        print("[!] Loi: Du lieu nhan ve khong phai la JSON hop le.")

    return None


if __name__ == "__main__":
    # Day la mot duong link API cong khai, mien phi 100% tren Internet
    link_api = "https://jsonplaceholder.typicode.com/todos/1"

    # 1. Doc du lieu tu link URL
    ket_qua = doc_du_lieu_tu_url(link_api)

    if ket_qua:
        print("\n--- DU LIEU NHAN DUOC TU INTERNET ---")
        for key, value in ket_qua.items():
            print(f"- {key}: {value}")

        # 2. KET HOP TUAN 10: Luu du lieu vua tai ve vao file tren may ban!
        thu_muc = Path(__file__).resolve().parent / ".learner-output"
        thu_muc.mkdir(parents=True, exist_ok=True)
        file_luu = thu_muc / "downloaded_todo.json"

        file_luu.write_text(
            json.dumps(ket_qua, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"\n-> DA LUU DU LIEU TU URL XUONG FILE: {file_luu.name}")
        print("=" * 60)
