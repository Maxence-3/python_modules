def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]
    is_valid = any(i in ingredients.lower() for i in valid_ingredients)
    if is_valid:
        return f"({ingredients} - VALID)"
    else:
        return f"({ingredients} - INVALID)"
