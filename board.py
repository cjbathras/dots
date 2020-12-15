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

    def get_cell(self, row, col):
        return self.cells[row][col]

    def set_adjacent_clicked_edge(self, row, col, edge):
        # Set the edge in the adjacent cell to selected
        if edge == c.TOP:
            if row > 0:
                self.cells[row - 1][col].set_clicked_edge(c.BOTTOM)

        elif edge == c.BOTTOM:
            if row < self._config.rows - 1:
                self.cells[row + 1][col].set_clicked_edge(c.TOP)

        elif edge == c.LEFT:
            if col > 0:
                self.cells[row][col - 1].set_clicked_edge(c.RIGHT)

        elif edge == c.RIGHT:
            if col < self._config.columns - 1:
                self.cells[row][col + 1].set_clicked_edge(c.LEFT)

    def redraw_dirty_cells(self):
        for row in self.cells:
            for cell in row:
                if cell.is_dirty:
                    cell.draw()
