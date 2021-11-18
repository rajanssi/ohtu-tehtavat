import requests
from player import Player
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    nationality = "FIN"
    print("Players from", nationality, datetime.now())

    players = []

    for player_dict in response:
        if player_dict['nationality'] == nationality:
            player = Player(player_dict)
            players.append(player)

    
    print()

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
