import math
import sys
import time

import pygame
from pygame.locals import *

from __init__ import *
from board import Board


def main():
    pygame.display.init()
    pygame.display.set_caption('Dots')

    # Create the game screen and initialize the size
    screen = pygame.display.set_mode((
        COLS * CELL_WIDTH + (COLS + 1) * EDGE_THICKNESS + GUTTER_LEFT + GUTTER_RIGHT,
        ROWS * CELL_HEIGHT + (ROWS + 1) * EDGE_THICKNESS + GUTTER_TOP + GUTTER_BOTTOM
    ))
    screen.fill(WHITE)

    board = Board()
    board.draw(screen)

    pygame.display.update()

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
                location = board.get_row_col(mouse_pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()


        time.sleep(0.001)


if __name__ == '__main__':
    main()
