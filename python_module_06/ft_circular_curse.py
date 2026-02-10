from alchemy.grimoire import validate_ingredients
from alchemy.grimoire import record_spell

if __name__ == "__main__":
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    result = validate_ingredients("fire air")
    print(f"validate_ingredients(\"fire air\"): {result}")
    result = validate_ingredients("dragon scales")
    print(f"validate_ingredients(\"dragon scales\"): {result}")

    print("\nTesting spell recording with validation")
    result = record_spell("Fireball", "fire air")
    print(f"record_spell(\"Fireball\", \"fire air\"): {result}")
    result = record_spell("Dark Magic", "shadow")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {result}")

    print("\nTesting late import technique:")
    result = record_spell("Lightning", "air")
    print(f"record_spell(\"Lightning\", \"air\"): {result}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spell processed safely!")