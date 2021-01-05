"""The main board for game play in the game of Dots."""

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

import pygame as pg

from __init__ import *

from cell import Cell
from config import Config
from dot import Dot
from edge import Edge


class Board:
    """A Board is the collection of all of the entities that make up the game.
    Namely, dots, edges, and cells. Entities are grouped into what I call
    superrows and supercolumns. A single element, or supercell, of a superrow
    and supercolumn is the collection of one dot, two edges and one cell. The
    number of superrows is one greater than the number of cells in the board's
    height and the number of supercolumns is one greater than the number of
    cells in the board's width. Superrows and supercolumns allow for a very fast
    lookup of which two edges could possibly contain a point in space. Once the
    supercell is known, it is quick to check if either edge contains the point.

    The diagram below illustrates the concept of a supercell. D = a dot, E = an
    edge, C = a cell.

    DDD | EEEEEEEEEEEEEEE
    DDD | EEEEEEEEEEEEEEE
    ---------------------
    EEE | CCCCCCCCCCCCCCC
    EEE | CCCCCCCCCCCCCCC
    EEE | CCCCCCCCCCCCCCC
    EEE | CCCCCCCCCCCCCCC
    EEE | CCCCCCCCCCCCCCC
    EEE | CCCCCCCCCCCCCCC

    This supercell consists of one dot, two edges (one vertical and one
    horizontal) and one cell. For the last supercolumn, the supercell only
    contains the dot and vertical edge. For the last superrow, the supercell
    only contains the dot and horizontal edge. The upper left corner of a
    supercell and its height and width are well-defined. So the lookup of which
    supercell contains a point is very fast. From there, it is at most two
    comparisons to see if either edge contains the point.
    """
    def __init__(self, x_shift: int=0, y_shift: int=0):
        super().__init__()
        self._cfg: Config = Config()
        self._x_shift: int = x_shift
        self._y_shift: int = y_shift
        self._screen: pg.Surface = pg.display.get_surface()
        self._highlighted_edge = None

        # Create the dots (a 2D list of Dot objects)
        self._dots: list[list[Dot]] = []
        for r in range(0, self._cfg.CELL_ROWS + 1):
            row = []
            for c in range(0, self._cfg.CELL_COLS + 1):
                dot = Dot(
                    ((self._cfg.DOT_DIA + self._cfg.CELL_WIDTH) * c
                    + self._cfg.GUTTER_WIDTH + self._x_shift,
                    (self._cfg.DOT_DIA + self._cfg.CELL_HEIGHT) * r
                    + self._cfg.GUTTER_WIDTH + self._y_shift),

                    (self._cfg.DOT_DIA, self._cfg.DOT_DIA),

                    BLACK
                )
                row.append(dot)
                dot.draw()
            self._dots.append(row)

        # Create the cells (a 2D list of Cell objects)
        self._cells: list[list[Cell]] = []
        for r in range(0, self._cfg.CELL_ROWS):
            row = []
            for c in range(0, self._cfg.CELL_COLS):
                cell = Cell(
                    ((c + 1) * self._cfg.DOT_DIA + c * self._cfg.CELL_WIDTH
                    + self._cfg.GUTTER_WIDTH + self._x_shift,
                    (r + 1) * self._cfg.DOT_DIA + r * self._cfg.CELL_HEIGHT
                    + self._cfg.GUTTER_WIDTH + self._y_shift),

                    (self._cfg.CELL_WIDTH,  self._cfg.CELL_HEIGHT),

                    BACKGROUND_COLOR
                )
                row.append(cell)
                cell.draw()
            self._cells.append(row)

        # Create the edges (a 2D list of Edge objects)
        # Superrows and supercolumns are rows and columns of a collection
        # of one dot, two edges, and one cell. This allows for easy grouping
        # and lookup of edges based on mouse location.
        self._edges: list[list[Edge]] = []
        for r in range(0, self._cfg.CELL_ROWS + 1):
            row = []
            for c in range(0, self._cfg.CELL_COLS + 1):
                h_edge, v_edge = None, None
                if c < self._cfg.CELL_COLS:
                    # horizontal edge
                    h_edge = Edge(
                        ((c + 1) * self._cfg.DOT_DIA + c * self._cfg.CELL_WIDTH
                        + self._cfg.GUTTER_WIDTH + self._x_shift,
                        r * self._cfg.DOT_DIA + r * self._cfg.CELL_HEIGHT
                        + self._cfg.GUTTER_WIDTH + self._y_shift),

                        (self._cfg.CELL_WIDTH, self._cfg.DOT_DIA),

                        EDGE_COLOR_DEFAULT
                    )
                    h_edge.draw()

                # Establish cell to edge relationships - for checking whether a
                # cell is captured by a user, we need to know which cells the
                # edge touches. An edge always touches one or two cells. Edges
                # that touch one cell are the edges that make up the exterior
                # of the board.
                # top superrow
                if h_edge and r == 0:
                    h_edge.cell2 = self._cells[r][c]
                    self._cells[r][c].edge_top = h_edge

                # bottom superrow
                elif h_edge and r == self._cfg.CELL_ROWS:
                    h_edge.cell1 = self._cells[r-1][c]
                    self._cells[r-1][c].edge_bottom = h_edge

                # all other superrows
                elif h_edge:
                    h_edge.cell1 = self._cells[r-1][c]
                    h_edge.cell2 = self._cells[r][c]
                    self._cells[r][c].edge_top = h_edge
                    self._cells[r-1][c].edge_bottom = h_edge

                if r < self._cfg.CELL_ROWS:
                    # vertical edge
                    v_edge = Edge(
                        (c * self._cfg.DOT_DIA + c * self._cfg.CELL_WIDTH
                        + self._cfg.GUTTER_WIDTH + self._x_shift,
                        (r + 1) * self._cfg.DOT_DIA + r * self._cfg.CELL_HEIGHT
                        + self._cfg.GUTTER_WIDTH + self._y_shift),

                        (self._cfg.DOT_DIA, self._cfg.CELL_HEIGHT),

                        EDGE_COLOR_DEFAULT
                    )
                    v_edge.draw()

                # Establish cell to edge relationships - for checking whether a
                # cell is captured by a user, we need to know which edges the
                # cell touches. A cell always touches four edges: top, bottom,
                # left and right.
                # left supercolumn
                if v_edge and c == 0:
                    v_edge.cell2 = self._cells[r][c]
                    self._cells[r][c].edge_left = v_edge

                # right supercolumn
                elif v_edge and c == self._cfg.CELL_COLS:
                    v_edge.cell1 = self._cells[r][c-1]
                    self._cells[r][c-1].edge_right = v_edge

                # all other supercolumns
                elif v_edge:
                    v_edge.cell1 = self._cells[r][c-1]
                    v_edge.cell2 = self._cells[r][c]
                    self._cells[r][c].edge_left = v_edge
                    self._cells[r][c-1].edge_right = v_edge

                # Group the edges into tuples with (usually) two edges per
                # tuple. Each tuple is stored by row,col in the edges 2-D list.
                # The last column will only have the vertical edge in the tuple.
                # The last row will only have the horizontal edge in the tuple.
                # The last row and column will be empty.
                # Each member of the tuple is a dict that stores a reference to
                # the pg.Rect that represents the edge, its capture status, and
                # a tuple of cells it touches.
                if h_edge and v_edge:
                    row.append((h_edge, v_edge))
                elif h_edge: # bottom row
                    row.append((h_edge,))
                elif v_edge: # right col
                    row.append((v_edge,))
                else: # bottom, right corner
                    row.append(())

            self._edges.append(row)

        self.draw()

    def get_edge(self, pos: tuple) -> Edge:
        """Retrieve the edge containing pos."""
        # To look up the edge to see if it contains the x,y you can quickly
        # retrieve the tuple of edges that possibly contains x,y by:
        # row = y // (dd + ch)
        # col = x // (dd + cw)
        # Then simply check collidepoint on each edge to see if it contains the
        # x,y
        try:
            x, y = pos
            # Determine the superrow and supercolumn containing the point
            row = (y - self._y_shift - self._cfg.GUTTER_WIDTH) // \
                (self._cfg.DOT_DIA + self._cfg.CELL_HEIGHT)
            col = (x - self._x_shift - self._cfg.GUTTER_WIDTH) // \
                (self._cfg.DOT_DIA + self._cfg.CELL_WIDTH)
            edges = self._edges[row][col]

            # Check to see if either edge contains the point
            for edge in edges:
                if edge.collidepoint(pos):
                    return edge
            return None
        except IndexError:
            return None

    def highlight_edge(self, edge: Edge) -> None:
        """Highlight the specified edge."""
        if not edge.captured and self._highlighted_edge != edge:
            if self._highlighted_edge:
                pg.draw.rect(self._screen,
                    EDGE_COLOR_DEFAULT, self._highlighted_edge)
                pg.display.update(self._highlighted_edge)

            pg.draw.rect(self._screen, EDGE_COLOR_CAPTURED, edge, width=1)
            pg.display.update(edge)
            self._highlighted_edge = edge

    def unhighlight_edge(self) -> None:
        """Clear the highlighted edge so it is no longer highlighted."""
        if self._highlighted_edge:
            pg.draw.rect(self._screen, EDGE_COLOR_DEFAULT,
                self._highlighted_edge)
            pg.display.update(self._highlighted_edge)
            self._highlighted_edge = None

    def capture_edge(self, edge: Edge) -> None:
        """Capture the specified edge."""
        self._highlighted_edge = None
        edge.captured = True
        pg.draw.rect(self._screen, EDGE_COLOR_CAPTURED, edge)
        pg.display.update(edge)

    def draw(self) -> None:
        """Draw the entire board."""
        pg.display.flip()

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'{len(self._cells[0])}x{len(self._cells)} cells'

    def __repr__(self) -> str:
        return str(self)
