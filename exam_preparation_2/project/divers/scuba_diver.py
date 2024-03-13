from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540
    REDUCE_OXYGEN = 0.3

    def __init__(self, name):
        super(ScubaDiver, self).__init__(name, self.OXYGEN_LEVEL)

    def miss(self, time_to_catch):
        if self.oxygen_level < round(time_to_catch * self.REDUCE_OXYGEN):
            self.oxygen_level = 0

        else:
            self.oxygen_level -= round(time_to_catch * self.REDUCE_OXYGEN)

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL

