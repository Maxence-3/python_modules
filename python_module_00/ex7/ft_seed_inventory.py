def ft_seed_inventor(seed, quantity, type):
    if (type == "packets"):
        print(f"{seed.title()} seeds: {quantity} {type} available")
    elif (type == "grams"):
        print(f"{seed.title()} seeds: {quantity} {type} total")
    elif (type == "area"):
        print(f"{seed.title()} seeds: covers {quantity} square meters")


if __name__ == "__main__":
    ft_seed_inventor("tomato", 15, "packets")
    ft_seed_inventor("carrot", 8, "grams")
    ft_seed_inventor("lettuce", 12, "area")
