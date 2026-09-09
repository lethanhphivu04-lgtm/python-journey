# 🐍 Python Journey — Nhật Ký Học Tập & Thực Hành Lập Trình Python

> **Hồ sơ học tập, mã nguồn thực hành và tài liệu giải thuật môn Lập Trình Python theo phương pháp "Học Qua Làm" (Learning by Doing).**

![Python Journey Banner](assets/banner.png)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![VS Code](https://img.shields.io/badge/IDE-VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Git](https://img.shields.io/badge/VCS-Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/Repo-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lethanhphivu04-lgtm/python-journey)
[![Status](https://img.shields.io/badge/Tiến_độ-6%2F15_Tuần_(40%25)-22c55e?style=for-the-badge)](#-bảng-theo-dõi-tiến-độ-15-tuần)
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
2. **Lập trình phòng thủ (Defensive Coding):** Luôn kiểm tra tính hợp lệ của dữ liệu đầu vào (`input validation`), dùng vòng lặp yêu cầu nhập lại thay vì để chương trình bị crash/văng lỗi đột ngột.
3. **Ưu tiên thư viện chuẩn (Standard Library First):** Tận dụng tối đa sức mạnh sẵn có của Python (`math`, `re`, `pathlib`, `json`, `csv`) trước khi phụ thuộc vào thư viện bên ngoài.
4. **Kiểm thử tự động & Minh chứng (Evidence over Assumption):** Mọi bài tập đều có kết quả mẫu minh họa (`# -> Kết quả: ...`), vượt qua 100% các bài kiểm tra tự động (`verify_course: PASS`, `check_solutions: PASS`).

---

## 📁 Cấu trúc kho lưu trữ (Repository Structure)

```text
python-journey/
├── weeks/                              # 15 tuần học tập từ cơ bản đến nâng cao
│   ├── week-01-hello-python/           # Cài đặt, REPL, print, tổng kết giải thuật W1
│   ├── week-02-variables-types/        # Biến, ép kiểu, input/output, tổng kết W2
│   ├── week-03-conditionals/           # if/elif/else, logic, mini-project vé xem phim
│   ├── week-04-strings/                # Chuỗi, format f-string, regex, phân tích text
│   ├── week-05-lists-tuples/           # Danh sách, tuple, mutability, unpacking
│   ├── week-06-loops/                  # for, while, enumerate, zip, comprehensions
│   ├── week-07-functions/ ... week-15/ # Các tuần tiếp theo & Đồ án cuối khóa
├── scripts/                            # Scripts kiểm tra tính toàn vẹn (verify_course.py)
├── tests/                              # Bộ kiểm thử tự động (Repository Invariants)
├── README.md                           # Trang chủ dự án & Hồ sơ học tập
├── PROGRESS.md                         # Bảng tự đánh giá tiến trình chi tiết
├── SYLLABUS.md                         # Đề cương môn học chuẩn
├── STYLE_GUIDE.md                      # Quy tắc viết code chuẩn Python
└── FINAL_PROJECT.md                    # Đặc tả yêu cầu đồ án tốt nghiệp Capstone
```

---

## 🗺️ Bảng theo dõi tiến độ 15 tuần

> Chi tiết danh sách tự kiểm tra từng tiêu chí xem tại: [Bảng theo dõi tiến trình (PROGRESS.md)](PROGRESS.md).

### Giai đoạn 1: Nền tảng & Cấu trúc điều khiển

| Tuần | Chủ đề | Trọng tâm bài tập | Tài liệu đúc kết | Trạng thái |
|:---:|:---|:---|:---:|:---:|
| **01** | [Môi trường & Hello Python](weeks/week-01-hello-python/README.md) | Terminal, REPL, `print()`, lệnh tính toán | [tongketweek1.md](weeks/week-01-hello-python/tongketweek1.md) | 🟢 Hoàn thành |
| **02** | [Biến & Kiểu dữ liệu](weeks/week-02-variables-types/README.md) | `int`, `float`, `str`, `bool`, `input()`, ép kiểu | [tongketweek2.md](weeks/week-02-variables-types/tongketweek2.md) | 🟢 Hoàn thành |
| **03** | [Cấu trúc điều kiện](weeks/week-03-conditionals/README.md) | `if/elif/else`, toán tử logic, validate vé | [tongketweek3.md](weeks/week-03-conditionals/tongketweek3.md) | 🟢 Hoàn thành |

### Giai đoạn 2: Dữ liệu & Tư duy thuật toán

| Tuần | Chủ đề | Trọng tâm bài tập | Tài liệu đúc kết | Trạng thái |
|:---:|:---|:---|:---:|:---:|
| **04** | [Xử lý chuỗi (Strings)](weeks/week-04-strings/README.md) | String slicing, methods, f-strings, Regex | [tongketweek4.md](weeks/week-04-strings/tongketweek4.md) | 🟢 Hoàn thành |
| **05** | [Lists & Tuples](weeks/week-05-lists-tuples/README.md) | CRUD list, tính khả biến, unpacking | [tongketweek5.md](weeks/week-05-lists-tuples/tongketweek5.md) | 🟢 Hoàn thành |
| **06** | [Vòng lặp (Loops)](weeks/week-06-loops/README.md) | `for`, `while`, `enumerate()`, comprehensions | [tongketweek6.md](weeks/week-06-loops/tongketweek6.md) | 🟢 Hoàn thành |
| **07** | [Hàm & Phân rã bài toán](weeks/week-07-functions/README.md) | `def`, phạm vi biến, type hints, Utility toolkit | — | ⚪ Sắp học |
| **08** | [Dictionaries & Sets](weeks/week-08-dicts-sets/README.md) | Key-value mapping, set operations, data modeling | — | ⚪ Chưa bắt đầu |

### Cột mốc giữa khóa 🏆

| Tuần | Chủ đề | Sản phẩm bàn giao | Trạng thái |
|:---:|:---|:---|:---:|
| **09** | [Midterm Project](weeks/week-09-midterm-project/README.md) | Ứng dụng Console tổng hợp W01–W08 có cấu trúc hoàn chỉnh | ⚪ Chưa bắt đầu |

### Giai đoạn 3: Kỹ thuật phần mềm & Ứng dụng thực tế

| Tuần | Chủ đề | Trọng tâm bài tập | Trạng thái |
|:---:|:---|:---|:---:|
| **10** | [Tệp tin & Dữ liệu (File I/O)](weeks/week-10-files-io/README.md) | Đọc/ghi text, `pathlib`, CSV, JSON với `with` context | ⚪ Chưa bắt đầu |
| **11** | [Ngoại lệ & Debugging](weeks/week-11-exceptions/README.md) | `try/except`, traceback, debug phòng vệ | ⚪ Chưa bắt đầu |
| **12** | [Kiểm thử với pytest](weeks/week-12-testing-pytest/README.md) | Viết unit tests, mẫu Arrange-Act-Assert, test edge cases | ⚪ Chưa bắt đầu |
| **13** | [Modules, CLI & API](weeks/week-13-modules-cli-api/README.md) | Module hóa, tham số dòng lệnh CLI, gọi HTTP API cơ bản | ⚪ Chưa bắt đầu |
| **14** | [Lập trình hướng đối tượng (OOP)](weeks/week-14-oop-essentials/README.md) | Class, object, `__init__`, `self`, composition cơ bản | ⚪ Chưa bắt đầu |

### Cột mốc tốt nghiệp 🎓

| Tuần | Chủ đề | Sản phẩm bàn giao | Trạng thái |
|:---:|:---|:---|:---:|
| **15** | [Capstone Project](weeks/week-15-capstone-project/README.md) | Đồ án cuối kỳ hoàn chỉnh: Code, Tests, Tài liệu theo [FINAL_PROJECT.md](FINAL_PROJECT.md) | ⚪ Chưa bắt đầu |

---

## 🚀 Hướng dẫn chạy và kiểm tra mã nguồn

### 1. Kiểm tra tính toàn vẹn của toàn bộ khóa học
Trong thư mục gốc của dự án, chạy lệnh:
```bash
python scripts/verify_course.py
```
*(Kết quả kỳ vọng: `Python Journey course verification: PASS`)*

### 2. Kiểm tra lời giải bài tập các tuần (Solution Checks)
```bash
# Chạy kiểm tra từng tuần (ví dụ Tuần 02):
python weeks/week-02-variables-types/checks/check_solutions.py
```

### 3. Chạy thử các bài tập thực hành
Mỗi bài tập có thể chạy độc lập trực tiếp từ terminal:
```bash
# Ví dụ chạy bài tập điều kiện Tuần 03:
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
