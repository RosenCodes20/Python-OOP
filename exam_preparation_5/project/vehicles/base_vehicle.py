from abc import ABC, abstractmethod


class BaseVehicle(ABC):

    def __init__(self, brand, model, license_plate_number, max_mileage):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False
        
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, value):
        if value == "" or not value.strip():
            raise ValueError("Brand cannot be empty!")
        
        self.__brand = value
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if value == "" or not value.strip():
            raise ValueError("Model cannot be empty!")

        self.__model = value

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        if value == "" or not value.strip():
            raise ValueError("License plate number is required!")

        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        if not self.is_damaged:
            self.is_damaged = True

        elif self.is_damaged:
            self.is_damaged = False

    def __str__(self):
        status = "OK" if not self.is_damaged else "Damaged"
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: {status}"
