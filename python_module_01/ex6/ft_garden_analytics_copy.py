class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def award_points(self):
        self.prize_points += 1


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def calculate_score(self):
        total = 0
        for plant in self.plants:
            total += plant.height
            if isinstance(plant, PrizeFlower):
                total += plant.prize_points
        return total


class GardenManager:
    total_gardens = 0

    def __init__(self):
        self.gardens = []

    def add_garden(self, garden):
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls):
        return cls()

    @staticmethod
    def validate_height(height):
        return height > 0

    class GardenStats:
        @staticmethod
        def print_report(garden):
            print(f"=== {garden.owner}'s Garden Report ===")
            print("Plants in garden:")

            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    blooming_status = (
                        "blooming" if plant.is_blooming else "not blooming"
                    )
                    print(
                        f"- {plant.name}: {plant.height}cm, \
{plant.flower_color} flowers ({blooming_status}), \
Prize points: {plant.prize_points}"
                    )
                elif isinstance(plant, FloweringPlant):
                    blooming_status = (
                        "blooming" if plant.is_blooming else "not blooming"
                    )
                    print(
                        f"- {plant.name}: {plant.height}cm, {plant.flower_color} flowers ({blooming_status})"
                    )
                else:
                    print(f"- {plant.name}: {plant.height}cm")

            total_plants = len(garden.plants)
            total_growth = sum(
                plant.height - plant.initial_height for plant in garden.plants
            )

            regular_count = 0
            flowering_count = 0
            prize_count = 0

            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize_count += 1
                elif isinstance(plant, FloweringPlant):
                    flowering_count += 1
                else:
                    regular_count += 1

            print(
                f"\nPlants added: {total_plants}, Total growth: {total_growth}cm"
            )
            print(
                f"Plant types: {regular_count} regular, {flowering_count} flowering, {prize_count} prize flowers\n"
            )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = Garden("Alice")
    alice_garden.add_plant(Plant("Oak Tree", 100))
    rose = FloweringPlant("Rose", 25, "red")
    rose.bloom()
    alice_garden.add_plant(rose)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    sunflower.bloom()
    alice_garden.add_plant(sunflower)

    alice_garden.help_plants_grow()

    print()
    GardenManager.GardenStats.print_report(alice_garden)

    print(f"Height validation test: {GardenManager.validate_height(100)}")

    bob_garden = Garden("Bob")
    bob_garden.add_plant(Plant("Maple", 80))

    manager = GardenManager.create_garden_network()
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    alice_score = alice_garden.calculate_score()
    bob_score = bob_garden.calculate_score()
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    print(f"Total gardens managed: {GardenManager.total_gardens}")
