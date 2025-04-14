class Car:
    def move(self):
        print("Driving on the road 🚗")

class Plane:
    def move(self):
        print("Flying in the sky ✈️")

class Boat:
    def move(self):
        print("Sailing on the water 🚢")

# Function that uses polymorphism
def start_journey(vehicle):
    vehicle.move()

# Create vehicle objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Call the same function with different vehicle types
start_journey(my_car)
start_journey(my_plane)
start_journey(my_boat)
