from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()

    dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )
    lightning_bolt = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity="common",
        effect_type="Deal 3 damage to target"
    )
    mana_crystal = ArtifactCard(
        name="Mana Crystal",
        cost=2, rarity="rare",
        durability=5,
        effect="Permanent: +1 mana per turn"
    )
    deck.add_card(dragon)
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)

    print(deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")

    print("Drew: Lightning Bolt (Spell)")
    print(f"Play result: {lightning_bolt.play({})}\n")

    print("Drew: Mana Crystal (Artifact)")
    print(f"Play result: {mana_crystal.play({})}\n")

    print("Drew: Fire Dragon (Creature)")
    print(f"Play result: {dragon.play({})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")
