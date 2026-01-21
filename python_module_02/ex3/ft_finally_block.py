def water_plant(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error : {e}")
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("Testing normal watering...")
    water_plant(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plant(["tomato", None])

if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
