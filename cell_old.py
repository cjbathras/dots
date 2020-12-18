from collections import namedtuple
import math

import pygame

from __init__ import *


Neighbors = namedtuple('Neighbors', ['top', 'bottom', 'left', 'right'])


class Cell(pygame.Rect):
    def __init__(self, origin, size, row, col, bg_color):
        super().__init__(origin, size)
        self.bg_color = bg_color
        self.row = row
        self.col = col
        self.is_captured = False
        self.is_dirty = False
        self.neighbors = None
        self.neighbors_list = []
        self.highlighted_edge = None
        self.screen = pygame.display.get_surface()

        # Value is True if edge has been activated, False otherwise
        self.edge_status = {TOP: False, BOTTOM: False, RIGHT: False, LEFT: False}

        # Prefix of r_ means variable is a Rect
        # tl = top left
        # tr = top right
        # bl = bottom left
        # br = bottom right

        # Define all of the component rectangles

        # Corner dots
        self.r_dot_tl = pygame.Rect(self.x - DOT_RAD, self.y - DOT_RAD, DOT_DIA, DOT_DIA)
        self.r_dot_tr = pygame.Rect(self.topright[0] - DOT_RAD, self.y - DOT_RAD, DOT_DIA, DOT_DIA)
        self.r_dot_bl = pygame.Rect(self.bottomleft[0] - DOT_RAD, self.bottomleft[1] - DOT_RAD, DOT_DIA, DOT_DIA)
        self.r_dot_br = pygame.Rect(self.bottomright[0] - DOT_RAD, self.bottomright[1] - DOT_RAD, DOT_DIA, DOT_DIA)

        # Edges
        self.r_top_edge = pygame.Rect(self.topleft, (self.width, DOT_DIA * 0.707))
        self.r_top_edge.center = self.midtop
        self.r_bottom_edge = pygame.Rect(self.topleft, (self.width, DOT_DIA * 0.707))
        self.r_bottom_edge.center = self.midbottom
        self.r_left_edge = pygame.Rect(self.topleft, (DOT_DIA * 0.707, self.height))
        self.r_left_edge.center = self.midleft
        self.r_right_edge = pygame.Rect(self.topleft, (DOT_DIA * 0.707, self.height))
        self.r_right_edge.center = self.midright

        # Edge highlights
        self.r_top_highlight = self.r_top_edge.move(0, 0)
        self.r_top_highlight.width -= (DOT_DIA * 2)
        self.r_top_highlight.height = HIGHLIGHT_WIDTH
        self.r_top_highlight.center = self.r_top_edge.center

        self.r_bottom_highlight = self.r_bottom_edge.move(0, 0)
        self.r_bottom_highlight.width -= (DOT_DIA * 2)
        self.r_bottom_highlight.height = HIGHLIGHT_WIDTH
        self.r_bottom_highlight.center = self.r_bottom_edge.center

        self.r_left_highlight = self.r_left_edge.move(0, 0)
        self.r_left_highlight.width = HIGHLIGHT_WIDTH
        self.r_left_highlight.height -= (DOT_DIA * 2)
        self.r_left_highlight.center = self.r_left_edge.center

        self.r_right_highlight = self.r_right_edge.move(0, 0)
        self.r_right_highlight.width = HIGHLIGHT_WIDTH
        self.r_right_highlight.height -= (DOT_DIA * 2)
        self.r_right_highlight.center = self.r_right_edge.center

    def assign_neighbors(self, top, bottom, left, right):
        self.neighbors = Neighbors(top, bottom, left, right)

        if top:
            self.neighbors_list.append(top)
        if bottom:
            self.neighbors_list.append(bottom)
        if left:
            self.neighbors_list.append(left)
        if right:
            self.neighbors_list.append(right)

    def draw(self, surface):
        # Draw the component shapes
        pygame.draw.rect(surface, self.bg_color, self)

        pygame.draw.circle(surface, BLACK, self.r_dot_tl.center, DOT_RAD)
        pygame.draw.circle(surface, BLACK, self.r_dot_tr.center, DOT_RAD)
        pygame.draw.circle(surface, BLACK, self.r_dot_bl.center, DOT_RAD)
        pygame.draw.circle(surface, BLACK, self.r_dot_br.center, DOT_RAD)

    def highlight_edge(self, pos):
        if not self.edge_status[TOP] and self.r_top_edge.collidepoint(pos):
            pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, self.r_top_highlight, width=0)
            self.highlighted_edge = self.r_top_highlight

        elif not self.edge_status[BOTTOM] and self.r_bottom_edge.collidepoint(pos):
            pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, self.r_bottom_highlight, width=0)
            self.highlighted_edge = self.r_bottom_highlight

        elif not self.edge_status[LEFT] and self.r_left_edge.collidepoint(pos):
            pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, self.r_left_highlight, width=0)
            self.highlighted_edge = self.r_left_highlight

        elif not self.edge_status[RIGHT] and self.r_right_edge.collidepoint(pos):
            pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, self.r_right_highlight, width=0)
            self.highlighted_edge = self.r_right_highlight

        else:
            # Since the pos is not on an edge, reset the highlighted edge if
            # the highlighted edge is set.
            if self.highlighted_edge:
                pygame.draw.rect(self.screen, self.bg_color, self.highlighted_edge, width=0)
                self.highlighted_edge = None

    def get_edge(self, pos):
        if self.r_top_edge.collidepoint(pos):
            return TOP

        elif self.r_bottom_edge.collidepoint(pos):
            return BOTTOM

        elif self.r_left_edge.collidepoint(pos):
            return LEFT

        elif self.r_right_edge.collidepoint(pos):
            return RIGHT

        else:
            return None

    def highlight_top_edge(self):
        pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, self.r_top_highlight, width=0)

    def highlight_bottom_edge(self):
        pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, self.r_bottom_highlight, width=0)

    def highlight_left_edge(self):
        pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, self.r_left_highlight, width=0)

    def highlight_right_edge(self):
        pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, self.r_right_highlight, width=0)

    def clear_highlighted_edge(self):
        if self.highlighted_edge:
            pygame.draw.rect(self.screen, WHITE, self.highlighted_edge, width=0)

    def set_edge(self, edge):
        if edge == TOP and not self.edge_status[TOP]:
            self.edge_status[TOP] = True
            pygame.draw.rect(self.screen, SET_COLOR, self.r_top_edge, width=0)
            self.neighbors.top.set_edge(BOTTOM)
        elif edge == BOTTOM and not self.edge_status[BOTTOM]:
            self.edge_status[BOTTOM] = True
            pygame.draw.rect(self.screen, SET_COLOR, self.r_bottom_edge, width=0)
            self.neighbors.bottom.set_edge(TOP)
        elif edge == LEFT and not self.edge_status[LEFT]:
            self.edge_status[LEFT] = True
            pygame.draw.rect(self.screen, SET_COLOR, self.r_left_edge, width=0)
            self.neighbors.left.set_edge(RIGHT)
        elif edge == RIGHT and not self.edge_status[RIGHT]:
            self.edge_status[RIGHT] = True
            pygame.draw.rect(self.screen, SET_COLOR, self.r_right_edge, width=0)
            self.neighbors.right.set_edge(LEFT)

    def __str__(self):
        return f'Cell {self.row}, {self.col} {self.topleft}'

    def __repr__(self):
        return f'Cell {self.row}, {self.col} {self.topleft}'
