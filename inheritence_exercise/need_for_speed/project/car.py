from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, hp):
        super().__init__(fuel, hp)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
