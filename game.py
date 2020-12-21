from __init__ import *
from config import Config
from player import Player


class Game:
    def __init__(self, *players: list[Player]):
        super().__init__()
        self.cfg = Config()
        self.players = list(players)
        self.player_ptr = 0
        self.scores = {p: 0 for p in self.players}
        self.tgt_total = self.cfg.ROWS * self.cfg.COLS
        self.total = 0
        self.is_over = False

    def next_player(self) -> Player:
        self.player_ptr = (self.player_ptr + 1) % len(self.players)
        return self.current_player()

    def current_player(self) -> Player:
        return self.players[self.player_ptr]

    def increment_score(self, player: Player) -> None:
        self.scores[player] += 1
        self.total += 1

    def get_score(self, player: Player) -> int:
        return self.scores[player]

    def check_for_winner(self) -> list[Player]:
        if self.total == self.tgt_total:
            self.is_over = True
            # Create a reverse sorted list of (player, score) tuples
            sorted_scores = [(k, v) for k, v \
                in reversed(
                    sorted(self.scores.items(), key=lambda item: item[1]))]
            # Scan sorted_scores to see if there is a tie
            # That's why we're returning a list because there could be more 
            # than one winner
            return [p for p, s in sorted_scores if s == sorted_scores[0][1]]
        else:
            return None

    def __str__(self) -> str:
        score_items = self.scores.items()
        return f'{type(self).__name__}: Target={self.tgt_total} ' \
            f'Score=({", ".join([str(p)+"="+str(s) for p, s in score_items])})'

    def __repr__(self) -> str:
        return str(self)
