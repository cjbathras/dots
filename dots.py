import argparse
import sys
import time
import traceback

import pygame
from pygame.locals import *

from __init__ import *
from board import Board
from cell import Cell
from config import Config
from dot import Dot
from edge import Edge
from footer import Footer
from game import Game
from player import Player
from scoreboard import Scoreboard

DESCRIPTION="""
A simple game of trying to capture as many cells as you can by connecting
the dots.
"""

parser = argparse.ArgumentParser(description=DESCRIPTION)


def parse_args():
    parser.add_argument('-r', metavar='ROWS', default='4', type=int,
                        help='number of rows of cells (default: 4)')
    parser.add_argument('-c', metavar='COLUMNS', default='4', type=int,
                        help='number of columns of cells (default: 4)')
    parser.add_argument('-w', metavar='CELL_WIDTH', default='100', type=int,
                        help='width of cells (default: 100 pixels)')
    parser.add_argument('-t', metavar='CELL_HEIGHT', default='100', type=int,
                        help='height of cells (default: 100 pixels)')
    parser.add_argument('-p', metavar='PLAYER', default=['Player1', 'Player2'], nargs=2,
                        help='names of the two players (default: Player1 Player2)')
    args = parser.parse_args()
    return args


def play(args, cfg):
    # Initialize pygame
    pygame.display.init()
    pygame.display.set_caption('Dots')
    screen = pygame.display.set_mode((
        cfg.COLS * cfg.CELL_WIDTH + (cfg.COLS + 1) * cfg.EDGE_THICKNESS + cfg.GUTTER_LEFT + cfg.GUTTER_RIGHT,
        cfg.ROWS * cfg.CELL_HEIGHT + (cfg.ROWS + 1) * cfg.EDGE_THICKNESS + cfg.GUTTER_TOP * 2 + cfg.SCOREBOARD_HEIGHT + cfg.GUTTER_BOTTOM * 2 + cfg.FOOTER_HEIGHT
    ))

    # Create the static components
    player1 = Player(args.p[0], PLAYER1_COLOR)
    player2 = Player(args.p[1], PLAYER2_COLOR)
    game = Game(player1, player2)
    board = Board()
    scoreboard = Scoreboard(pygame.Rect(cfg.SCOREBOARD_ORIGIN, cfg.SCOREBOARD_SIZE), LIGHT_GRAY, game)
    footer = Footer(pygame.Rect(cfg.FOOTER_ORIGIN, cfg.FOOTER_SIZE), LIGHT_GRAY)

    # Initialize game state
    current_player = game.current_player()
    highlighted_edge = None

    # Draw the components
    screen.fill(BACKGROUND_COLOR)
    board.draw()
    scoreboard.draw()



    footer.draw([player1])



    # Game play loop
    while True:
        # Iterate through all of the current events in the event queue
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
                        else:
                            if capture1_success: game.increment_score(current_player)
                            if capture2_success: game.increment_score(current_player)
                            scoreboard.update_score(current_player)
                            winner = game.check_for_winner()
                            if winner is not None:
                                footer.draw(winner)

        # Very brief sleep so the process doesn't peg the CPU
        # time.sleep(0.001)


if __name__ == '__main__':
    try:
        args = parse_args()
        # Config MUST be initialized here for the singleton to be configured
        # properly for use elsewhere
        config = Config(rows=args.r, cols=args.c, cell_size=(args.w, args.t))
        play(args, config)
    except Exception as e:
        print()
        print(traceback.format_exc())
        parser.print_usage()
    finally:
        pygame.quit()
