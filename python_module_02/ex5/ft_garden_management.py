from typing import Dict, List, Optional


class GardenError(Exception):
    pass


class PlantValueError(GardenError):
    def __init__(self, message: str = "Plant name cannot be empty!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in tank") -> None:
        super().__init__(message)


class GardenManager:
    def __init__(self, water_tank: int) -> None:
        self.plants: Dict[str, Dict[str, int]] = {}
        self.water_tank = water_tank

    def add_plant(self, plant_name: Optional[str], water_level: Optional[int],
                  sunlight_hours: Optional[int]) -> None:
        try:
            if plant_name is None or plant_name == "":
                raise PlantValueError()
            self.plants[plant_name] = {'water': water_level,
                                       'sunlight': sunlight_hours}
            print(f"Added {plant_name} successfully")
        except PlantValueError as e:
            print(f"Error adding plant: {e}")

    def watering_plants(self, plant_names: List[str]) -> None:
        print("Opening watering system")
        try:
            for plant in plant_names:
                if plant is None:
                    raise ValueError("Cannot water None - invalid plant!")
                print(f"Watering {plant} - success")
        except ValueError as e:
            print(f"Error watering plant: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> None:
        water_level = self.plants[plant_name]['water']
        sunlight_hours = self.plants[plant_name]['sunlight']

        try:
            if water_level > 10:
                raise ValueError(f"Water level {water_level} \
 is too high (max 10)")
            elif sunlight_hours < 2:
                raise ValueError(f"Sunlight hours {sunlight_hours} \
is too low (min 2)")
            else:
                print(f"{plant_name}: healthy (water: {water_level}, \
sun: {sunlight_hours})")
        except ValueError as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    garden = GardenManager(5)

    print("Adding plants to garden...")
    garden.add_plant("tomato", 5, 8)
    garden.add_plant("lettuce", 15, 6)
    garden.add_plant(None, None, None)

    print("\nWatering plants...")
    garden.watering_plants(["tomato", "lettuce"])

    print("\nChecking plant health...")
    garden.check_plant_health("tomato")
    garden.check_plant_health("lettuce")

    print("\nTesting error recovery...")
    try:
        if garden.water_tank < 10:
            raise WaterError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
