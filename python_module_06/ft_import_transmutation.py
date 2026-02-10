import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion

if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    result = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {result}")

    print("\nMethod 2 - Specific function import:")
    result = create_water()
    print(f"create_water(): {result}")

    print("\nMethod 3 - Aliased import:")
    result = heal()
    print(f"heal(): {result}")

    print("\nMethod 4 - Multiple imports:")
    result = create_earth()
    print(f"create_earth(): {result}")
    result = create_fire()
    print(f"create_fire(): {result}")
    result = strength_potion()
    print(f"strength_potion(): {result}")

    print("\nAll import transmutation methods mastered!")