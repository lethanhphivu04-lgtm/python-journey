"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect a successful offline response fixture."""
    data = parse_json_response(200, fixture)
    assert data["lesson"] == 13, f"Expected lesson == 13, got {data.get('lesson')}"
    print(f"Parsed response (status 200): {data}")

    try:
        parse_json_response(500, fixture)
    except ValueError as error:
        print(f"Observed expected ValueError (status 500): {error}")


if __name__ == "__main__":
    main()
