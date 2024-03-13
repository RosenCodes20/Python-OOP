from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME_TO_CATCH_FISH = 180

    def __init__(self, name, points):
        super(DeepSeaFish, self).__init__(name, points, self.TIME_TO_CATCH_FISH)

    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"