import random
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 power: int,
                 base_rating: int = 1000):
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.power = power
        self.wins = 0
        self.losses = 0
        self.rating = base_rating
        self.card_id = None

    def play(self, game_state: dict) -> dict:
        effect_multiplier = 1 + (self.power / 100)
        effect_value = int(self.cost * effect_multiplier)

        return {
            'card_played': self.name,
            'effect': f"{self.rarity} power activated",
            'effect_value': effect_value,
            'game_state': game_state
        }

    def attack(self, target: 'TournamentCard') -> dict:
        attacker_score = self.power + (self.cost * 0.1) + random.randint(1, 20)
        defender_score = (
            target.power +
            (target.cost * 0.1) + random.randint(1, 20))

        attacker_wins = attacker_score > defender_score
        damage_dealt = int(abs(attacker_score - defender_score))

        return {
            'attacker': self.name,
            'defender': target.name,
            'attacker_score': round(attacker_score, 2),
            'defender_score': round(defender_score, 2),
            'attacker_wins': attacker_wins,
            'damage': damage_dealt
        }

    def defend(self, incoming_damage: int) -> dict:
        reduced = max(0, incoming_damage - (self.power // 4))
        return {
            'card': self.name,
            'incoming_damage': incoming_damage,
            'damage_taken': reduced
        }

    def get_combat_stats(self) -> dict:
        return {
            'name': self.name,
            'power': self.power,
            'cost': self.cost,
            'rarity': self.rarity,
            'combat_rating': self.power + self.cost
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= losses * 16

    def get_rank_info(self) -> dict:
        rank = self._determine_rank()
        return {
            'name': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses,
            'rank': rank,
            'win_rate': self._calculate_win_rate()
        }

    def get_tournament_stats(self) -> dict:
        combat_stats = self.get_combat_stats()
        rank_info = self.get_rank_info()

        interfaces = []
        if isinstance(self, Card):
            interfaces.append("Card")
        if isinstance(self, Combatable):
            interfaces.append("Combatable")
        if isinstance(self, Rankable):
            interfaces.append("Rankable")

        return {
            'id': self.card_id,
            'name': self.name,
            'interfaces': interfaces,
            **combat_stats,
            **rank_info
        }

    def _determine_rank(self) -> str:
        if self.rating >= 1400:
            return "Legendary"
        elif self.rating >= 1300:
            return "Diamond"
        elif self.rating >= 1200:
            return "Gold"
        elif self.rating >= 1100:
            return "Silver"
        else:
            return "Bronze"

    def _calculate_win_rate(self) -> float:
        total = self.wins + self.losses
        if total == 0:
            return 0.0
        return round((self.wins / total) * 100, 1)

    def __str__(self) -> str:
        return (f"{self.name} (ID: {self.card_id}) | "
                f"Rating: {self.rating} | "
                f"Record: {self.wins}-{self.losses}")
