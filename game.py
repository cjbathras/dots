class Game:
    def __init__(self, *players):
        super().__init__()
        self.players = [p for p in players]
        self.player_ptr = 0
        self.scores = {p:0 for p in players}

    def next_player(self):
        self.player_ptr = (self.player_ptr + 1) % len(self.players)
        return self.current_player()

    def current_player(self):
        return self.players[self.player_ptr]

    def increment_score(self, player):
        self.scores[player] = self.scores[player] + 1
