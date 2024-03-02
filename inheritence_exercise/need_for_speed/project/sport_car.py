from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, hp):
        super().__init__(fuel, hp)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION