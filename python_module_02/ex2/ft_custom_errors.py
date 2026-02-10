class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant: str) -> None:
        super().__init__(f"The {plant} plant is wilting!")
        self.plant = plant


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def check_plant(plant_name: str) -> None:
    raise PlantError(plant_name)


def check_water(level: int) -> None:
    if level < 10:
        raise WaterError()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        check_water(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        check_plant("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water(5)
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")
