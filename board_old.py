import pygame

from __init__ import *
from cell import Cell


class Board:
    def __init__(self):
        super().__init__()
        self.board = [] # ROWS x COLS array

        for r in range(0, ROWS):
            row = []
            for c in range(0, COLS):
                cell = Cell(
                    (c * CELL_WIDTH + GUTTER_LEFT, r * CELL_HEIGHT + GUTTER_TOP),
                    CELL_SIZE,
                    r,
                    c,
                    WHITE
                )
                row.append(cell)
            self.board.append(row)

    def __getitem__(self, pos):
        if isinstance(pos, tuple):
            return self.board[pos[0]][pos[1]]
        else:
            return self.board[pos]

    def get_row_col(self, pos):
        x, y = pos
        row = (y - GUTTER_TOP) // CELL_HEIGHT
        col = (x - GUTTER_LEFT) // CELL_WIDTH

        if row < 0 or row >= ROWS:
            row = None
        if col < 0 or col >= COLS:
            col = None

        if row is None or col is None:
            return None
        else:
            return row, col

    def assign_neighbors(self):
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if r == 0: # top row
                    if c == 0: # first col
                        self.board[r][c].assign_neighbors(top=None, bottom=self.board[r+1][c], left=None, right=self.board[r][c+1])
                    elif c == COLS - 1: # last col
                        self.board[r][c].assign_neighbors(top=None, bottom=self.board[r+1][c], left=self.board[r][c-1], right=None)
                    else: # inner cols
                        self.board[r][c].assign_neighbors(top=None, bottom=self.board[r+1][c], left=self.board[r][c-1], right=self.board[r][c+1])

                elif r == ROWS - 1: # bottom row
                    if c == 0: # first col
                        self.board[r][c].assign_neighbors(top=self.board[r-1][c], bottom=None, left=None, right=self.board[r][c+1])
                    elif c == COLS - 1: # last col
                        self.board[r][c].assign_neighbors(top=self.board[r-1][c], bottom=None, left=self.board[r][c-1], right=None)
                    else: # inner cols
                        self.board[r][c].assign_neighbors(top=self.board[r-1][c], bottom=None, left=self.board[r][c-1], right=self.board[r][c+1])

                else: # inner rows
                    if c == 0: # first col
                        self.board[r][c].assign_neighbors(top=self.board[r-1][c], bottom=self.board[r+1][c], left=None, right=self.board[r][c+1])
                    elif c == COLS - 1: # last col
                        self.board[r][c].assign_neighbors(top=self.board[r-1][c], bottom=self.board[r+1][c], left=self.board[r][c-1], right=None)
                    else: # inner cols
                        self.board[r][c].assign_neighbors(top=self.board[r-1][c], bottom=self.board[r+1][c], left=self.board[r][c-1], right=self.board[r][c+1])

    def draw(self, screen):
        for r in range(0, ROWS):
            for c in range(0, COLS):
                self.board[r][c].draw(screen)

    def __repr__(self):
        return f'Board {len(self.board[0])}x{len(self.board)}'
