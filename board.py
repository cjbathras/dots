import random

import pygame

from cell import Cell
import constants as c
from config import Config


class Board:
    def __init__(self):
        super().__init__()
        self._config = Config()
        self.cells = [] # n x n array
        self.dirty_cells = [] # list of tuples containing indexes of cells needing redraw

        for row in range(0, self._config.rows):
            tmp = []
            for column in range(0, self._config.columns):
                cell = Cell(pygame.Rect(column * self._config.cell_size + c.GUTTER_LEFT,
                                        row * self._config.cell_size + c.GUTTER_TOP,
                                        self._config.cell_size,
                                        self._config.cell_size),
                            row,
                            column,
                            c.WHITE)
                tmp.append(cell)

            self.cells.append(tmp)

    def handle_selection(self, x, y, player):
        row, col = self.get_row_col_from_pos((x, y))

        cell = self.get_cell(row, col)
        clicked_edge = cell.get_clicked_edge(x, y)
        if clicked_edge:
            cell.set_clicked_edge(clicked_edge, player)
            self.set_adjacent_clicked_edge(row, col, clicked_edge, player)

    def get_row_col_from_pos(self, pos):
        x, y = pos
        row = (y - c.GUTTER_TOP) // self._config.cell_size
        col = (x - c.GUTTER_LEFT) // self._config.cell_size
        if row < 0:
            row = 0
        elif row >= self._config.rows:
            row = self._config.rows - 1

        if col < 0:
            col = 0
        elif col >= self._config.columns:
            col = self._config.columns - 1

        return row, col

    def get_cell(self, row, col):
        return self.cells[row][col]

    def set_adjacent_clicked_edge(self, row, col, edge, player):
        # Set the edge in the adjacent cell to selected
        if edge == c.TOP:
            if row > 0:
                self.cells[row - 1][col].set_clicked_edge(c.BOTTOM, player)

        elif edge == c.BOTTOM:
            if row < self._config.rows - 1:
                self.cells[row + 1][col].set_clicked_edge(c.TOP, player)

        elif edge == c.LEFT:
            if col > 0:
                self.cells[row][col - 1].set_clicked_edge(c.RIGHT, player)

        elif edge == c.RIGHT:
            if col < self._config.columns - 1:
                self.cells[row][col + 1].set_clicked_edge(c.LEFT, player)

    def redraw_dirty_cells(self):
        for row in self.cells:
            for cell in row:
                if cell.is_dirty:
                    cell.draw()

    def __repr__(self):
        return f'Board {len(self.cells[0])}x{len(self.cells)}'
