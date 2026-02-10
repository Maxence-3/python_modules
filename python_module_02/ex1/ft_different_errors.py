def garden_operations(error_type: str) -> None:
    if error_type == "value":
        int("abc")
    elif error_type == "zero_division":
        _ = 3 / 0
    elif error_type == "file_not_found":
        with open("missing.txt", "r") as f:
            _ = f
    elif error_type == "key":
        plants = {"rose": 25}
        _ = plants["missing_plant"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations("zero_division")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        garden_operations("file_not_found")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        print("Testing KeyError...")
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        print("Testing multiple errors together...")
        garden_operations("value")
        garden_operations("zero_division")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
