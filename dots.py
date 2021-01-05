"""Dots is an implementation of the classic game where you draw a bunch of dots
on a piece of paper in a grid pattern and then players take turns connecting the
dots. When a square, or cell, is made the player "captures" the cell. The player
with the greatest number of captured cells at the end of the game wins."""

# Copyright 2021 Curt Bathras
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import traceback

import pygame as pg

from __init__ import *
from banner import Banner
from board import Board
from button import Button
from config import Config
from edge import Edge
from game import Game
from player import Player
from scoreboard import Scoreboard

DESCRIPTION="""
A pygame implementation of the classic game of trying to capture as many cells
as you can by connecting the dots.
"""

parser = argparse.ArgumentParser(description=DESCRIPTION)


def parse_args():
    """Parse all of the command line arguments."""
    parser.add_argument('-r', metavar='ROWS', default='4', type=int,
        help='number of rows of cells (default: 4)')

    parser.add_argument('-c', metavar='COLUMNS', default='4', type=int,
        help='number of columns of cells (default: 4)')

    parser.add_argument('-w', metavar='CELL_WIDTH', default='100', type=int,
        help='width of cells (default: 100 pixels)')

    parser.add_argument('-t', metavar='CELL_HEIGHT', default='100', type=int,
        help='height of cells (default: 100 pixels)')

    parser.add_argument('-p', metavar='PLAYER', default=['Alice', 'Bob'],
        nargs='*', help='names of the two to four players (default: Alice Bob)')

    args = parser.parse_args()
    return args


class Dots:
    """Dots is the main object the encompasses the entire game. It is
    responsible for instantiating all graphics objects, the game object, the
    player objects, and managing game play."""
    def __init__(self, screen, args):
        self._done = False
        self._clock = pg.time.Clock()
        self._screen = screen
        self._cfg = Config()
        self._game_over = False
        self._banner = None
        self._game = None
        self._scoreboard = None
        self._board = None
        self._current_player = None
        self._highlighted_edge = None
        self._cell_captured = False
        self._captured_edge = None
        self._play_again_button = None

        # Create the static components
        if 1 < len(args.p) < 5:
            self._players = [Player(p, get_color()) for p in args.p]
        else:
            raise Exception('Only two to four players are allowed')

        self.new_game()

    def new_game(self) -> None:
        """Creates a new game and resets all entities."""
        if self._play_again_button:
            self._play_again_button.visible = False
        self._game = Game(self._players)
        self._scoreboard = Scoreboard(self._cfg.SCOREBOARD_ORIGIN,
            self._cfg.SCOREBOARD_SIZE, LIGHT_GRAY, self._game)
        self._board = Board(
            x_shift=0, y_shift=self._cfg.SCOREBOARD_HEIGHT+GAP_20)
        self._current_player: Player = self._game.current_player
        self._highlighted_edge: Edge = None
        self._cell_captured: bool = False
        self._captured_edge: Edge = None
        self._scoreboard.set_active(self._current_player)
        self._game_over = False

    def quit(self) -> None:
        """Set the done flag to True so the game can quit."""
        self._done = True

    def run(self) -> None:
        """Run the main game play loop until commanded to quit."""
        while not self._done:
            self._clock.tick(30)
            self.handle_events()
            self.check_game_state()
            self.draw()

    def handle_events(self) -> None:
        """Handle all game events."""
        for event in pg.event.get():

            if event.type == pg.QUIT:
                self._done = True

            if event.type == pg.MOUSEMOTION:
                if not self._game_over:
                    edge = self._board.get_edge(event.pos)
                    if edge:
                        edge.handle_event(event)
                        self._highlighted_edge = edge
                    elif self._highlighted_edge:
                        self._highlighted_edge.clear()

            elif event.type == pg.MOUSEBUTTONUP:
                if not self._game_over:
                    edge = self._board.get_edge(event.pos)
                    if edge and not edge.captured:
                        edge.handle_event(event)
                        if edge.captured:
                            self._captured_edge = edge

            if self._play_again_button:
                self._play_again_button.handle_event(event)

    def check_game_state(self) -> None:
        """Checks for cell capture and if the game is over."""
        if self._captured_edge:
            cell1_captured, cell2_captured = False, False

            # Check to see if any cells were captured. If so, increment score
            # of current player for each cell captured.
            if self._captured_edge.cell1:
                cell1_captured = self._captured_edge.cell1.check_for_capture(
                    self._current_player)
                if cell1_captured:
                    self._game.increment_score(self._current_player)
            if self._captured_edge.cell2:
                cell2_captured = self._captured_edge.cell2.check_for_capture(
                    self._current_player)
                if cell2_captured:
                    self._game.increment_score(self._current_player)

            if cell1_captured or cell2_captured:
                self._scoreboard.update_score(self._current_player,
                    self._game.get_score(self._current_player))

            # Check to see if anyone won
            winners = self._game.check_for_winner()
            if winners:
                # If there are winners, display the banner and play again button
                self._banner = Banner(
                    pg.Rect(0, 0, self._cfg.SCOREBOARD_WIDTH*0.8, 100),
                    LIGHT_GRAY)
                self._banner.draw(winners)
                self._game_over = True

                self._play_again_button = Button(
                    (self._banner.centerx - 50, self._banner.bottom + 35),
                    (100, 35),
                    callback=self.new_game,
                    text='Play Again?', visible=False)
                self._play_again_button.visible = True
                self._play_again_button.draw()

            else:
                # If no cells were captured, move to next player
                if not cell1_captured and not cell2_captured:
                    self._scoreboard.set_inactive(self._current_player)
                    self._current_player = self._game.next_player()
                    self._scoreboard.set_active(self._current_player)

            self._captured_edge = None

    def draw(self) -> None:
        """Draws the entire game to the screen."""
        pg.display.flip()


if __name__ == '__main__':
    try:
        # Get the command line arguments
        args = parse_args()

        # Initialize the pygame engine
        pg.display.init()
        pg.display.set_caption('Dots')

        # Config MUST be initialized here for the singleton to be configured
        # properly for use elsewhere
        cfg = Config(cell_rows=args.r, cell_cols=args.c,
            cell_size=(args.w, args.t), num_players=len(args.p))

        # Initialize the display
        screen = pg.display.set_mode(cfg.SCREEN_SIZE)
        screen.fill(BACKGROUND_COLOR)
        pg.display.update()

        # Create the main game object and start the game loop
        dots = Dots(screen, args)
        dots.run()

    except Exception as e:
        print()
        print(traceback.format_exc())
        parser.print_usage()

    finally:
        pg.quit()
