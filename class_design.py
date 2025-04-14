# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name} and I protect {self.city} using my power: {self.power}!")

    def use_power(self):
        print(f"{self.name} is using {self.power}!")

# Inherited class
class FlyingHero(Superhero):
    def __init__(self, name, power, city, altitude_limit):
        super().__init__(name, power, city)
        self.altitude_limit = altitude_limit

    def fly(self):
        print(f"{self.name} is flying at {self.altitude_limit} feet!")

    # Overriding use_power to show polymorphism
    def use_power(self):
        print(f"{self.name} takes off and uses {self.power} from the sky!")

# Creating objects
hero1 = Superhero("ThunderMan", "Electric Shock", "Metro City")
hero2 = FlyingHero("SkyGirl", "Wind Storm", "Cloud Town", 10000)

# Using methods
hero1.introduce()
hero1.use_power()

print()  # spacing

hero2.introduce()
hero2.fly()
hero2.use_power()
