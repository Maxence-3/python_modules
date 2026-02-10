import alchemy
from alchemy.potions import healing_potion as heal

if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    alchemy.elements.create_fire()

    print("Method 2 - Specific function import:")
    alchemy.create_water()

    print("Method 3 - Aliased import:")
    heal()