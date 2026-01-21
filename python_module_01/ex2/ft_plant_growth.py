days = 1


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self._age = age

    def age(self):
        self._age += 1

    def grow(self):
        Plant.age(self)
        self.height += 1

    def get_info(self, days):
        print(f"=== Day {days} ===")
        print(f"{self.name}: {self.height}cm, {self._age} days old")


Rose = Plant(name="Rose", height=25, age=30)
Sunflower = Plant(name="Sunflower", height=80, age=45)
Cactus = Plant(name="Cactus", height=15, age=120)

for i in range(7):
    Plant.get_info(Rose, days)
    Plant.grow(Rose)
    days += 1

print(f"Growth this week: +{days - 2}cm")
