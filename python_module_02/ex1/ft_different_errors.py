def garden_operations(error_type):
    if error_type == "value":
        int("abc")
    if error_type == "zero_division":
        division = 3 / 0
    if error_type == "file_not_found":
        f = open("missing.txt", "r")
    if error_type == "key":
        key = {"rose": 25}
        key["missing_plant"]


def test_error_types():
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
    except:
        print("Caught an error, but program continues!\n")

    print("Alle error types tested successfully!")


if __name__ == "__main__":
    test_error_types()