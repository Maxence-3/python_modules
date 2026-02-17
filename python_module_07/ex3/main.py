from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")

    engine = GameEngine()

    print("Configure Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    turn_result = engine.simulate_turn()

    print(f"Hand: {turn_result['hand']}")