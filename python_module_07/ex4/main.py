from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...")
    fire_dragon = TournamentCard(
        "Fire Dragon",
        85,
        "dragon",
        75,
        1200
    )

    ice_wizard = TournamentCard(
        "Ice Wizard",
        70,
        "wizard",
        65,
        1150
    )

    platform = TournamentPlatform("DataDeck Tournament")

    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    for card in [fire_dragon, ice_wizard]:
        stats = card.get_tournament_stats()
        print(f"\n{card.name} (ID: {card.card_id}):")
        print(f"- Interfaces: {stats['interfaces']}")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(f"{entry['rank']}. {entry['name']} - Rating: \
{entry['rating']} ({entry['record']})")

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(f"{report}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
