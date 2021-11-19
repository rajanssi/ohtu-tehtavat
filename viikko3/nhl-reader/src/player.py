class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']

    def __str__(self):
        return f"{self.name:30}" + f"{self.team:4}" + f"{str(self.goals):2}" + " + " f"{str(self.assists):2}" + " = " + f"{str(self.goals + self.assists):3}"