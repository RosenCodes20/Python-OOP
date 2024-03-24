from unittest import TestCase, main

from CarManager.car_manager import Car


class CarManagerTest(TestCase):
    def setUp(self) -> None:
        self.car = Car(
            "BMW",
            "X6",
            30,
            60
        )

    def test_correct_init(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("X6", self.car.model)
        self.assertEqual(30, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_if_the_make_type_error_is_valid_if_it_is_null_or_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_the_model_type_error_is_valid_if_it_is_null_or_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_the_fuel_consumption_error_is_valid_if_it_is_bellow_or_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_if_the_fuel_capacity_error_is_valid_if_its_value_gets_bellow_or_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_if_the_fuel_amount_error_is_right_if_its_value_gets_bellow_or_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -15

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_if_the_refuel_of_the_car_is_right_expecting_an_error_if_its_fuel_gets_bellow_or_equal_to_zero(self):
        expected_fuel = 60

        self.car.refuel(61)

        self.assertEqual(expected_fuel, self.car.fuel_amount)

    def test_if_the_fuel_error_is_right_if_its_value_drops_bellow_or_gets_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-30)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_if_the_car_is_driving_fine_expecting_an_error_if_needed_distance_gets_higher_than_the_fuel_amount_value(self):
        self.car.fuel_amount = 40

        self.car.drive(100)

        self.assertEqual(10, self.car.fuel_amount)

    def test_if_the_raised_error_is_right_for_drive_func_and_if_the_string_representing_it_is_also_right_for_it(self):
        self.car.fuel_amount = 0

        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
