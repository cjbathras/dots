from __init__ import *
from config import Config
from player import Player


class Game:
    def __init__(self, players: list[Player]):
        super().__init__()
        self.cfg = Config()
        self._players = players
        self._player_ptr = 0
        self._scores = {p: 0 for p in self._players}
        self._tgt_total = self.cfg.ROWS * self.cfg.COLS
        self._total = 0
        self._is_over = False

    @property
    def is_over(self) -> bool:
        return self._is_over

    @property
    def players(self) -> list[Player]:
        return self._players

    def next_player(self) -> Player:
        self._player_ptr = (self._player_ptr + 1) % len(self._players)
        return self.current_player()

    def current_player(self) -> Player:
        return self._players[self._player_ptr]

    def increment_score(self, player: Player) -> None:
        self._scores[player] += 1
        self._total += 1

    def get_score(self, player: Player) -> int:
        return self._scores[player]

    def check_for_winner(self) -> list[Player]:
        if self._total == self._tgt_total:
            self._is_over = True
            # Create a reverse sorted list of (player, score) tuples
            sorted_scores = [(k, v) for k, v \
                in reversed(
                    sorted(self._scores.items(), key=lambda item: item[1]))]
            # Scan sorted_scores to see if there is a tie
            # That's why we're returning a list because there could be more
            # than one winner
            return [p for p, s in sorted_scores if s == sorted_scores[0][1]]
        else:
            return None

    def __str__(self) -> str:
        score_items = self._scores.items()
        return f'{type(self).__name__}: Target={self._tgt_total} ' \
            f'Score=({", ".join([str(p)+"="+str(s) for p, s in score_items])})'

    def __repr__(self) -> str:
        return str(self)
