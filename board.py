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
        self._dots: list[list[pg.Rect]] = []
        for r in range(0, self._cfg.CELL_ROWS + 1):
            row = []
            for c in range(0, self._cfg.CELL_COLS + 1):
                rect = pg.Rect(
                    (self._cfg.DOT_DIA + self._cfg.CELL_WIDTH) * c 
                    + self._cfg.GUTTER_WIDTH + x_shift, 
                    (self._cfg.DOT_DIA + self._cfg.CELL_HEIGHT) * r 
                    + self._cfg.GUTTER_WIDTH + y_shift, 
                    self._cfg.DOT_DIA, 
                    self._cfg.DOT_DIA
                )
                row.append(rect)
                pg.draw.rect(self._screen, BLACK, rect)
            self._dots.append(row)

        # Create the cells
        self._cells: list[list[pg.Rect]] = []
        for r in range(0, self._cfg.CELL_ROWS):
            row = []
            for c in range(0, self._cfg.CELL_COLS):
                rect = pg.Rect(
                    (c + 1) * self._cfg.DOT_DIA + c * self._cfg.CELL_WIDTH 
                    + self._cfg.GUTTER_WIDTH + x_shift, 
                    (r + 1) * self._cfg.DOT_DIA + r * self._cfg.CELL_HEIGHT 
                    + self._cfg.GUTTER_WIDTH + y_shift, 
                    self._cfg.CELL_WIDTH, 
                    self._cfg.CELL_HEIGHT
                )
                row.append(rect)
                pg.draw.rect(self._screen, BACKGROUND_COLOR, rect)
            self._cells.append(row)

        # Create the edges
        self._edges: list[list[pg.Rect]] = []
        for r in range(0, self._cfg.CELL_ROWS + 1):
            row = []
            for c in range(0, self._cfg.CELL_COLS + 1):
                h_edge, v_edge = None, None
                if c < self._cfg.CELL_COLS:
                    # horizontal edge
                    h_edge = pg.Rect(
                        (c + 1) * self._cfg.DOT_DIA + c * self._cfg.CELL_WIDTH 
                        + self._cfg.GUTTER_WIDTH + x_shift,

                        r * self._cfg.DOT_DIA + r * self._cfg.CELL_HEIGHT 
                        + self._cfg.GUTTER_WIDTH + y_shift,

                        self._cfg.CELL_WIDTH, 
                        self._cfg.DOT_DIA
                    )
                    pg.draw.rect(self._screen, EDGE_COLOR_DEFAULT, h_edge)
                
                if r < self._cfg.CELL_ROWS:
                    # vertical edge
                    v_edge = pg.Rect(
                        c * self._cfg.DOT_DIA + c * self._cfg.CELL_WIDTH 
                        + self._cfg.GUTTER_WIDTH + x_shift,
                        
                        (r + 1) * self._cfg.DOT_DIA + r * self._cfg.CELL_HEIGHT 
                        + self._cfg.GUTTER_WIDTH + y_shift,

                        self._cfg.DOT_DIA, 
                        self._cfg.CELL_HEIGHT
                    )
                    pg.draw.rect(self._screen, EDGE_COLOR_DEFAULT, v_edge)
            
                # Group the edges into tuples with (usually) two edges per 
                # tuple. Each tuple is stored by row,col in the edges 2-D list.
                # The last column will only have the vertical edge in the tuple.
                # The last row will only have the horizontal edge in the tuple.
                # The last row and column will be empty.
                if h_edge and v_edge:
                    row.append((h_edge, v_edge))
                elif h_edge:
                    row.append((h_edge,))
                elif v_edge:
                    row.append((v_edge,))
                else:
                    row.append(())

            self._edges.append(row)

        # Now when looking up the edge that contains x,y, you can quickly 
        # retrieve the tuple of edges that possibly contains x,y by:
        # row = y // (dd + ch)
        # col = x // (dd + cw)
        # Then simply check collidepoint on each edge to see if it contains the 
        # x,y

        # Now that all the entities have been created, it's time to establish
        # all of the connection relationships between them.
        # self._establish_connections()

        self.draw()

    def get_edge(self, pos: tuple) -> pg.Rect:
        x, y = pos
        row = y // (self._cfg.DOT_DIA + self._cfg.CELL_HEIGHT)
        col = x // (self._cfg.DOT_DIA + self._cfg.CELL_WIDTH)
        edges = self._edges[row][col]

        for edge in edges:
            if edge.collidepoint(pos):
                return edge
        return None

    def highlight_edge(self, edge: pg.Rect) -> None:
        if self._highlighted_edge != edge:
            if self._highlighted_edge:
                pg.draw.rect(self._screen, EDGE_COLOR_DEFAULT, self._highlighted_edge)
                pg.display.update(self._highlighted_edge)
                
            pg.draw.rect(self._screen, EDGE_CAPTURE_COLOR, edge, width=1)
            pg.display.update(edge)
            self._highlighted_edge = edge

    def unhighlight_edge(self) -> None:
        if self._highlighted_edge:
            pg.draw.rect(self._screen, EDGE_COLOR_DEFAULT, self._highlighted_edge)
            pg.display.update(self._highlighted_edge)

    def _establish_connections(self) -> None:
        for row in self._board:
            for entity in row:
                r, c = entity.row, entity.col
                if isinstance(entity, Cell):
                    # Every cell will always have four edges
                    entity.edge_top = self._board[r-1][c]
                    entity.edge_bottom = self._board[r+1][c]
                    entity.edge_left = self._board[r][c-1]
                    entity.edge_right = self._board[r][c+1]
                elif isinstance(entity, Edge):
                    # Depending on location in the board,
                    if r == 0: # top row of board
                        entity.cell1 = None
                        entity.cell2 = self._board[r+1][c]
                    elif r == 2 * self._cfg.CELL_ROWS: # bottom row of board
                        entity.cell1 = self._board[r-1][c]
                        entity.cell2 = None
                    elif c == 0: # left column of board
                        entity.cell1 = None
                        entity.cell2 = self._board[r][c+1]
                    elif c == 2 * self._cfg.CELL_COLS: # right column of board
                        entity.cell1 = self._board[r][c-1]
                        entity.cell2 = None
                    elif is_even(r): # horizontal edge
                        entity.cell1 = self._board[r-1][c]
                        entity.cell2 = self._board[r+1][c]
                    else: # vertical edge
                        entity.cell1 = self._board[r][c-1]
                        entity.cell2 = self._board[r][c+1]

    def draw(self) -> None:
        pg.display.flip()

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'{len(self._cells[0])}x{len(self._cells)} cells'

    def __repr__(self) -> str:
        return str(self)
