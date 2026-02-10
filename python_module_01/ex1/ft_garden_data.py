class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_data(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    Rose = Plant(name="Rose", height=25, age=30)
    Sunflower = Plant(name="Sunflower", height=80, age=45)
    Cactus = Plant(name="Cactus", height=15, age=120)

    print("=== Garden Plant Registry ===")
    Rose.print_data()
    Sunflower.print_data()
    Cactus.print_data()
