from unittest import TestCase, main

from TestCat.cat_file import Cat


class TestCat(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Roshko")

    def test_correct_init_by_name(self):
        self.assertEqual("Roshko", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_if_cat_has_eaten_good_expect_raise_an_exception_error_if_cat_is_already_fed(self):
        expected_size = 1
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_if_the_raised_exception_is_right_and_if_it_is_an_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_if_the_cat_is_ready_to_go_to_sleep_expect_an_error_if_she_is_not_fed_already(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_if_the_raised_exception_is_right_and_if_the_specific_error_str_is_right(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == "__main__":
    main()