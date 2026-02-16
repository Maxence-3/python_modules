from ex2.EliteCard import EliteCard

if __name__ == "__main__":
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    warrior = EliteCard(
        name="Arcane Warrior",
        cost=6, rarity="Mythic",
        attack_power=5,
        defense_power=3,
        mana_pool=4,
        spell_power=6
    )

    print(f"\nPlaying {warrior.name} (Elite Card):\n")

    print("Combat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}\n")

    print("Magic phase:")
    print("Spell cast: "
          f"{warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")
