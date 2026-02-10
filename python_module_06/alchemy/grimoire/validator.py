def validate_ingredients(ingredients):
    valid_ingredients = ["fire", "water", "earth", "air"]
    is_valid = any(ingredient in ingredients.lower() for ingredient in valid_ingredients)
    if is_valid:
        return f"({ingredients} - VALID)"
    else:
        return f"({ingredients} - INVALID)"