from project.toy_store import ToyStore

from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_correct_init(self):
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected_result, self.toy_store.toy_shelf)

    def test_add_toy_correct_way_expect_error(self):
        self.toy_store.toy_shelf = {"A": None}
        expected_result = {"A": "Bear"}
        result = self.toy_store.add_toy("A", "Bear")
        self.assertEqual(expected_result, self.toy_store.toy_shelf)
        self.assertEqual("Toy:Bear placed successfully!", str(result))

    def test_add_toy_incorrect_way_with_error_if_shelf_not_in_dict(self):
        self.toy_store.toy_shelf = {"A": None}

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("B", "Alien")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_incorrect_way_with_error_if_toy_is_already_in_the_shelf(self):
        self.toy_store.toy_shelf = {"A": "Bear"}

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Bear")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_incorrect_way_with_error_if_toy_shelf_is_not_none(self):
        self.toy_store.toy_shelf = {"A": "Bear"}

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Alien")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_remove_toy_correct_way_expecting_errors_if_toy_not_in_dict_and_shelf_is_not_the_same_as_toy_name(self):
        self.toy_store.toy_shelf = {"A": "Bear"}
        expected_result = {"A": None}
        result = self.toy_store.remove_toy("A", "Bear")
        self.assertEqual(expected_result, self.toy_store.toy_shelf)
        self.assertEqual("Remove toy:Bear successfully!", str(result))
        self.assertTrue(self.toy_store.toy_shelf["A"] is None)

    def test_remove_toy_incorrect_way_if_toy_not_in_the_shelf_keys(self):
        self.toy_store.toy_shelf = {"A": "Bear"}

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("B", "Bear")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_incorrect_way_if_toy_name_not_in_that_shelf(self):
        self.toy_store.toy_shelf = {"A": "Bear"}

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Alien")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))


if __name__ == "__main__":
    main()