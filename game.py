# Copyright 2021 Curt Bathras
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from config import Config
from player import Player


class Game:
    def __init__(self, players: list[Player]):
        super().__init__()
        self._cfg = Config()
        self._players = players
        self._player_ptr = 0
        self._scores = {p: 0 for p in self._players}
        self._tgt_total = self._cfg.CELL_ROWS * self._cfg.CELL_COLS
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
