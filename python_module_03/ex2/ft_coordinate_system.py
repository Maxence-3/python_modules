def check_value(input):
    try:
        separate = input.split(",")
        for nb in separate:
            int(nb)
        coordinate = tuple(separate)
    except ValueError as e:
        print(e)
    print(coordinate)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    check_value("1, 2, 3")
