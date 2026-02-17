def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire import validate_ingredients
    is_valid = validate_ingredients(ingredients)

    if "INVALID" in is_valid:
        return f"Spell rejected: {spell_name} {is_valid}"
    else:
        return f"Spell recorded: {spell_name} {is_valid}"
