import pygame as pg

from __init__ import *
from __init__ import is_even
from __init__ import is_odd

from cell import Cell
from config import Config
from dot import Dot
from edge import Edge
from entity import Entity


class Board:
    def __init__(self, x_shift: int=0, y_shift: int=0):
        super().__init__()
        self._cfg: Config = Config()
        self._x_shift: int = x_shift
        self._y_shift: int = y_shift
        self._screen: pg.Surface = pg.display.get_surface()
        self._highlighted_edge = None

        # Create the dots
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

        # Create the cells
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

        # Create the edges
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

                # Establish cell to edge relationships
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

                # Establish cell to edge relationships
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
        # To look up the edge to see if it contains the x,y you can quickly 
        # retrieve the tuple of edges that possibly contains x,y by:
        # row = y // (dd + ch)
        # col = x // (dd + cw)
        # Then simply check collidepoint on each edge to see if it contains the 
        # x,y
        x, y = pos
        row = (y - self._y_shift - self._cfg.GUTTER_WIDTH) // \
            (self._cfg.DOT_DIA + self._cfg.CELL_HEIGHT)
        col = (x - self._x_shift - self._cfg.GUTTER_WIDTH) // \
            (self._cfg.DOT_DIA + self._cfg.CELL_WIDTH)
        edges = self._edges[row][col]

        for edge in edges:
            if edge.collidepoint(pos):
                return edge
        return None

    def highlight_edge(self, edge: Edge) -> None:
        if not edge.captured and self._highlighted_edge != edge:
            if self._highlighted_edge:
                pg.draw.rect(self._screen,
                    EDGE_COLOR_DEFAULT, self._highlighted_edge)
                pg.display.update(self._highlighted_edge)
                
            pg.draw.rect(self._screen, EDGE_COLOR_CAPTURED, edge, width=1)
            pg.display.update(edge)
            self._highlighted_edge = edge

    def unhighlight_edge(self) -> None:
        if self._highlighted_edge:
            pg.draw.rect(self._screen, EDGE_COLOR_DEFAULT, 
                self._highlighted_edge)
            pg.display.update(self._highlighted_edge)
            self._highlighted_edge = None

    def capture_edge(self, edge: Edge) -> None:
        self._highlighted_edge = None
        edge.captured = True
        pg.draw.rect(self._screen, EDGE_COLOR_CAPTURED, edge)
        pg.display.update(edge)

    def draw(self) -> None:
        pg.display.flip()

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'{len(self._cells[0])}x{len(self._cells)} cells'

    def __repr__(self) -> str:
        return str(self)
