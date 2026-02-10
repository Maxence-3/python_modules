def record_spell(str, ingredients):
    from alchemy.grimoire import validate_ingredients
    is_valid = validate_ingredients(ingredients)

    if "INVALID" in is_valid:
        return f"Spell rejected: {str} {is_valid}"
    else:
        return f"Spell recorded: {str} {is_valid}"