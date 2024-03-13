from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type, diver_name):
        for diver in self.divers:
            if diver.name == diver_name:
                return f"{diver_name} is already a participant."

        if diver_type not in self.VALID_DIVERS:
            return f"{diver_type} is not allowed in our competition."

        new_diver = self.VALID_DIVERS[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type, fish_name, points: float):
        for fish in self.fish_list:
            if fish.name == fish_name:
                return f"{fish_name} is already permitted."

        if fish_type not in self.VALID_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."

        new_fish = self.VALID_FISH[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name, fish_name, is_lucky):

        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))

        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_with_health_issue = [d for d in self.divers if d.has_health_issue]
        for diver in divers_with_health_issue:
            diver.has_health_issue = False
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_with_health_issue)}"

    def diver_catch_report(self, diver_name):
        diver = [d for d in self.divers if d.name == diver_name][0]
        fish = [f.fish_details() for f in diver.catch]
        formatted_caught_fish = '\n'.join(map(str, fish))
        if diver:
            return f"**{diver_name} Catch Report**\n{formatted_caught_fish}"

    def competition_statistics(self):
        diver = [d for d in self.divers if not d.has_health_issue]
        sorted_diver = sorted(diver, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        formatted_diver = "\n".join(map(str, sorted_diver))
        return f"**Nautical Catch Challenge Statistics**\n{formatted_diver}"