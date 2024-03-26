from project.trip import Trip

from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self) -> None:
        self.trip = Trip(
            500,
            15,
            False
        )

    def test_correct_init(self):
        self.assertEqual(500, self.trip.budget)
        self.assertEqual(15, self.trip.travelers)
        self.assertFalse(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}, Trip.DESTINATION_PRICES_PER_PERSON)

    def test_travelers_setter_right_raised_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_setter_right_without_expecting_an_error(self):
        self.trip.travelers = 1
        self.trip.is_family = True

        self.assertFalse(self.trip.is_family)

    def test_another_is_family_setter_correct_output(self):
        self.trip.is_family = True
        self.trip.travelers = 5

        self.assertTrue(self.trip.is_family)

    def test_correct_output_for_booking_a_trip_method(self):
        expected_booked_trips_dict = {"Bulgaria": 1350}
        expected_budget = 650
        self.trip.budget = 2000
        self.trip.travelers = 3
        self.trip.is_family = True
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual(expected_booked_trips_dict, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(expected_budget, self.trip.budget)
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 650.00', str(result))

    def test_if_destination_in_the_booking_trip_method_is_not_in_the_dict(self):
        result = self.trip.book_a_trip("France")

        self.assertEqual('This destination is not in our offers, please choose a new one!', str(result))

    def test_if_the_budget_is_lower_than_the_required_price_in_the_book_a_trip_method(self):
        self.trip.travelers = 3
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual('Your budget is not enough!', str(result))

    def test_if_the_booking_status_output_is_right(self):
        self.trip.travelers = 1
        self.trip.is_family = False
        self.trip.budget = 10_000
        self.trip.book_a_trip("Bulgaria")
        self.trip.book_a_trip("Australia")
        expected_result = "Booked Destination: Australia\nPaid Amount: 5700.00\n" \
                          "Booked Destination: Bulgaria\nPaid Amount: 500.00\n" \
                          "Number of Travelers: 1\nBudget Left: 3800.00"

        result = self.trip.booking_status()

        self.assertEqual(expected_result, str(result))

    def test_if_the_booking_status_method_output_is_right_if_the_dict_is_empty(self):
        self.trip.booked_destinations_paid_amounts = {}

        result = self.trip.booking_status()

        self.assertEqual('No bookings yet. Budget: 500.00', str(result))

        
if __name__ == "__main__":
    main()