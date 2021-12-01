class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {
            player1_name: 0,
            player2_name: 0
        }
        self.scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
            4: "Deuce"
        }
        self.player1_name = player1_name
        self.player2_name = player2_name

    def won_point(self, player_name):
        self.players[player_name] += 1

    def get_score(self):
        if self.players[self.player1_name] == self.players[self.player2_name]:
            return self.equal_score_to_text()
        elif self.players[self.player1_name] >= 4 or self.players[self.player2_name] >= 4:
            return self.advantage_score_to_text()
        else:
            return self.score_to_text(self.player1_name, self.player2_name) 

    def equal_score_to_text(self):
        player1_score = self.players[self.player1_name]
        if player1_score != 4:
            return self.scores[player1_score] + "-All"  
        else:
            return self.scores[4]
    
    def advantage_score_to_text(self):
        score = self.players[self.player1_name] - self.players[self.player2_name] 
        advantage = max(self.players, key=lambda key: self.players[key]) 
        if score <= -2 or score >= 2:
            return "Win for " + advantage
        else:
            return "Advantage " + advantage 

    def score_to_text(self, player1, player2):
        score1 = self.players[player1]
        score2 = self.players[player2]
        return self.scores[score1] + "-" + self.scores[score2]
