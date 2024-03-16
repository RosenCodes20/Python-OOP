from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size):
        super(Bird, self).__init__(name, weight)
        self.wing_size = wing_size
        self.food_eaten = 0

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super(Mammal, self).__init__(name, weight)
        self.living_region = living_region
        self.food_eaten = 0

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"