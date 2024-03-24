from unittest import TestCase, main

from List.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.new_list = IntegerList(1, 2, 3, 4.5, "kkk", 6.5)

    def test_correct_init(self):
        self.assertEqual(self.new_list.get_data(), [1, 2, 3])

    def test_adding_new_element_expect_if_the_type_is_not_int_it_will_raise_an_error(self):
        expected_list = self.new_list.get_data().copy() + [4]
        self.new_list.add(4)

        self.assertEqual(expected_list, self.new_list.get_data())

    def test_if_the_raised_error_is_right_and_if_the_string_representation_is_also_good(self):
        with self.assertRaises(ValueError) as ve:
            self.new_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_if_the_removed_index_is_right_expect_an_indexerror_if_the_index_is_not_valid(self):
        expected_number = 2
        self.assertEqual(expected_number, self.new_list.remove_index(1))

    def test_if_the_exception_is_valid_and_if_the_str_raised_is_also_valid(self):
        self.index = 1000

        with self.assertRaises(IndexError) as ex:
            self.new_list.remove_index(self.index)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_the_get_function_of_index_is_valid_expecting_an_error_of_invalid_index(self):
        expected_number = 3

        self.assertEqual(expected_number, self.new_list.get(2))

    def test_if_the_raised_exception_is_valid_and_if_the_represented_string_of_it_is_also_valid(self):
        self.index = 10000

        with self.assertRaises(IndexError) as ex:
            self.new_list.get(self.index)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_the_inserting_function_is_right_expecting_an_error_if_the_index_is_invalid_and_if_the_type_is_not_valid(self):
        expected_list = [1, 4, 2, 3]
        self.new_list.insert(1, 4)

        self.assertEqual(expected_list, self.new_list.get_data())

    def test_if_the_raised_error_is_valid_and_if_the_string_representing_it_is_valid_too(self):
        self.index = 10101010
        with self.assertRaises(IndexError) as ex:
            self.new_list.insert(self.index, 7)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_the_raised_exception_is_right_for_the_invalid_type_of_element_and_if_the_text_representing_it_is_right(self):
        with self.assertRaises(ValueError) as ve:
            self.new_list.insert(1, 5.9)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_if_getting_biggest_number_of_the_list_is_working(self):
        expected_number = 3

        self.assertEqual(expected_number, self.new_list.get_biggest())

    def test_if_the_get_index_function_is_valid(self):
        expected_index = 0

        self.assertEqual(expected_index, self.new_list.get_index(1))


if __name__ == "__main__":
    main()