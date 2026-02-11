def rare_achievement(
        alice: set[str],
        bob: set[str],
        charlie: set[str]) -> set[str]:
    rare: set[str] = set()

    for achievement in alice:
        if achievement not in bob and achievement not in charlie:
            rare.add(achievement)
    for achievement in bob:
        if achievement not in alice and achievement not in charlie:
            rare.add(achievement)
    for achievement in charlie:
        if achievement not in alice and achievement not in bob:
            rare.add(achievement)
    return rare


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {"first_kill",
                       "level_10",
                       "treasure_hunter",
                       "speed_demon"}
    bob: set[str] = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie: set[str] = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===\n")

    union: set[str] = alice.union(bob, charlie)
    print(f"All unique achievements: {union}")
    print(f"Total unique achievements: {len(union)}\n")

    print(f"Common to all players: {alice.intersection(bob, charlie)}")
    print(f"Rare achievements (1 player): \
{rare_achievement(alice, bob, charlie)}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")
