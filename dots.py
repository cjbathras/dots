import sys

import pygame
from pygame.locals import *

from board import Board
import constants as c
from config import Config


def main():
    pygame.display.init()
    config = Config(rows=4, columns=4, cell_size=150, dot_radius=6)

    board = Board()

    DISPLAY = pygame.display.set_mode(
        (config.columns * config.cell_size + c.GUTTER_WIDTH * 2,
        config.rows * config.cell_size + c.GUTTER_WIDTH * 2 + c.TOP_OFFSET))
    DISPLAY.fill(c.WHITE)

    for row in board.cells:
        for cell in row:
            cell.draw()

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                row = (y - c.GUTTER_WIDTH) // config.cell_size
                col = (x - c.GUTTER_WIDTH) // config.cell_size
                if row < 0:
                    row = 0
                elif row >= config.rows:
                    row = config.rows - 1

                if col < 0:
                    col = 0
                elif col >= config.columns:
                    col = config.columns - 1

                cell = board.get_cell(row, col)
                clicked_edge = cell.get_clicked_edge(x, y)
                if clicked_edge:
                    cell.set_clicked_edge(clicked_edge)
                    board.set_adjacent_clicked_edge(row, col, clicked_edge)

                board.redraw_dirty_cells()

        pygame.display.update()

if __name__ == '__main__':
    main()
