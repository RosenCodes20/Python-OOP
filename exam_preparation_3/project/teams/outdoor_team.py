from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    BUDGET = 1000
    TEAM_ADVANTAGE = 115

    def __init__(self, name, country, advantage):
        super(OutdoorTeam, self).__init__(name, country, advantage, self.BUDGET)

    def win(self):
        self.advantage += self.TEAM_ADVANTAGE
        self.wins += 1