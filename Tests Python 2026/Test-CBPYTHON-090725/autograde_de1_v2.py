import subprocess
import os
import ast
import sys
from test_de1 import tests

def normalize(s):
    return s.lower().replace(" ", "").replace(":", "").replace("=", "").strip()

def run_code(file, input_data):
    try:
        env = os.environ.copy()
        env["PYTHONUTF8"] = "1"
        result = subprocess.run(
            [sys.executable, file],
            input=input_data.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=3,
            cwd=os.path.dirname(os.path.abspath(file)),
            env=env
        )
        output = result.stdout.decode("utf-8", errors="replace").strip().splitlines()
        return [line.strip() for line in output if line.strip()]
    except subprocess.TimeoutExpired:
        return ["loiquathoigian"]

def is_dict_expected(expected):
    return isinstance(expected, dict)

def test_dict_output(output, expected_dict):
    for line in output:
        try:
            d = ast.literal_eval(line)
            if isinstance(d, dict) and d == expected_dict:
                return True
        except:
            continue
    return False

def test_normal_output(output, expected):
    expected_norm = normalize(str(expected))
    return any(expected_norm in normalize(out) for out in output)

def get_student_info():
    ho_ten = "Nguyễn Văn A"
    mssv = "MSSV:..."
    may_so = "10"
    try:
        print("📝 Nhập thông tin sinh viên (nhấn Enter để dùng mặc định):")
        nhap_ten = input("  👤 Họ và tên: ").strip()
        if nhap_ten:
            ho_ten = nhap_ten
        nhap_mssv = input("  🆔 MSSV: ").strip()
        if nhap_mssv:
            mssv = nhap_mssv
        nhap_may = input("  🖥️  Số máy (mặc định 10): ").strip()
        if nhap_may:
            may_so = nhap_may
        print()
    except (EOFError, KeyboardInterrupt):
        pass
    return ho_ten, mssv, may_so

def grade(ho_ten="Nguyễn Văn A", mssv="MSSV:...", may_so="10", de_so="01", base_dir=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if base_dir is None:
        candidate = os.path.join(script_dir, "submissions_de1")
        if os.path.exists(candidate) and any(f.endswith(".py") and os.path.getsize(os.path.join(candidate, f)) > 0 for f in os.listdir(candidate)):
            base_dir = candidate
        elif os.path.exists(os.path.join(script_dir, "submissions")):
            base_dir = os.path.join(script_dir, "submissions")
        else:
            base_dir = candidate
    elif not os.path.isabs(base_dir):
        base_dir = os.path.join(script_dir, base_dir)

    total_score = 0
    max_score = 0
    print(f"📋 Bắt đầu chấm điểm cho: {ho_ten} ({mssv})\n")
    for bai, testcases in tests.items():
        file_path = os.path.join(base_dir, f"{bai}.py")
        if not os.path.exists(file_path):
            print(f"❌ Không tìm thấy file: {file_path}")
            continue

        print(f"🔹 {bai.upper()}")
        case_list = testcases if isinstance(testcases, list) else [testcases]
        case_right = 0
        for idx, test in enumerate(case_list, 1):
            output = run_code(file_path, test["input"])
            this_ok = False
            expected_items = test["expected"] if isinstance(test["expected"], list) else [test["expected"]]
            for expected in expected_items:
                if is_dict_expected(expected):
                    if test_dict_output(output, expected):
                        this_ok = True
                        break
                else:
                    if test_normal_output(output, expected):
                        this_ok = True
                        break
            if this_ok:
                print(f"  ✅ Test {idx}: Input {repr(test['input'].strip())} → Đúng")
                case_right += 1
            else:
                print(f"  ❌ Test {idx}: Input {repr(test['input'].strip())} → Sai")
        bai_score = round(case_right / len(case_list), 2)
        total_score += bai_score
        max_score += 1
        print(f"    Kết quả: {case_right}/{len(case_list)} test đúng → {bai_score} điểm\n")

    sv_info = f"{ho_ten} - {mssv}"
    print(f"""
    ╔════════════════════════════════════════════════════╗
    ║ 🎯 Tổng điểm: {total_score}/10
    ║ 👤 Sinh viên: {sv_info}
    ║ 🖥️  Máy số   : {may_so}
    ║ 📄  Đề số    : {de_so}
    ╚════════════════════════════════════════════════════╝
    """)


if __name__ == "__main__":
    ho_ten, mssv, may_so = get_student_info()
    grade(ho_ten=ho_ten, mssv=mssv, may_so=may_so, de_so="01")
