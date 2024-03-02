from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, hp):
        super().__init__(fuel, hp)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION