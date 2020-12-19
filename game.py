from __init__ import *
from config import Config


class Game:
    def __init__(self, *players):
        super().__init__()
        self.cfg = Config()
        self.players = list(players)
        self.player_ptr = 0
        self.scores = {p: 0 for p in self.players}
        self.tgt_total = self.cfg.ROWS * self.cfg.COLS
        self.total = 0

    def next_player(self):
        self.player_ptr = (self.player_ptr + 1) % len(self.players)
        return self.current_player()

    def current_player(self):
        return self.players[self.player_ptr]

    def increment_score(self, player):
        self.scores[player] += 1
        self.total += 1

    def get_score(self, player):
        return self.scores[player]

    def check_for_winner(self):
        if self.total == self.tgt_total:
            # Create a reverse sorted list of (player, score) tuples
            sorted_scores = [(k, v) for k, v in reversed(sorted(self.scores.items(), key=lambda item: item[1]))]
            # Scan sorted_scores to see if there is a tie
            # That's why we're returning a list because there could be more than one winner
            return [p for p, s in sorted_scores if s == sorted_scores[0][1]]
        else:
            return None
