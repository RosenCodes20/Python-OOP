from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180

    def __init__(self, brand, model, license_plate_number):
        super(CargoVan, self).__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage):
        self.battery_level -= 5
        percentage_to_decrease = (mileage / self.max_mileage) * 100
        self.battery_level -= round(percentage_to_decrease)
