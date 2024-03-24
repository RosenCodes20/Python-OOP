from unittest import TestCase, main

from TestWorker.test_worker_file import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker("Rosen", 300, 60)

    def test_correct_init(self):
        self.assertEqual("Rosen", self.worker.name)
        self.assertEqual(300, self.worker.salary)
        self.assertEqual(60, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_worker_is_working_except_error_if_energy_gets_bellow_zero(self):
        expected_money = self.worker.salary * 3
        expected_energy = 57

        self.worker.work()
        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_if_the_error_name_is_right_and_if_the_money_gets_bellow_zero(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_the_worker_is_resting_fine_by_adding_one_to_his_energy_and_getting_him_rest_good(self):
        expected_energy = 61
        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_if_the_info_for_the_worker_is_wright_by_getting_his_name_and_money(self):
        expected_result = f"{self.worker.name} has saved {self.worker.money} money."
        self.assertEqual(expected_result, self.worker.get_info())


if __name__ == "__main__":
    main()