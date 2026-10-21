"""Starter for the Student Manager alternative midterm track."""


def calculate_average(student: dict[str, object]) -> float:
    """Return the average of the student's scores."""
    scores = student.get("scores", [])
    if not isinstance(scores, list) or not scores:
        return 0.0
    return sum(float(s) for s in scores) / len(scores)


def classify_student(average: float) -> str:
    """Return an explainable classification from an average."""
    if average >= 8.0:
        return "Giỏi"
    if average >= 6.5:
        return "Khá"
    if average >= 5.0:
        return "Đạt"
    return "Cần cố gắng"


def find_student(
    students: list[dict[str, object]], query: str
) -> dict[str, object] | None:
    """Return the first case-insensitive name match."""
    q = query.strip().lower()
    for student in students:
        if str(student.get("name", "")).strip().lower() == q:
            return student
    return None


def generate_report(students: list[dict[str, object]]) -> str:
    """Return an explainable summary report of all students."""
    if not students:
        return "Danh sách rỗng"
    lines = []
    total_avg = 0.0
    for student in students:
        avg = calculate_average(student)
        total_avg += avg
        lines.append(f"- {student.get('name', '?')}: {avg:.1f} [{classify_student(avg)}]")
    class_avg = total_avg / len(students)
    lines.append(f"Điểm trung bình cả lớp: {class_avg:.2f}")
    return "\n".join(lines)


def main() -> None:
    """Run the starter with sample data and test boundary cases."""
    classroom: list[dict[str, object]] = [
        {"name": "An", "scores": [8.0, 9.0, 7.5]},
        {"name": "Bình", "scores": [7.0, 6.0, 8.0]},
        {"name": "Châu", "scores": []},  # Boundary: điểm rỗng
    ]

    print("=== Báo cáo lớp học ===")
    print(generate_report(classroom))

    print("\n=== Tìm kiếm học sinh ===")
    found = find_student(classroom, "  bình ")
    if found:
        avg = calculate_average(found)
        print(f"Tìm thấy: {found['name']}, Điểm TB: {avg:.1f}, Xếp loại: {classify_student(avg)}")
    else:
        print("Không tìm thấy")

    print("\n=== Boundary case: Danh sách rỗng ===")
    print(generate_report([]))


if __name__ == "__main__":
    main()
