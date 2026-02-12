import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total_card = len(self.cards)
        total_cost = 0

        creatures = 0
        artifacts = 0
        spells = 0

        for card in self.cards:
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            elif isinstance(card, SpellCard):
                spells += 1

        avg_cost = total_cost/total_card
        return {
            'total_cards': total_card,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': round(avg_cost, 1)
            }
