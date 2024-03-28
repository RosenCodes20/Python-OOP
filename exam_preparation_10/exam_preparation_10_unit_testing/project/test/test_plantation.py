from unittest import TestCase, main

from project.plantation import Plantation


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(
            20
        )

    def test_correct_init(self):
        self.assertEqual(20, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_correct_size_getter_working(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_method_working_right_expecting_an_error(self):
        result = self.plantation.hire_worker("Rosen")
        self.assertEqual(["Rosen"], self.plantation.workers)
        self.assertEqual("Rosen successfully hired.", str(result))

    def test_hire_method_representation_working_right(self):
        self.plantation.workers = ["Rosen"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Rosen")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_len_method_working_right_not_expecting_an_errors(self):
        self.plantation.plants = {"Rosen": ["Tulip", "Sunflower", "Rose"]}
        self.assertEqual(3, len(self.plantation))

    def test_planting_method_working_right_expecting_errors(self):
        self.plantation.hire_worker("Rosen")
        result = self.plantation.planting("Rosen", "Tulip")

        self.assertEqual({"Rosen": ["Tulip"]}, self.plantation.plants)
        self.assertEqual("Rosen planted it's first Tulip.", str(result))

    def test_planting_method_error_if_worker_not_hired(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Rosen", "Tulip")

        self.assertEqual("Worker with name Rosen is not hired!", str(ve.exception))
        self.assertEqual(0, len(self.plantation.plants))

    def test_if_worker_in_dict_keys(self):
        self.plantation.hire_worker("Rosen")
        self.plantation.plants = {"Rosen": ["Tulip"]}

        result = self.plantation.planting("Rosen", "Rose")

        self.assertEqual({"Rosen": ["Tulip", "Rose"]}, self.plantation.plants)
        self.assertEqual("Rosen planted Rose.", str(result))
        self.assertEqual(2, len(self.plantation.plants["Rosen"]))

    def test_planting_method_error_if_len_is_not_right(self):
        self.plantation.size = 1
        self.plantation.hire_worker("Ivo")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivo", "Tulip")
            self.plantation.planting("Ivo", "Tulip")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_method_error_if_len_gets_higher_than_the_size(self):
        self.plantation.size = 2
        self.plantation.plants = {"Rosen": ["Rose"], "Ivan": ["Tulip"]}
        self.plantation.hire_worker("Ivo")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivo", "Tulip")

        self.assertEqual("The plantation is full!", str(ve.exception))
        self.assertEqual(2, len(self.plantation))

    def test_str_method_representation_is_right(self):
        self.plantation.hire_worker("Rosen")
        self.plantation.planting("Rosen", "Tulip")
        expected_result = "Plantation size: 20\n" \
                          "Rosen\n" \
                          "Rosen planted: Tulip"

        self.assertEqual(expected_result, str(self.plantation))

    def test_if_representation_method_working_right(self):
        self.plantation.hire_worker("Rosen")
        self.plantation.hire_worker("Ivelin")
        self.plantation.size = 1

        expected_result = "Size: 1\n" \
                          "Workers: Rosen, Ivelin"

        self.assertEqual(expected_result, repr(self.plantation))


if __name__ == "__main__":
    main()
