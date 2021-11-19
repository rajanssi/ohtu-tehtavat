class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        players_by_nationality = []
        for player in players:
            if player.nationality == nationality:
                players_by_nationality.append(player)

        players_by_nationality.sort(key=lambda player: player.goals+player.assists, reverse=True)
        return players_by_nationality