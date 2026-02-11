import math


def coordinate_parser(input: str) -> tuple[int, int, int] | None:
    try:
        separate: list[str] = input.split(",")
        for i in range(0, len(separate)):
            separate[i] = int(separate[i])
        coordinate: tuple[int, int, int] = tuple(separate)
        print(f"Parsed position: {coordinate}")
        return coordinate
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        return None


def calculate_distance(c: tuple[int, int, int]) -> None:
    input_coordinates = c
    result: float = math.sqrt((c[0] - 0)**2 + (c[1] - 0)**2 + (c[2] - 0)**2)
    print(f"Distance between (0, 0, 0) and \
{input_coordinates}: {result:.2f}\n")


def unpacking_tuple(tple: tuple[int, int, int]) -> None:
    print(f"Player at x={tple[0]}, y={tple[1]}, z={tple[2]}")
    (X, Y, Z) = tple
    print(f"Coordiantes: X={X}, Y={Y}, Z={Z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    coordinates: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {coordinates}")
    calculate_distance(coordinates)

    coordinates: str = "3,4,0"
    print(f"Parsing coordinates: \"{coordinates}\"")
    coordinates: tuple[int, int, int] = coordinate_parser(coordinates)
    calculate_distance(coordinates)

    coordinates: str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {coordinates}")
    coordinates = coordinate_parser(coordinates)

    print("Unpacking demonstration:")
    unpacking_tuple((3, 4, 0))
