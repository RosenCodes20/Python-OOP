from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TIME_TO_CATCH_FISH = 90

    def __init__(self, name, points):
        super(PredatoryFish, self).__init__(name, points, self.TIME_TO_CATCH_FISH)

    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"