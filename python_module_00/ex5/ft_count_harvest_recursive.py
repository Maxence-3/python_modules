def ft_count_harvest_recursive(days=0, i=0):
    if (int(days) == 0):
        days = input("Days until harvest: ")
    if (i < int(days)):
        i += 1
        print(f"Day {int(i)}")
        ft_count_harvest_recursive(days, i)
    else:
        print("Harvest time!")

# ft_count_harvest_recursive()
