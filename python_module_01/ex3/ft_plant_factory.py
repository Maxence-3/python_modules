class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_data(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    plants_infos = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []

    for name, height, age in plants_infos:
        plants.append(Plant(name, height, age))

    i = 0

    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.print_data()
        i += 1

    print(f"\nTotal plants created: {i}")
