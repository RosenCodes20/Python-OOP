from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(
            100,
            200
        )

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method_working_correctly_expecting_an_error_if_fuel_gets_lower_than_needed(self):
        self.vehicle.fuel = 50
        expected_fuel = 37.5
        self.vehicle.drive(10)

        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_drive_method_with_error_and_output_correctly_showed(self):
        self.vehicle.fuel = 50

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_method_working_correctly_expecting_an_error_if_the_capacity_is_over(self):
        self.vehicle.fuel = 50

        self.vehicle.refuel(30)

        self.assertEqual(80, self.vehicle.fuel)

    def test_refuel_method_with_error_and_if_it_is_raised_right(self):
        self.vehicle.fuel = 50

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(70)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_if_string_method_representation_is_good(self):
        expected_string = "The vehicle has 200 " \
               f"horse power with 100 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected_string, str(self.vehicle))


if __name__ == "__main__":
    main()