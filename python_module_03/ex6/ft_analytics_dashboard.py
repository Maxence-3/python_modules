players_scores: dict[dict[str | int | bool]] = [
    {'name': 'alice', 'score': 2300, 'active': True},
    {'name': 'bob', 'score': 1800, 'active': True},
    {'name': 'charlie', 'score': 2150, 'active': True},
    {'name': 'diana', 'score': 2050, 'active': False}
]


player_achievements: dict[str, list[str]] = {
    'alice': ['first_kill',
              'level_10', 'boss_slayer', 'speed_run', 'collector'],
    'bob': ['first_kill', 'level_10', 'explorer'],
    'charlie': ['first_kill', 'level_10', 'boss_slayer', 'speed_run',
                'collector', 'master', 'legend'],
    'diana': ['first_kill', 'level_10', 'boss_slayer', 'speed_run', 'explorer']
}


player_regions: list[dict[str, str]] = [
    {'player': 'alice', 'region': 'north'},
    {'player': 'bob', 'region': 'east'},
    {'player': 'charlie', 'region': 'central'},
    {'player': 'diana', 'region': 'north'},
    {'player': 'alice', 'region': 'central'}
]


def categorize_score(score: int) -> str:
    if score > 2000:
        return 'high'
    elif score > 1900:
        return 'medium'
    return 'low'


high_scorers: list[str] = [p['name']
                           for p in players_scores if p['score'] > 2000]
scores_doubled: list[int] = [p['score'] * 2 for p in players_scores]
active_players: list[str] = [p['name'] for p in players_scores if p['active']]

player_scores: dict[str, int] = {p['name']: p['score']
                                 for p in players_scores if p['active']}
categories: list[str] = [categorize_score(s) for s in player_scores.values()]


score_categories: dict[str, int] = {cat: categories.count(cat)
                                    for cat in ['high', 'medium', 'low']
                                    if categories.count(cat) > 0}

active_names: set[str] = {p['name'] for p in players_scores if p['active']}
achievement_counts: dict[str, int] = {
    name: len(achievements)
    for name, achievements in player_achievements.items()
    if name in active_names}

unique_players: set[str] = {p['name'] for p in players_scores}
unique_achievements: set[str] = {
    ach for achievements in player_achievements.values()
    for ach in achievements}
active_regions: set[str] = {p['region'] for p in player_regions}

total_players: int = len(unique_players)
total_unique_achievements: int = len(unique_achievements)
average_score: float = sum(player_scores.values()) / len(player_scores)

top_player: dict[str, str | int | bool] = max(
    players_scores, key=lambda p: p['score'])
top_achievements: int = achievement_counts.get(top_player['name'], 0)

if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.1f}")
    print(f"Top performer: {top_player['name']} \
({top_player['score']} points, "f"{top_achievements} achievements)")
