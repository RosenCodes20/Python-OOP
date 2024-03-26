from project.hero import Hero

from unittest import TestCase, main


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero(
            "Rosen",
            1,
            100,
            200
        )

        self.enemy_hero = Hero(
            "Ivelin",
            1,
            100,
            50
        )

    def test_correct_init(self):
        self.assertEqual("Rosen", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(200, self.hero.damage)

    def test_battle_if_the_end_of_the_game_is_draw(self):
        self.hero.damage = 100
        self.enemy_hero.damage = 100

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("Draw", str(result))
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy_hero.health)

    def test_battle_method_working_right_expecting_three_errors_our_player_to_win(self):
        hero_expected_health = 55
        hero_expected_level = 2
        hero_expected_damage = 205
        enemy_expected_health = -100
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(hero_expected_level, self.hero.level)
        self.assertEqual(hero_expected_health, self.hero.health)
        self.assertEqual(hero_expected_damage, self.hero.damage)
        self.assertEqual("You win", str(result))
        self.assertEqual(enemy_expected_health, self.enemy_hero.health)

    def test_battle_method_working_for_enemy_player_expecting_three_errors(self):
        self.enemy_hero.damage = 200
        self.hero.damage = 50

        enemy_hero_expected_health = 55
        enemy_hero_expected_level = 2
        enemy_hero_expected_damage = 205
        hero_expected_health = -100
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(enemy_hero_expected_level, self.enemy_hero.level)
        self.assertEqual(enemy_hero_expected_health, self.enemy_hero.health)
        self.assertEqual(enemy_hero_expected_damage, self.enemy_hero.damage)
        self.assertEqual("You lose", str(result))
        self.assertEqual(hero_expected_health, self.hero.health)

    def test_battle_method_with_error_having_equal_usernames(self):
        self.enemy_hero.username = "Rosen"
        with self.assertRaises(Exception) as ex:
             self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_if_our_health_is_lower_than_zero_with_error(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_correct_error_raised_if_enemy_health_gets_lower_than_zero(self):
        self.enemy_hero.health = -1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight Ivelin. He needs to rest", str(ve.exception))

    def test_str_method_representation_working_also_right(self):
        expected_string = f"Hero Rosen: 1 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 200\n"

        self.assertEqual(expected_string, str(self.hero))


if __name__ == "__main__":
    main()