import sys
import time

import pygame
from pygame.locals import *

from __init__ import *
from board import Board
from cell import Cell
from dot import Dot
from edge import Edge
from game import Game
from player import Player
from scoreboard import Scoreboard


def play():
    # Initialize pygame
    pygame.display.init()
    pygame.display.set_caption('Dots')

    # Create the game screen and initialize the size
    screen = pygame.display.set_mode((
        COLS * CELL_WIDTH + (COLS + 1) * EDGE_THICKNESS + GUTTER_LEFT + GUTTER_RIGHT,
        ROWS * CELL_HEIGHT + (ROWS + 1) * EDGE_THICKNESS + GUTTER_TOP * 2 + SCOREBOARD_HEIGHT + GUTTER_BOTTOM
    ))
    screen.fill(WHITE)

    # Create the players
    player1 = Player('Player 1', PLAYER1_COLOR)
    player2 = Player('Player 2', PLAYER2_COLOR)

    # Create the game
    game = Game(player1, player2)
    current_player = game.current_player()

    # Create the board
    board = Board()
    board.draw()

    # Create the scoreboard
    scoreboard = Scoreboard(pygame.Rect(SCOREBOARD_ORIGIN, SCOREBOARD_SIZE), LIGHT_GRAY, game)
    scoreboard.draw()

    highlighted_edge = None

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
                location = board.get_row_col(mouse_pos)
                entity = board[location]
                if isinstance(entity, Edge):
                    entity.highlight()
                    highlighted_edge = entity
                else:
                    if highlighted_edge:
                        highlighted_edge.clear()

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
                location = board.get_row_col(mouse_pos)
                entity = board[location]

                if isinstance(entity, Edge):
                    success = entity.activate()

                    if success:
                        capture1_success = entity.cell1.check_for_capture(current_player) if entity.cell1 else False
                        capture2_success = entity.cell2.check_for_capture(current_player) if entity.cell2 else False

                        if not capture1_success and not capture2_success:
                            current_player = game.next_player()
                            scoreboard.set_active_box(current_player)

        # Very brief sleep so the process doesn't peg the CPU
        time.sleep(0.001)


if __name__ == '__main__':
    play()
