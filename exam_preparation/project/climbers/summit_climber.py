from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    MIN_STRENGTH_TO_CLIMB = 75
    REDUCE_IF_ADVANCED = 30 * 1.3
    REDUCE_IF_EXTREME = 30 * 2.5
    
    def __init__(self, name):
        super(SummitClimber, self).__init__(name, 150)
    
    def can_climb(self):
        return self.strength >= self.MIN_STRENGTH_TO_CLIMB

    def climb(self, peak: BasePeak):
        if peak.calculate_difficulty_level() == "Advanced":
            self.strength -= self.REDUCE_IF_ADVANCED

        elif peak.calculate_difficulty_level() == "Extreme":
            self.strength -= self.REDUCE_IF_EXTREME

        self.conquered_peaks.append(peak.name)

