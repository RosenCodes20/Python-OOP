from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.station = RailwayStation(
            "Sofia"
        )

    def test_correct_init(self):
        self.assertEqual("Sofia", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_if_name_setter_error_is_raised_right(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "ros"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_if_adding_new_arrival_ont_the_board_is_right(self):
        expected_arrival_trains_list = deque(["Train Sofia"])

        self.station.new_arrival_on_board("Train Sofia")

        self.assertEqual(expected_arrival_trains_list, self.station.arrival_trains)

    def test_if_the_train_has_arrived_correctly(self):
        self.station.arrival_trains = deque(["Train Sofia", "Train Vratza", "Train Varna"])

        expected_departure_trains = deque(["Train Sofia"])

        result = self.station.train_has_arrived("Train Sofia")

        self.assertEqual(expected_departure_trains, self.station.departure_trains)
        self.assertEqual(f"Train Sofia is on the platform and will leave in 5 minutes.", str(result))
        self.assertTrue(len(self.station.arrival_trains) == 2)

    def test_if_the_arrived_trains_is_not_equal_as_train_info(self):
        self.station.arrival_trains = deque(["Train Sofia", "Train Vratza", "Train Varna"])

        result = self.station.train_has_arrived("Train Mezdra")

        self.assertEqual("There are other trains to arrive before Train Mezdra.", str(result))

    def test_if_the_train_has_left_successfully(self):
        self.station.departure_trains = deque(["Train Sofia", "Train Vratza"])

        result = self.station.train_has_left("Train Sofia")

        self.assertTrue(result)
        self.assertTrue(len(self.station.departure_trains) == 1)
        self.assertTrue("Train Vratza" in self.station.departure_trains)

    def test_if_train_has_not_left_yet(self):
        self.station.departure_trains = deque(["Train Sofia", "Train Vratza"])

        result = self.station.train_has_left("Train Varna")

        self.assertFalse(result)
        self.assertTrue(len(self.station.departure_trains) == 2)
        self.assertTrue("Train Sofia" in self.station.departure_trains)

        
if __name__ == "__main__":
    main()