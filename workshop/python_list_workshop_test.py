from unittest import TestCase, main
from python_list_workshop import List


class TestList(TestCase):

    def setUp(self) -> None:
        self.my_list = List([1, 2, 3, 4])

    def test_correct_init(self):
        self.assertEqual([1, 2, 3, 4], self.my_list.my_list)

    def test_setter_working_properly_right(self):
        with self.assertRaises(ValueError) as ve:
            self.my_list.my_list = set(self.my_list.my_list)

        self.assertEqual("You can only start with list!!!", str(ve.exception))

    def test_second_setter_working_properly_right(self):
        with self.assertRaises(ValueError) as ve:
            self.my_list.my_list = []

        self.assertEqual("The list cannot be empty!!", str(ve.exception))

    def test_append_method_working_properly_right_not_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3, 4]
        result = self.my_list.append(5)

        self.assertEqual([1, 2, 3, 4, 5], self.my_list.my_list)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_remove_method_working_properly_right_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3]
        result = self.my_list.remove(2)

        self.assertEqual([1, 3], self.my_list.my_list)
        self.assertEqual(None, result)

    def test_remove_method_error_works_properly_right(self):
        self.my_list.my_list = [1, 2, 3]
        with self.assertRaises(Exception) as ex:
            self.my_list.remove(6)

        self.assertEqual("Element is not in our list!!", str(ex.exception))

    def test_get_method_works_properly_right_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3, 4]
        result = self.my_list.get(0)
        self.assertEqual(1, result)

    def test_get_method_error_working_right(self):
        self.my_list.my_list = [1, 2, 3]

        with self.assertRaises(IndexError) as ie:
            self.my_list.get(3)

        self.assertEqual("Invalid index!!!", str(ie.exception))

    def test_extend_method_works_properly_right_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3]
        result = self.my_list.extend([4, 5, 6])

        self.assertEqual([1, 2, 3, 4, 5, 6], self.my_list.my_list)
        self.assertEqual([1, 2, 3, 4, 5, 6], result)

    def test_extend_method_error_working_properly_right(self):
        self.my_list.my_list = [1, 2, 3]

        with self.assertRaises(ValueError) as ve:
            self.my_list.extend(2)

        self.assertEqual("Not right Value!!!!", str(ve.exception))

    def test_insert_method_working_properly_right_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3]

        result = self.my_list.insert(0, 0)

        self.assertEqual([0, 1, 2, 3], self.my_list.my_list)
        self.assertEqual([0, 1, 2, 3], result)

    def test_insert_error_working_right(self):
        self.my_list.my_list = [1, 2, 3]

        with self.assertRaises(IndexError) as ie:
            self.my_list.insert(6, 4)

        self.assertEqual("Index not in right diapason!", str(ie.exception))

    def test_pop_method_work_right_not_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3]
        result = self.my_list.pop()
        self.assertEqual(3, result)

    def test_clear_method_working_right_not_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3]
        result = self.my_list.clear()
        self.assertEqual([], result)

    def test_index_method_work_right_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3]

        result = self.my_list.index(2)

        self.assertEqual(1, result)

    def test_index_method_work_right_with_string_in_the_list(self):
        self.my_list.my_list = ["Rosen", 1, 2, 3]

        result = self.my_list.index("Rosen")

        self.assertEqual(0, result)

    def test_index_method_error_working_right(self):
        self.my_list.my_list = [1, 2, 3]

        with self.assertRaises(ValueError) as ve:
            self.my_list.index(6)

        self.assertEqual("Value is not in the list!", str(ve.exception))

    def test_count_method_error_working_properly_right_expecting_an_error_if_value_not_in_the_list(self):
        self.my_list.my_list = [1, 2, 3, 2, 2]

        result = self.my_list.count(2)

        self.assertEqual(3, result)

    def test_count_method_error_works_right(self):
        self.my_list.my_list = [1, 2, 3]

        with self.assertRaises(ValueError) as ve:
            self.my_list.count(6)

        self.assertEqual("Value not in the list!", str(ve.exception))

    def test_reverse_method_working_right_not_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3]
        result = self.my_list.reverse()

        self.assertEqual([3, 2, 1], self.my_list.my_list)
        self.assertEqual(None, result)

    def test_copy_method_works_right_not_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3]

        result = self.my_list.copy()

        self.assertEqual([1, 2, 3], result)

    def test_sort_method_working_properly_right_not_expecting_an_error(self):
        self.my_list.my_list = [2, 3, 4, 5, 1]

        self.my_list.sort()

        self.assertEqual([1, 2, 3, 4, 5], self.my_list.my_list)

    def test_size_method_working_right_not_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3, 4, 5]

        result = self.my_list.size()

        self.assertEqual(5, result)

    def test_add_first_method_working_right_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3]

        result = self.my_list.add_first(0)

        self.assertEqual([0, 1, 2, 3], self.my_list.my_list)
        self.assertEqual([0, 1, 2, 3], result)

    def test_add_first_method_error_working_right(self):
        self.my_list.my_list = [1, 2, 3]

        with self.assertRaises(ValueError) as ve:
            self.my_list.add_first(4.2)

        self.assertEqual("Our list is formed only by integers!", str(ve.exception))

    def test_dictionize_method_working_right_not_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3, 4]

        result = self.my_list.dictionize()

        self.assertEqual({1: 2, 3: 4}, result)

    def test_dictionize_method_working_properly_right_if_length_is_an_odd_number(self):
        self.my_list.my_list = [1, 2, 3]

        result = self.my_list.dictionize()

        self.assertEqual({1: 2, 3: " "}, result)

    def test_move_method_works_properly_right_expecting_an_error(self):
        self.my_list.my_list = [1, 2, 3, 4]

        result = self.my_list.move(2)

        self.assertEqual([3, 4, 1, 2], self.my_list.my_list)
        self.assertEqual([3, 4, 1, 2], result)

    def test_move_method_error_works_right(self):
        self.my_list.my_list = [1, 2, 3, 4]

        with self.assertRaises(ValueError) as ve:
            self.my_list.move(6)

        self.assertEqual("Please enter a valid amount of numbers", str(ve.exception))

    def test_sum_method_without_a_string(self):
        self.my_list.my_list = [1, 2, 3, 4]

        result = self.my_list.sum()

        self.assertEqual(10, result)

    def test_sum_method_with_a_string(self):
        self.my_list.my_list = [1, 2, 3, "Rosen"]

        result = self.my_list.sum()

        self.assertEqual(11, result)

    def test_overbound_method_without_strings(self):
        self.my_list.my_list = [1, 2, 3, 4, 10]

        result = self.my_list.overbound()

        self.assertEqual(10, result)

    def test_overbound_method_with_strings(self):
        self.my_list.my_list = [1, 2, 3, "Rosen"]

        result = self.my_list.overbound()

        self.assertEqual(5, result)

    def test_underbound_method_without_strings(self):
        self.my_list.my_list = [1, 2, 3, -1]

        result = self.my_list.underbound()

        self.assertEqual(-1, result)

    def test_underbound_method_with_strings(self):
        self.my_list.my_list = ["R", 2, 3, 4]

        result = self.my_list.underbound()

        self.assertEqual(1, result)

if __name__ == "__main__":
    main()