from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    MIN_STRENGTH_TO_CLIMB = 100
    REDUCE_STRENGTH_EXTREME = 20 * 2
    REDUCE_STRENGTH_ADVANCED = 20 * 1.5

    def __init__(self, name):
        super(ArcticClimber, self).__init__(name, 200)

    def can_climb(self):
        return self.strength >= self.MIN_STRENGTH_TO_CLIMB

    def climb(self, peak: BasePeak):
        if peak.calculate_difficulty_level() == "Extreme":
            self.strength -= self.REDUCE_STRENGTH_EXTREME

        elif peak.calculate_difficulty_level() == "Advanced":
            self.strength -= self.REDUCE_STRENGTH_ADVANCED

        self.conquered_peaks.append(peak.name)



