'''Classes: Blueprints for objects.
Objects: Instances of a class.
Attributes and Methods: Define object properties and behaviors.
OOP Principles: Encapsulation, Inheritance, Polymorphism, and Abstraction.
Special Methods: __init__, __str__, __repr__, etc., provide custom behavior.'''

# Defining a class named `car` (Classes are blueprints for creating objects)

class Person:
    pass  # A placeholder indicating no implementation yet, This basically allows a blank class without errors

class car:
    # The constructor method (__init__) initializes object attributes when an instance of the class is created
    def __init__(self, hp, model, brand, year):
        self.horsepower = hp  # Assigning `hp` to the instance attribute `horsepower`
        self.model = model   
        self.brand = brand    
        self.year = year      

    # Defining a method to return information about the car
    # This is an instance method because it works on an instance of the class
    
    def info(self):
        return f'{self.horsepower} HP {self.model} {self.brand} {self.year}'
        # Returns a formatted string with the car's details

# Creating instances (objects) of the `car` class
car1 = car(855, "AudiGT", "AUDI", 2024)  
car2 = car(478, "AudiGT", "AUDI", 2025)  

# Printing information about the cars using the `info()` method
print(car1.info()) 
print(car2.info())  

#Inheritance: A class can copy attributes and methods from another class.

class ElectricCar(car):  # ElectricCar inherits from car
    def __init__(self, hp, model, brand, year, battery_size):
        super().__init__(hp, model, brand, year)  # Call parent class's constructor
        self.battery_size = battery_size  # New attribute for ElectricCar

    def battery_info(self):
        return f"Battery size: {self.battery_size} kWh"

ecar = ElectricCar(500, "Model S", "Tesla", 2024, 100)
print(ecar.info())  # Inherited method
print(ecar.battery_info())  # Specific to ElectricCar


#polymorphism : The ability to redefine methods in child classes.

class Car:
    def drive(self):
        return "The car is driving."

class SportsCar(Car):
    def drive(self):
        return "The sports car is driving at high speed!"

car = Car()
sports_car = SportsCar()
print(car.drive())  # Output: The car is driving. this is the parent class 
print(sports_car.drive())  # Output: The sports car is driving at high speed! we have copied the method from the parent class 


#ABSTRACION: Hiding unnecessary implementation details from the users
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def start_engine(self):
        pass  # No implementation

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

my_car = Car()
print(my_car.start_engine())  # Output: Car engine started.


#CLASS METHODS: -- Methods that operate on the class rather than an instance.
class Car:
    total_cars = 0  # Class attribute

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def car_count(cls):
        return f"Total cars created: {cls.total_cars}"

car1 = Car()
car2 = Car()
print(Car.car_count())  # Output: Total cars created: 2

