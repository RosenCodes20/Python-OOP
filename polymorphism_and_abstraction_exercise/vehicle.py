from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CAR_AIR_CONDITIONER = 0.9

    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption + Car.CAR_AIR_CONDITIONER) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Car.CAR_AIR_CONDITIONER) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    TRUCK_AIR_CONDITIONER = 1.6
    TRUCK_TINY_HOLE = 0.95

    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption + Truck.TRUCK_AIR_CONDITIONER) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Truck.TRUCK_AIR_CONDITIONER) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.TRUCK_TINY_HOLE


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
