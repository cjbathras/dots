import argparse
import traceback

import pygame as pg

from __init__ import *
from banner import Banner
from board import Board
from button import Button
from cell import Cell
from config import Config
from dot import Dot
from edge import Edge
from entity import Entity
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
        nargs='*', help='names of the two - four players (default: Alice Bob)')

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
        self._board = Board()
        self._scoreboard = Scoreboard(self._cfg.SCOREBOARD_ORIGIN,
            self._cfg.SCOREBOARD_SIZE, LIGHT_GRAY, self._game)

        self._play_again_button = Button(
            (screen_rect.width // 2 - 50, screen_rect.height - 70), (100, 35),
            text='Play Again?', visible=False)

    def quit(self):
        self._done = True

    def run(self):
        # Game play loop
        self._current_player = self._game.current_player()
        self._highlighted_edge = None
        self._cell_captured = False

        while not self._done:
            self._clock.tick(30)
            self.handle_events()
            self.run_logic()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                self._done = True

            if event.type == pg.MOUSEMOTION:
                entity = self._board.get_entity(event.pos)
                if entity:
                    entity.handle_event(event)

                # if entity and isinstance(entity, Edge):
                #     entity.highlight()
                #     self._highlighted_edge = entity
                # elif self._highlighted_edge:
                #     self._highlighted_edge.clear()

            elif event.type == pg.MOUSEBUTTONUP:
                entity = self._board.get_entity(event.pos)
                if entity:
                    entity.handle_event(event)

                    # entity.capture()
                    # if entity.cell1:
                    #     entity.cell1.check_for_capture(self._current_player)
                    # if entity.cell2:
                    #     entity.cell2.check_for_capture(self._current_player)

            self._play_again_button.handle_event(event)

    def run_logic(self):
        pass

    def draw(self):
        pg.display.flip()

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


if __name__ == '__main__':
    try:
        args = parse_args()
        pg.display.init()
        pg.display.set_caption('Dots')

        # Config MUST be initialized here for the singleton to be configured
        # properly for use elsewhere
        cfg = Config(cell_rows=args.r, cell_cols=args.c,
            cell_size=(args.w, args.t), num_players=len(args.p))

        # Initialize pygame
        screen = pg.display.set_mode(cfg.SCREEN_SIZE)
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
