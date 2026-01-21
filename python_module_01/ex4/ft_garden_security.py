class SecurePlant:
    def __init__(self, name):
        self._name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self._name}")

    def set_height(self, value):
        if value < 0:
            print(f"\nInvalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value):
        if value < 0:
            print(f"\nInvalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def __str__(self):
        return f"\nCurrent plant: {self._name} ({self._height}cm, {self._age} days)"


print("=== Garden Security System ===")
plant = SecurePlant("Rose")
plant.set_height(25)
plant.set_age(30)
plant.set_height(-5)
print(plant)
