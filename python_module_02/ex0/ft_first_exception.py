def check_temperature(str_temp: str) -> None:
    test_temperature_input(str_temp)


def test_temperature_input(str_temp: str) -> None:
    temp: int = 0
    print(f"Testing temperature: {str_temp}")
    try:
        temp = int(str_temp)
    except ValueError:
        print(f"Error: '{str_temp}' is not a valid number\n")
        return

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
    else:
        print(f"Temperature {temp}°C is perfect for plants!\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")
