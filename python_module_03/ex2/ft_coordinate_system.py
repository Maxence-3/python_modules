import math


def coordinate_parser(input):
    try:
        separate = input.split(",")
        for i in range(0, len(separate)):
            separate[i] = int(separate[i])
        coordinate = tuple(separate)
        print(f"Parsed position: {coordinate}")
        return coordinate
    except ValueError as e:
        print(f"Error parsing coordinates: {e}\n")


def calculate_distance(c):
    input_coordinates = c
    result = math.sqrt((c[0] - 0)**2 + (c[1] - 0)**2 + (c[2] - 0)**2)
    print(f"Distance between (0, 0, 0) and {input_coordinates}: {result}\n")


def unpacking_tuple(tple):
    print(f"Player at x={tple[0]}, y={tple[1]}, z={tple[2]}")
    (X, Y, Z) = tple
    print(f"Coordiantes: X={X}, Y={Y}, Z={Z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    coordinates = (10, 20, 5)
    print(f"Position created: {coordinates}")
    calculate_distance(coordinates)

    coordinates = "3,4,0"
    print(f"Parsing coordinates: \"{coordinates}\"")
    coordinates = coordinate_parser(coordinates)
    calculate_distance(coordinates)

    coordinates = "abc,def,ghi"
    print(f"Parsong invalid coordinates: {coordinates}")
    coordinates = coordinate_parser(coordinates)

    print("Unpacking demonstration:")
    unpacking_tuple((3, 4, 0))
