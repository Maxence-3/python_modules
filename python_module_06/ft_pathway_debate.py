from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
import alchemy


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    result = lead_to_gold()
    print(f"lead_to_gold(): {result}")
    result = stone_to_gem()
    print(f"stone_to_gem(): {result}")

    print("\nTesting Relative Imports (from advanced.py):")
    result = philosophers_stone()
    print(f"philosophers_stone(): {result}")
    result = elixir_of_life()
    print(f"elixir_of_life(): {result}")

    print("\nTesting Package Access:")
    result = alchemy.transmutation.lead_to_gold()
    print(f"alchemy.transmutation.lead_to_gold(): {result}")
    result = alchemy.transmutation.philosophers_stone()
    print(f"alchemy.transmutation.philosophers_stone(): {result}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
