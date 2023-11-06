#classes practice

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #default value 
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

#create a variable attached to an object eg, car1, car2 etc        
car1 = Car('audi', 'a4', 2016)

#attach method to variable
print(car1.get_descriptive_name())
print(car1.read_odometer())
print(car1.fill_gas_tank())
print(car1.increment_odometer(100))

print("-----------------------------------------------------------------------\n")

class Hero():
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f"{self.name} is attacking with {self.power} power")
    def defend(self):
        print(f"{self.name} is defending with {self.power} power")
        
hero1 = Hero("Spiderman", 100)
hero1.attack()