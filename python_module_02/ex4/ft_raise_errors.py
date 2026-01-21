def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name is None:
            raise ValueError(f"Plant name cannot be empty!")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        else:
            print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")

def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    check_plant_health("tomato", 5, 5)

    print("\nTesting empty plant name...")
    check_plant_health(None, 5, 5)
    
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 5)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)

    print("\nAll error raising tests completed!")

if __name__ == "__main__":
    test_plant_checks()
