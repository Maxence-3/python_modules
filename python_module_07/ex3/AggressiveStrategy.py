from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        result = {
            'cards_played': [],
            'mana_used': 0,
            'targets_attacked': [],
            'damage_dealt': 0
        }

        mana_available = 8

        for card in hand:
            cost = card.cost

            if cost <= mana_available:
                result['cards_played'].append(card.name)
                result['mana_used'] += cost
                mana_available -= cost

                result['damage_dealt'] += cost

        if result['cards_played']:
            result['targets_attacked'].append('Enemy Player')

        return result

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(
            available_targets,
            key=lambda t: t.get('priority', 0),
            reverse=True)
