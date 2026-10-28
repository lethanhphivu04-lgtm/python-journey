# 🐍 Python Journey — Nhật Ký Học Tập & Thực Hành Lập Trình Python

> **Hồ sơ học tập, mã nguồn thực hành và tài liệu giải thuật môn Lập Trình Python theo phương pháp "Học Qua Làm" (Learning by Doing).**

![Python Journey Banner](assets/banner.png)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![VS Code](https://img.shields.io/badge/IDE-VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Git](https://img.shields.io/badge/VCS-Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/Repo-GitHub-181717?style=for-the-badge&logo=github)](https://github.com/lethanhphivu04-lgtm/python-journey)
[![Status](https://img.shields.io/badge/Tiến_độ-15%2F15_Tuần_(100%25)-22c55e?style=for-the-badge)](#-bảng-theo-dõi-tiến-độ-15-tuần)
[![Code Style](https://img.shields.io/badge/Style-PEP_8-blue?style=for-the-badge)](STYLE_GUIDE.md)

</div>

---

## 📌 Thông tin sinh viên & Học phần

| Mục | Chi tiết |
|:---|:---|
| **Họ và tên:** | **Lê Thanh Phi Vũ** |
| **Mã số sinh viên (MSSV):** | **2123110178** |
| **Email:** | [lethanhphivu04@gmail.com](mailto:lethanhphivu04@gmail.com) |
| **GitHub:** | [@lethanhphivu04-lgtm](https://github.com/lethanhphivu04-lgtm) |
| **Cơ sở đào tạo:** | **Trường Cao đẳng Công Thương TP.HCM (HITU)** |
| **Môn học:** | **Lập Trình Python** |
| **Môi trường phát triển:** | Python `>= 3.12` (Python 3.14) · VS Code · PowerShell · Git |
| **Mô hình học tập:** | `Learn → Build → Test → Debug → Improve → Commit → Prove` |

---

## 💡 Triết lý & Tiêu chuẩn kỹ thuật (Engineering Standards)

Mỗi dòng code trong kho lưu trữ này được xây dựng dựa trên 4 nguyên tắc cốt lõi:

1. **Chuẩn phong cách (PEP 8 Compliant):** Đặt tên biến và hàm theo chuẩn `snake_case`, tách hàm rõ ràng, định dạng code sạch sẽ.
2. **Lập trình phòng thủ (Defensive Coding):** Kiểm tra tính hợp lệ của dữ liệu đầu vào (`input validation`), dùng vòng lặp yêu cầu nhập lại thay vì để chương trình gặp lỗi đột ngột.
3. **Ưu tiên thư viện chuẩn (Standard Library First):** Tận dụng các thư viện có sẵn của Python như `math`, `re`, `pathlib`, `json`, `csv` trước khi sử dụng thư viện bên ngoài.
4. **Kiểm thử & Minh chứng (Evidence over Assumption):** Sử dụng kết quả mẫu, kiểm thử tự động và các công cụ xác minh để đánh giá tính đúng đắn của chương trình.

---

## 📁 Cấu trúc kho lưu trữ (Repository Structure)

```text
python-journey/
├── weeks/                              # 15 tuần học tập từ cơ bản đến nâng cao
│   ├── week-01-hello-python/           # Cài đặt, REPL, print, tổng kết giải thuật W1
│   ├── week-02-variables-types/        # Biến, kiểu dữ liệu, input/output
│   ├── week-03-conditionals/           # if/elif/else, logic, mini-project vé xem phim
│   ├── week-04-strings/                # Chuỗi, f-string, regex, phân tích text
│   ├── week-05-lists-tuples/           # CRUD list, mutability, unpacking
│   ├── week-06-loops/                  # for, while, enumerate, zip, comprehensions
│   ├── week-07-functions/              # Hàm, phạm vi biến, type hints
│   ├── week-08-dicts-sets/             # Dictionaries, sets, data modeling
│   ├── week-09-midterm-project/        # Dự án giữa kỳ
│   ├── week-10-files-io/               # Đọc/ghi tệp, CSV, JSON
│   ├── week-11-exceptions/             # Ngoại lệ, xử lý lỗi, debugging
│   ├── week-12-testing-pytest/         # Unit testing, pytest
│   ├── week-13-modules-cli-api/        # Modules, CLI, HTTP API
│   ├── week-14-oop-essentials/         # Lập trình hướng đối tượng
│   └── week-15-capstone-project/       # Đồ án cuối khóa
├── scripts/                            # Scripts kiểm tra tính toàn vẹn
├── tests/                              # Bộ kiểm thử tự động
├── README.md                           # Trang chủ dự án & hồ sơ học tập
├── PROGRESS.md                         # Bảng theo dõi tiến trình
├── SYLLABUS.md                         # Đề cương môn học
├── STYLE_GUIDE.md                      # Quy tắc viết code Python
└── FINAL_PROJECT.md                    # Đặc tả đồ án cuối khóa
```

---

## 🗺️ Bảng theo dõi tiến độ 15 tuần

> **Tiến độ hiển thị: 15/15 tuần — 100%.**
>
> Chi tiết tiêu chí theo dõi: [Bảng theo dõi tiến trình (PROGRESS.md)](PROGRESS.md).

### Giai đoạn 1: Nền tảng & Cấu trúc điều khiển

| Tuần | Chủ đề | Trọng tâm bài tập | Tài liệu đúc kết | Trạng thái |
|:---:|:---|:---|:---:|:---:|
| **01** | [Môi trường & Hello Python](weeks/week-01-hello-python/README.md) | Terminal, REPL, `print()`, lệnh tính toán | [tongketweek1.md](weeks/week-01-hello-python/tongketweek1.md) | 🟢 Hoàn thành |
| **02** | [Biến & Kiểu dữ liệu](weeks/week-02-variables-types/README.md) | `int`, `float`, `str`, `bool`, `input()`, ép kiểu | [tongketweek2.md](weeks/week-02-variables-types/tongketweek2.md) | 🟢 Hoàn thành |
| **03** | [Cấu trúc điều kiện](weeks/week-03-conditionals/README.md) | `if/elif/else`, toán tử logic, validate dữ liệu | [tongketweek3.md](weeks/week-03-conditionals/tongketweek3.md) | 🟢 Hoàn thành |

### Giai đoạn 2: Dữ liệu & Tư duy thuật toán

| Tuần | Chủ đề | Trọng tâm bài tập | Tài liệu đúc kết | Trạng thái |
|:---:|:---|:---|:---:|:---:|
| **04** | [Xử lý chuỗi (Strings)](weeks/week-04-strings/README.md) | String slicing, methods, f-strings, Regex | [tongketweek4.md](weeks/week-04-strings/tongketweek4.md) | 🟢 Hoàn thành |
| **05** | [Lists & Tuples](weeks/week-05-lists-tuples/README.md) | CRUD list, tính khả biến, unpacking | [tongketweek5.md](weeks/week-05-lists-tuples/tongketweek5.md) | 🟢 Hoàn thành |
| **06** | [Vòng lặp (Loops)](weeks/week-06-loops/README.md) | `for`, `while`, `enumerate()`, comprehensions | [tongketweek6.md](weeks/week-06-loops/tongketweek6.md) | 🟢 Hoàn thành |
| **07** | [Hàm & Phân rã bài toán](weeks/week-07-functions/README.md) | `def`, phạm vi biến, type hints, Utility toolkit | — | 🟢 Hoàn thành |
| **08** | [Dictionaries & Sets](weeks/week-08-dicts-sets/README.md) | Key-value mapping, set operations, data modeling | — | 🟢 Hoàn thành |

### Cột mốc giữa khóa 🏆

| Tuần | Chủ đề | Sản phẩm bàn giao | Trạng thái |
|:---:|:---|:---|:---:|
| **09** | [Midterm Project](weeks/week-09-midterm-project/README.md) | Ứng dụng Console tổng hợp kiến thức W01–W08 | 🟢 Hoàn thành |

### Giai đoạn 3: Kỹ thuật phần mềm & Ứng dụng thực tế

| Tuần | Chủ đề | Trọng tâm bài tập | Trạng thái |
|:---:|:---|:---|:---:|
| **10** | [Tệp tin & Dữ liệu (File I/O)](weeks/week-10-files-io/README.md) | Đọc/ghi text, `pathlib`, CSV, JSON với `with` | 🟢 Hoàn thành |
| **11** | [Ngoại lệ & Debugging](weeks/week-11-exceptions/README.md) | `try/except`, traceback, debug phòng vệ | 🟢 Hoàn thành |
| **12** | [Kiểm thử với pytest](weeks/week-12-testing-pytest/README.md) | Unit tests, Arrange-Act-Assert, edge cases | 🟢 Hoàn thành |
| **13** | [Modules, CLI & API](weeks/week-13-modules-cli-api/README.md) | Module hóa, CLI, gọi HTTP API cơ bản | 🟢 Hoàn thành |
| **14** | [Lập trình hướng đối tượng (OOP)](weeks/week-14-oop-essentials/README.md) | Class, object, `__init__`, `self`, composition | 🟢 Hoàn thành |

### Cột mốc tốt nghiệp 🎓

| Tuần | Chủ đề | Sản phẩm bàn giao | Trạng thái |
|:---:|:---|:---|:---:|
| **15** | [Capstone Project](weeks/week-15-capstone-project/README.md) | Đồ án cuối kỳ: Code, Tests, tài liệu theo [FINAL_PROJECT.md](FINAL_PROJECT.md) | 🟢 Hoàn thành |

---

## 🚀 Hướng dẫn chạy và kiểm tra mã nguồn

### 1. Kiểm tra tính toàn vẹn của toàn bộ khóa học

Tại thư mục gốc của dự án, chạy:

```bash
python scripts/verify_course.py
```

Kết quả mong đợi khi toàn bộ kiểm tra thực sự đạt yêu cầu:

```text
Python Journey course verification: PASS
```

### 2. Kiểm tra lời giải bài tập các tuần

Ví dụ kiểm tra Tuần 02:

```bash
python weeks/week-02-variables-types/checks/check_solutions.py
```

### 3. Chạy thử bài tập thực hành

Ví dụ chạy mini-project Tuần 03:

```bash
python weeks/week-03-conditionals/mini-project/starter.py
```

---

## 📚 Tài liệu tham khảo & Đường dẫn quan trọng

- [Đề cương chi tiết (SYLLABUS.md)](SYLLABUS.md)
- [Bảng theo dõi tiến trình (PROGRESS.md)](PROGRESS.md)
- [Chuẩn phong cách code (STYLE_GUIDE.md)](STYLE_GUIDE.md)
- [Yêu cầu đồ án cuối khóa (FINAL_PROJECT.md)](FINAL_PROJECT.md)
- [Dự án mở rộng: VuaCóc Bot Journey](projects/vuacoc-bot-journey/README.md)

---

<div align="center">

**Lê Thanh Phi Vũ · 2123110178**

Trường Cao đẳng Công Thương TP.HCM (HITU) · Khoa Công Nghệ Thông Tin

*Dự án học tập liên tục được cập nhật theo tiến độ giảng dạy.*

</div>
