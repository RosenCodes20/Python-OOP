import re

from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity  # num of teams that tournament can have
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise ValueError("Invalid equipment type!")

        new_equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type, team_name, country, advantage):
        if team_type not in self.VALID_TEAMS:
            raise ValueError("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type, team_name):
        team = [t for t in self.teams if t.name == team_name][0]
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type][-1]

        if team.budget < equipment.price:
            return "Budget is not enough!"

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

        # TODO: Take the last equipment of the given type from the collection. Done

    def remove_team(self, team_name):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))

        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type):
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type]

        for equipments in equipment:
            equipments.increase_price()
        return f"Successfully changed {len(equipment)}pcs of equipment."

    def play(self, team_name1, team_name2):
        team_one = [t for t in self.teams if t.name == team_name1][0]
        team_two = [t for t in self.teams if t.name == team_name2][0]

        if not team_one.__class__.__name__ == team_two.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_one_sum = team_one.advantage + sum([e.protection for e in team_one.equipment])
        team_two_sum = team_two.advantage + sum([e.protection for e in team_two.equipment])

        if team_one_sum > team_two_sum:
            team_one.win()
            return f"The winner is {team_one.name}."

        elif team_one_sum < team_two_sum:
            team_two.win()
            return f"The winner is {team_two.name}."

        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        teams = [t.get_statistics() for t in sorted_teams]
        final_result = "\n".join(map(str, teams))
        return f"Tournament: {self.name}\n" \
               f"Number of Teams: {len(self.teams)}\n" \
               f"Teams:\n{final_result}"
