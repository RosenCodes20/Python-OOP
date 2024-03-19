from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450

    def __init__(self, brand, model, license_plate_number):
        super(PassengerCar, self).__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage):
        percentage_to_decrease = (mileage / self.max_mileage) * 100
        self.battery_level -= round(percentage_to_decrease)
