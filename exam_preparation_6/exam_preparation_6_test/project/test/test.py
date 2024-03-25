from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.tennis_player = TennisPlayer(
            "Rosen",
            20,
            50
        )

    def test_correct_init(self):
        self.assertEqual("Rosen", self.tennis_player.name)
        self.assertEqual(20, self.tennis_player.age)
        self.assertEqual(50, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_setter_error_right(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "ro"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_error_right(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 16

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_method_is_right_if_tournament_name_is_not_int_the_wins_list(self):
        expected_wins_list = ["Varna", "Sofia"]

        self.tennis_player.add_new_win("Varna")
        self.tennis_player.add_new_win("Sofia")

        self.assertEqual(expected_wins_list, self.tennis_player.wins)

    def test_add_new_win_method_if_tournament_is_already_in_wins_list(self):
        self.tennis_player.wins = []

        self.tennis_player.add_new_win("Varna")
        result = self.tennis_player.add_new_win("Varna")

        self.assertEqual(f"Varna has been already added to the list of wins!", str(result))

    def test_if_lower_than_method_is_working_for_other_player(self):
        new_player = TennisPlayer(
            "Ivan",
            23,
            60
        )

        result = self.tennis_player.points < new_player.points
        self.assertTrue(result)
        self.assertEqual('Ivan is a top seeded player and he/she is better than Rosen',
                         self.tennis_player.__lt__(new_player))

    def test_if_the_lower_method_is_working_for_our_player(self):
        new_player = TennisPlayer(
            "Ivan",
            23,
            40
        )

        result = new_player.points < self.tennis_player.points
        self.assertTrue(result)
        self.assertEqual('Rosen is a better player than Ivan',
                         self.tennis_player.__lt__(new_player))

    def test_if_the_string_method_representation_is_right(self):
        self.tennis_player.wins = ["Sofia", "Varna"]
        self.assertEqual(f"Tennis Player: Rosen\n"
                         f"Age: 20\n"
                         f"Points: 50.0\n"
                         f"Tournaments won: Sofia, Varna", str(self.tennis_player))


if __name__ == "__main__":
    main()
