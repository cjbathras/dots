import pygame

from __init__ import *
from shape import Shape


class Board:
    def __init__(self):
        super().__init__()
        self.board = [] # 2*ROWS+1 x 2*COLS+1 array
        self.dots = []
        self.cells = []
        self.edges = []

        for r in range(0, (2 * ROWS + 1)):
            row = []
            for c in range(0, (2 * COLS + 1)):
                if is_even(r) and is_even(c):
                    # dot
                    size = (DOT_DIA, DOT_DIA)
                    origin = (c // 2 * DOT_DIA + c // 2 * CELL_WIDTH + GUTTER_LEFT,
                              r // 2 * DOT_DIA + r // 2 * CELL_HEIGHT + GUTTER_TOP)
                    shape = Shape(origin, size, r, c, DOT, DOT_COLOR)
                    self.dots.append(shape)

                elif is_odd(r) and is_odd(c):
                    # cell
                    size = CELL_SIZE
                    origin = ((c + 1) // 2 * EDGE_THICKNESS + (c - 1) // 2 * CELL_WIDTH + GUTTER_LEFT,
                              (r + 1) // 2 * EDGE_THICKNESS + (r - 1) // 2 * CELL_HEIGHT + GUTTER_TOP)
                    shape = Shape(origin, size, r, c, CELL, CELL_COLOR_DEFAULT)
                    self.cells.append(shape)

                else:
                    # edge
                    if is_even(r):
                        size = (CELL_WIDTH, EDGE_THICKNESS)
                        origin = ((c + 1) // 2 * DOT_DIA + (c - 1) // 2 * CELL_WIDTH + GUTTER_LEFT,
                                  r // 2 * DOT_DIA + r // 2 * CELL_HEIGHT + GUTTER_TOP)
                        shape = Shape(origin, size, r, c, EDGE, EDGE_COLOR_DEFAULT)
                    else:
                        size = (EDGE_THICKNESS, CELL_HEIGHT)
                        origin = (c // 2 * DOT_DIA + c // 2 * CELL_WIDTH + GUTTER_LEFT,
                                  (r + 1) // 2 * DOT_DIA + r // 2 * CELL_HEIGHT + GUTTER_TOP)
                        shape = Shape(origin, size, r, c, EDGE, EDGE_COLOR_DEFAULT)
                    self.edges.append(shape)

                row.append(shape)
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

    def draw(self, screen):
        for r in range(0, len(self.board)):
            for c in range(0, len(self.board[0])):
                self.board[r][c].draw(screen)

    def __repr__(self):
        return f'{type(self).__name__} {len(self.board[0])}x{len(self.board)}'
