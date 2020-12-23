import argparse
import sys
import traceback

import pygame as pg
# from pygame.locals import QUIT
# from pygame.locals import MOUSEBUTTONDOWN
# from pygame.locals import MOUSEBUTTONUP
# from pygame.locals import MOUSEMOTION

from __init__ import *
from banner import Banner
from board import Board
from button import Button
from cell import Cell
from config import Config
from dot import Dot
from edge import Edge
from game import Game
from player import Player
from scoreboard import Scoreboard

clock = pg.time.Clock()

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

    parser.add_argument('-p', metavar='PLAYER', default=['Alice', 'Bob'],
        nargs=2, help='names of the two - four players (default: Alice Bob)')

    args = parser.parse_args()
    return args


class Dots:
    def __init__(self, screen, args):
        self._done = False
        self._clock = pg.time.Clock()
        self._screen = screen
        self._cfg = Config()

        screen_rect = self._screen.get_rect()

        # Create the static components
        if 1 < len(args.p) < 5:
            self._players = [Player(p, get_color()) for p in args.p]
        else:
            raise Exception('Only two to four players are allowed')

        self._game = Game(self._players)
        # self._board = Board()
        self._scoreboard = Scoreboard(self._cfg.SCOREBOARD_ORIGIN, 
            self._cfg.SCOREBOARD_SIZE, LIGHT_GRAY, self._game)
        self._scoreboard.draw()
        # self._banner = Banner(pg.Rect(self._cfg.BANNER_ORIGIN, self._cfg.BANNER_SIZE), LIGHT_GRAY)

        self._play_again_button = Button(
            (screen_rect.width // 2 - 50, screen_rect.height - 50), (100, 35), 
            text='Play Again?', visible=False)
        self._play_again_button.draw()

    def quit(self):
        self._done = True

    def run(self):
        # Game play loop
        while not self._done:
            self._dt = self._clock.tick(30) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                self._done = True

            self._play_again_button.handle_event(event)
            self._play_again_button.draw()

            # for sprite in self._all_sprites:
            #     sprite.handle_event(event)

    def run_logic(self):
        pass

    def draw(self):
        pg.display.flip()

    # def add_sprite(self, spr):
    #     self._all_sprites.add(spr)

# def play(args, cfg):
#     # Create the static components
#     player1 = Player(args.p[0], PLAYER1_COLOR)
#     player2 = Player(args.p[1], PLAYER2_COLOR)
#     game = Game([player1, player2])
#     board = Board()
#     scoreboard = Scoreboard(
#         pg.Rect(cfg.SCOREBOARD_ORIGIN, cfg.SCOREBOARD_SIZE),
#         LIGHT_GRAY, game
#     )
#     banner = Banner(pg.Rect(cfg.BANNER_ORIGIN, cfg.BANNER_SIZE), LIGHT_GRAY)
#     play_again_button = Button('Play Again?')
#     play_again_button.center = \
#         (pg.display.get_surface().get_width() // 2,
#         pg.display.get_surface().get_height() \
#         - play_again_button.height - 20)
#     play_again_button.visible = False

#     # Initialize game state
#     current_player = game.current_player()
#     highlighted_edge = None

#     # Draw the components
#     board.draw()
#     scoreboard.draw()

#     buttons = [play_again_button]

#     # Game play loop
#     while True:
#         # Iterate through all of the current events in the event queue
#         for event in pg.event.get():

#             if event.type == QUIT:
#                 pg.quit()
#                 sys.exit()

#             elif event.type == MOUSEMOTION:
#                 location = board.get_row_col(event.pos)
#                 entity = board[location]
#                 if isinstance(entity, Edge) and not game.is_over:
#                     entity.highlight()
#                     highlighted_edge = entity
#                 else:
#                     if highlighted_edge:
#                         highlighted_edge.clear()

#                 for b in buttons:
#                     b.on_mouse_enter(event.pos)
#                     b.on_mouse_leave(event.pos)

#             elif event.type == MOUSEBUTTONDOWN:
#                 for b in buttons:
#                     b.on_mouse_down(event.pos)

#             elif event.type == MOUSEBUTTONUP:
#                 location = board.get_row_col(event.pos)
#                 entity = board[location]

#                 if isinstance(entity, Edge):
#                     edge_captured = entity.capture()

#                     if edge_captured:
#                         cell1_captured = \
#                             entity.cell1.check_for_capture(current_player) \
#                                 if entity.cell1 else False

#                         cell2_captured = \
#                             entity.cell2.check_for_capture(current_player) \
#                                 if entity.cell2 else False

#                         if not cell1_captured and not cell2_captured:
#                             current_player = game.next_player()
#                             scoreboard.set_active_box(current_player)

#                         else:
#                             if cell1_captured:
#                                 game.increment_score(current_player)
#                             if cell2_captured:
#                                 game.increment_score(current_player)

#                             scoreboard.update_score(current_player)
#                             winner = game.check_for_winner()

#                             if winner is not None:
#                                 banner.draw(winner)
#                                 play_again_button.visible = True
#                                 play_again_button.draw()

#                 for b in buttons:
#                     b.on_mouse_up(event.pos)
#                     banner.clear()

#         # Very brief sleep so the process doesn't peg the CPU
#         clock.tick(30)


if __name__ == '__main__':
    try:
        args = parse_args()
        pg.display.init()
        pg.display.set_caption('Dots')

        # Config MUST be initialized here for the singleton to be configured
        # properly for use elsewhere
        config = Config(rows=args.r, cols=args.c, cell_size=(args.w, args.t))

        # Initialize pygame
        screen = pg.display.set_mode((
            config.COLS * config.CELL_WIDTH
            + (config.COLS + 1) * config.EDGE_THICKNESS
            + config.GUTTER_LEFT
            + config.GUTTER_RIGHT,

            config.ROWS * config.CELL_HEIGHT
            + (config.ROWS + 1) * config.EDGE_THICKNESS
            + config.GUTTER_TOP * 2
            + config.SCOREBOARD_HEIGHT
            + config.GUTTER_BOTTOM * 2
            + config.BANNER_HEIGHT
        ))
        screen.fill(BACKGROUND_COLOR)
        pg.display.update()

        dots = Dots(screen, args)
        dots.run()

    except Exception as e:
        print()
        print(traceback.format_exc())
        parser.print_usage()

    finally:
        pg.quit()
