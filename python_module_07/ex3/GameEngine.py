from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Optional


class GameEngine():
    def __init__(self):
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        hand = [
            self.factory.create_creature(5),
            self.factory.create_creature(2),
            self.factory.create_spell(3)
        ]

        self.cards_created += len(hand)

        battlefield = []

        turn_result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_result.get('damage_dealt', 0)
        return {
            'strategy': self.strategy.get_strategy_name(),
            'hand': '[' + ', '.join([f"{card.name} \
({card.cost})" for card in hand]) + ']',
            'actions': turn_result
        }

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
