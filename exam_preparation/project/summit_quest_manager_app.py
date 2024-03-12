from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAKS = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: list = []
        self.peaks: list = []

    def register_climber(self, climber_type, climber_name):
        for climber in self.climbers:
            if climber.name == climber_name:
                return f"{climber_name} has been already registered."

        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        new_climber = self.VALID_CLIMBERS[climber_type](climber_name)
        self.climbers.append(new_climber)

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type, peak_name, peak_elevation):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."

        new_climber = self.VALID_PEAKS[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_climber)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, c_name, p_name, gear):
        climber = next(filter(lambda c: c.name == c_name, self.climbers))
        peak = next(filter(lambda p: p.name == p_name, self.peaks))

        rec_gear = peak.get_recommended_gear()
        missing = sorted(set(rec_gear) - set(gear))

        if missing:
            climber.is_prepared = False
            return f"{c_name} is not prepared to climb {p_name}." \
                   f" Missing gear: {', '.join(map(str, missing))}."

        return f"{c_name} is prepared to climb {p_name}."

    def perform_climbing(self, climber_name, peak_name):
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))

        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))

        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} " \
                   f"whose difficulty level is {peak.calculate_difficulty_level()}."

        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        print([p.name for p in self.peaks])
        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks], key=lambda x: (-len(x.conquered_peaks), x.name))
        peaks_info = "\n".join([str(c) for c in sorted_climbers])
        return f"Total climbed peaks: {len(self.peaks)}\n**Climber's statistics:**\n{peaks_info}"
