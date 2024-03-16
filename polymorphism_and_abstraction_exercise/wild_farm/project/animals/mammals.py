from abc import ABC

from project.animals.animal import Animal, Mammal
from project.food import Food


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__.__name__ not in ["Vegetable", "Fruit"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Mouse.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ not in ["Meat"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Dog.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food: Food):
        if food.__class__.__name__ not in ["Vegetable", "Meat"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Cat.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ not in ["Meat"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Tiger.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity
