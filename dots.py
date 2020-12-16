import sys
import time

import pygame
from pygame.locals import *

from board import Board
import constants as c
from config import Config
from scoreboard import Scoreboard


def main():
    pygame.display.init()
    pygame.display.set_caption('Dots')

    config = Config(rows=4, columns=4, cell_size=150, dot_radius=6)

    board = Board()

    DISPLAY = pygame.display.set_mode(
        (config.columns * config.cell_size + c.GUTTER_LEFT + c.GUTTER_RIGHT,
        config.rows * config.cell_size + c.GUTTER_TOP + c.GUTTER_BOTTOM))
    DISPLAY.fill(c.WHITE)
    width, height = pygame.display.get_window_size()

    scoreboard = Scoreboard(pygame.Rect(20, 20, width - 40, c.GUTTER_TOP - 40), c.GRAY)
    scoreboard.draw()

    for row in board.cells:
        for cell in row:
            cell.draw()

    current_player = c.PLAYER1

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = (mouse_y - c.GUTTER_TOP) // config.cell_size
                col = (mouse_x - c.GUTTER_LEFT) // config.cell_size
                if row < 0:
                    row = 0
                elif row >= config.rows:
                    row = config.rows - 1

                if col < 0:
                    col = 0
                elif col >= config.columns:
                    col = config.columns - 1

                cell = board.get_cell(row, col)
                clicked_edge = cell.get_clicked_edge(mouse_x, mouse_y)
                if clicked_edge:
                    cell.set_clicked_edge(clicked_edge, current_player)
                    board.set_adjacent_clicked_edge(row, col, clicked_edge, current_player)

                board.redraw_dirty_cells()

        pygame.display.update()
        time.sleep(0.05)


if __name__ == '__main__':
    main()
