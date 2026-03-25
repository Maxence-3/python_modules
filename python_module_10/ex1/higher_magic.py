def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditional(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list) -> callable:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heal {target}"

    def fireball_damage(target):
        return 10

    def is_enemy(target):
        return target in ["Dragon", "Orc", "Troll"]

    def ice_bolt(target):
        return f"Ice Bolt strikes {target}"

    def lightning(target):
        return f"Lightning zaps {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball_damage, 3)
    original = fireball_damage("Dragon")
    amplified = mega_fireball("Dragon")
    print(f"Original: {original}, Amplified: {amplified}")
