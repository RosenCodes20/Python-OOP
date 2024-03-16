
from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food: Food):
        if food.__class__.__name__ not in ["Meat"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Owl.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Food):
        if food.__class__.__name__ not in ["Vegetable", "Fruit", "Meat", "Seed"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Hen.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity
