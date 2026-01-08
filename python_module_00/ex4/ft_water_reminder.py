def ft_water_reminder():
    last_watering = input("Days since last watering: ")
    if (int(last_watering) < 3):
        print("Plants are fine")
    else:
        print("Water the plants!")

# ft_water_reminder()
