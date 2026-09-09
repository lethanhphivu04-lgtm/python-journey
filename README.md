# 🐍 Nhật Ký Học Tập & Thực Hành — Lập Trình Python

> **Hồ sơ học tập và thực hành môn Lập Trình Python theo phương pháp học qua làm.**

![Python Journey Banner](assets/banner.png)

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Status](https://img.shields.io/badge/Status-In%20Progress-f59e0b?style=flat-square)](#-bảng-theo-dõi-tiến-độ-15-tuần)
[![School](https://img.shields.io/badge/Trường-Cao%20Đẳng%20Công%20Thương-0284c7?style=flat-square)](https://hitu.edu.vn)

---

## 📌 Thông tin sinh viên & Học phần

| Mục | Chi tiết |
|:---|:---|
| **Họ và tên:** | **Lê Thanh Phi Vũ** |
| **MSSV:** | **2123110178** |
| **Trường:** | **Trường Cao đẳng Công Thương** |
| **Môn học:** | **Lập Trình Python** |
| **Môi trường:** | Python `>= 3.12` · VS Code · Git / GitHub · PowerShell |
| **Mô hình học tập:** | `Learn → Build → Test → Debug → Improve → Commit → Prove` |

---

## 🎯 Mục tiêu học tập cá nhân

1. **Nền tảng vững chắc:** Nắm vững cú pháp chuẩn của Python (từ Python 3.12 trở lên) và tuân thủ [Style Guide (PEP 8)](STYLE_GUIDE.md).
2. **Kỹ năng giải quyết bài toán:** Biết phân rã vấn đề phức tạp thành các hàm nhỏ có trách nhiệm rõ ràng, áp dụng cấu trúc dữ liệu phù hợp.
3. **Thao tác dữ liệu thực tế:** Đọc, ghi và xử lý các định dạng dữ liệu thông dụng (Text, CSV, JSON) bằng `pathlib` và thư viện chuẩn.
4. **Kiểm thử & Debug có phương pháp:** Tự viết kiểm thử với `pytest`, biết đọc traceback, khoanh vùng lỗi và khắc phục sự cố thay vì đoán mò.
5. **Kỷ luật mã nguồn:** Xây dựng thói quen quản lý phiên bản với Git/GitHub, ghi chú commit rõ ràng, lưu trữ bằng chứng hoàn thành từng tuần.
6. **Sản phẩm hoàn chỉnh:** Hoàn thành xuất sắc [Dự án Giữa khóa (Midterm)](weeks/week-09-midterm-project/README.md) và [Dự án Cuối khóa (Capstone)](FINAL_PROJECT.md).

---

## 🗺️ Bảng theo dõi tiến độ 15 tuần

Chi tiết danh sách tự kiểm tra từng tiêu chí xem tại: [Bảng theo dõi tiến trình (PROGRESS.md)](PROGRESS.md).

### Giai đoạn 1: Nền tảng & Cấu trúc điều khiển

| Tuần | Chủ đề | Trọng tâm bài tập | Trạng thái |
|:---:|:---|:---|:---:|
| **01** | [Môi trường & Hello Python](weeks/week-01-hello-python/README.md) | Terminal, REPL, lệnh `print()`, commit đầu tiên | 🟢 Hoàn thành |
| **02** | [Biến & Kiểu dữ liệu](weeks/week-02-variables-types/README.md) | `int`, `float`, `str`, `bool`, `input()`, ép kiểu | 🟢 Hoàn thành |
| **03** | [Cấu trúc điều kiện](weeks/week-03-conditionals/README.md) | `if/elif/else`, toán tử logic, kiểm tra dữ liệu đầu vào | 🟢 Hoàn thành |

### Giai đoạn 2: Dữ liệu & Tư duy thuật toán

| Tuần | Chủ đề | Trọng tâm bài tập | Trạng thái |
|:---:|:---|:---|:---:|
| **04** | [Xử lý chuỗi (Strings)](weeks/week-04-strings/README.md) | String slicing, methods, f-strings, Regex mini-lab | 🟢 Hoàn thành |
| **05** | [Lists & Tuples](weeks/week-05-lists-tuples/README.md) | CRUD list, tính khả biến (mutability), unpacking | 🟢 Hoàn thành |
| **06** | [Vòng lặp (Loops)](weeks/week-06-loops/README.md) | `for`, `while`, `enumerate()`, `zip()`, comprehensions | 🟢 Hoàn thành |
| **07** | [Hàm & Phân rã bài toán](weeks/week-07-functions/README.md) | `def`, phạm vi biến, type hints, Utility toolkit | ⚪ Chưa bắt đầu |
| **08** | [Dictionaries & Sets](weeks/week-08-dicts-sets/README.md) | Key-value mapping, set operations, mô hình dữ liệu | ⚪ Chưa bắt đầu |

### Cột mốc giữa khóa 🏆

| Tuần | Chủ đề | Sản phẩm bàn giao | Trạng thái |
|:---:|:---|:---|:---:|
| **09** | [Midterm Project](weeks/week-09-midterm-project/README.md) | Ứng dụng Console tổng hợp W01–W08 có cấu trúc hoàn chỉnh | ⚪ Chưa bắt đầu |

### Giai đoạn 3: Viết chương trình đáng tin cậy

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

## 🚀 Hướng dẫn chạy và thực hành bài tập

### 1. Cài đặt môi trường
Xem chi tiết hướng dẫn thiết lập tại [SETUP.md](SETUP.md).

### 2. Quy trình làm bài mỗi tuần
Trong mỗi thư mục tuần (ví dụ: [weeks/week-01-hello-python](weeks/week-01-hello-python/)):
1. **Lý thuyết:** Đọc `notes.md` và chạy thử code trong `examples/`.
2. **Làm bài tập:** Mở các file trong `exercises/`, hoàn thành các mục `# TODO` và chạy thử:
   ```bash
   python weeks/week-01-hello-python/exercises/ex01_hello.py
   ```
3. **Khi cần gợi ý:** Mở `hints.md` trước khi xem đáp án tại `solutions/`.
4. **Mini-project:** Thực hiện yêu cầu trong `mini-project/README.md`.
5. **Cập nhật tiến độ:** Đánh dấu hoàn thành trong [PROGRESS.md](PROGRESS.md).

---

## 📚 Tài liệu tham khảo nhanh

- [Đề cương chi tiết (SYLLABUS.md)](SYLLABUS.md)
- [Bảng theo dõi tiến trình (PROGRESS.md)](PROGRESS.md)
- [Chuẩn phong cách code (STYLE_GUIDE.md)](STYLE_GUIDE.md)
- [Yêu cầu đồ án cuối khóa (FINAL_PROJECT.md)](FINAL_PROJECT.md)
- [Dự án mở rộng: VuaCóc Bot Journey](projects/vuacoc-bot-journey/README.md)
