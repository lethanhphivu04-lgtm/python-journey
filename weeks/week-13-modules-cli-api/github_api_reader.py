"""Vi du thuc te: Doc du lieu tu mot REST API that tren Internet (GitHub API).
Khong can API key, su dung thu vien chuan urllib va json.
"""

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# Dam bao in duoc tieng Viet co dau tren moi terminal Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def lay_thong_tin_github(username: str) -> None:
    api_url = f"https://api.github.com/users/{username}"
    print("=" * 60)
    print(f"[*] DANG GOI API GITHUB DE LAY DU LIEU NGUOI DUNG: '{username}'")
    print(f"[*] API URL: {api_url}")
    print("=" * 60)

    yeu_cau = Request(api_url, headers={"User-Agent": "Python-Journey-App/1.0"})

    try:
        with urlopen(yeu_cau, timeout=10) as phan_hoi:
            ma_trang_thai = phan_hoi.status
            du_lieu_raw = phan_hoi.read().decode("utf-8")
            user_data = json.loads(du_lieu_raw)

            print(f"[+] Status Code: {ma_trang_thai} (Ket noi thanh cong!)\n")
            print("--- KET QUA NHAN DUOC TU API ---")
            print(f"- Ten day du     : {user_data.get('name')}")
            print(f"- Tai khoan      : {user_data.get('login')}")
            print(f"- Tieu su (Bio)  : {user_data.get('bio')}")
            print(f"- Cong ty / Noi lam: {user_data.get('company')}")
            print(f"- Dia diem       : {user_data.get('location')}")
            print(f"- So Repo mo     : {user_data.get('public_repos')}")
            print(f"- So nguoi theo doi: {user_data.get('followers')}")
            print("=" * 60)

    except HTTPError as e:
        if e.code == 404:
            print(f"[!] LOI: Khong tim thay nguoi dung '{username}' tren GitHub (404 Not Found)!")
        else:
            print(f"[!] LOI HTTP tu Server: {e.code} - {e.reason}")
    except URLError as e:
        print(f"[!] LOI KET NOI MANG: {e.reason}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        user = "torvalds"

    lay_thong_tin_github(user)
