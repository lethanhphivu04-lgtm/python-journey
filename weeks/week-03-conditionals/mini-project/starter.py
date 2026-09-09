"""Starter for the Week 03 Decision Ticket."""

while True:
    # 1. Nhập tên (không để trống)
    while True:
        name = input("Tên: ").strip()
        if name:
            break
        print("Tên không được để trống, vui lòng nhập lại!")

    # 2. Nhập tuổi (phải là số nguyên không âm từ 0 đến 120)
    while True:
        age_text = input("Tuổi: ").strip()
        if age_text.isdigit():
            age = int(age_text)
            if 0 <= age <= 120:
                break
            print("Tuổi phải nằm trong khoảng 0 đến 120, vui lòng nhập lại!")
        else:
            print("Tuổi cần là số nguyên không âm, vui lòng nhập lại!")

    # 3. Nhập loại vé (chỉ nhận standard hoặc vip)
    while True:
        ticket_type = input("Loại vé (standard/vip): ").strip().lower()
        if ticket_type in ("standard", "vip"):
            break
        print("Loại vé chỉ nhận 'standard' hoặc 'vip', vui lòng nhập lại!")

    # 4. Phân loại vé và in kết quả
    if age < 12:
        print(f"{name}: vé trẻ em")
    elif ticket_type == "vip":
        print(f"{name}: vé VIP")
    else:
        print(f"{name}: vé standard")
    # -> Kết quả mẫu (Vux, 20, standard): Vux: vé standard

    # 5. Cho phép nhập tiếp người khác thay vì văng khỏi chương trình
    tiep_tuc = input("\nBạn có muốn nhập vé tiếp theo không? (y/n): ").strip().lower()
    if tiep_tuc != "y":
        print("Đã kết thúc chương trình kiểm tra vé.")
        break
    print("-" * 35)
