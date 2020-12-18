import math
import sys
import time

import pygame
from pygame.locals import *

from __init__ import *
from board import Board
from cell import Cell


def main():
    pygame.display.init()
    pygame.display.set_caption('Dots')

    screen = pygame.display.set_mode((
        COLS * CELL_WIDTH + GUTTER_LEFT + GUTTER_RIGHT,
        ROWS * CELL_HEIGHT + GUTTER_TOP + GUTTER_BOTTOM
    ))
    screen.fill(WHITE)

    board = Board()
    board.assign_neighbors()
    board.draw(screen)

    pygame.display.update()

    current_cell = None
    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
                coords = board.get_row_col(mouse_pos)
                cell = board[coords]
                clicked_edge = cell.get_edge(mouse_pos)
                cell.set_edge(clicked_edge)
                pygame.display.update(cell)
                pygame.display.update(cell.neighbors_list)

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
                coords = board.get_row_col(mouse_pos)
                if coords:
                    i, j = coords
                    cell = board[coords]
                    cell.highlight_edge(mouse_pos)
                    pygame.display.update(cell)
                    pygame.display.update(cell.neighbors_list)
                    current_cell = cell
                else:
                    if current_cell:
                        current_cell.clear_highlighted_edge()
                        pygame.display.update(current_cell)
                        current_cell = None


        time.sleep(0.001)


if __name__ == '__main__':
    main()
