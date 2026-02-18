from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self, name: str):
        self.name = name
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name.lower().replace(' ', '_')}_\
{len(self.cards) + 1:03d}"
        card.card_id = card_id
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        result = card1.attack(card2)

        if result['attacker_wins']:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        sorted_cards = (
            sorted(self.cards.values(), key=lambda c: c.rating, reverse=True))
        leaderboard = []
        for i, card in enumerate(sorted_cards, 1):
            leaderboard.append({
                'rank': i,
                'name': card.name,
                'rating': card.rating,
                'record': f"{card.wins}-{card.losses}"
            })
        return leaderboard

    def generate_tournament_report(self) -> dict:
        all_ratings = [c.rating for c in self.cards.values()]
        avg_rating = (
            int(sum(all_ratings) / len(all_ratings)) if all_ratings else 0)
        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active' if self.cards else 'inactive'
        }
