from mammal.project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal(
            "Rosen",
            "dog",
            "bark"
        )

    def test_correct_init(self):
        self.assertEqual("Rosen", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("bark", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method_correct_output(self):
        result = self.mammal.make_sound()

        self.assertEqual(f"Rosen makes bark", str(result))

    def test_info_method_output_works_correctly(self):
        result = self.mammal.info()

        self.assertEqual("Rosen is of type dog", str(result))


if __name__ == "__main__":
    main()