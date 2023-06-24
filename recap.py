from hashlib import new


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        #FUel capacity
        self.fuel_Capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity"""
        self.fuel_level = self.fuel_Capacity
        print("Fuel tank is full")

    def drive(self):
        print("The car is moving")
    
    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_Capacity:
            self.fuel_level = new_level
            print(f"new fuel level is{self.fuel_level}")
        else:
            print("The tank cant hold that much")

my_car = Car('audi', 'a4', 2016)


print(my_car.make)
print(my_car.model)
print(my_car.year)

#Calling  methods
my_car.fill_tank()
my_car.drive()

#Creating multiple objects
my_old_car = Car('subaru', 'outback', 2015)
my_truck = Car("Totota", "Hilux", 1994)
my_truck.make = 'Ford'
my_truck.model = 'Ranger'
my_truck.year = 2021

print(f"Details about my car {my_truck.make}, {my_truck.model}, {my_truck.year}")
my_truck.fill_tank()
my_truck.drive()
my_truck.update_fuel_level(8)

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery_size = 75
        self.charge_level = 0

    def charge(self):
        self.charge_level = 100
        print("FUlly charged")
    
    #Method overriding 
    def fill_tank(self):
        print("THe car does not have a  fuel tanlk")

my_tesla = ElectricCar('tesla', 'model s', 2021)
my_tesla.charge()
my_tesla.drive()
my_tesla.fill_tank()