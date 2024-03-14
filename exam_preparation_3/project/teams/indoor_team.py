from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    BUDGET = 500
    ADVANTAGE = 145

    def __init__(self, name, country, advantage):
        super(IndoorTeam, self).__init__(name, country, advantage, self.BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE
        self.wins += 1