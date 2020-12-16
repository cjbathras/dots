import sys
import time

import pygame
from pygame.locals import *

from board import Board
import constants as c
from config import Config
from game import Game
from player import Player
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

    game = Game(
        Player(c.PLAYER1, c.PLAYER1_COLOR),
        Player(c.PLAYER2, c.PLAYER2_COLOR)
    )
    current_player = game.current_player()

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                board.handle_selection(mouse_x, mouse_y, current_player)

                board.redraw_dirty_cells()

        pygame.display.update()
        time.sleep(0.05)


if __name__ == '__main__':
    main()
