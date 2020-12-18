from collections import namedtuple
import math

import pygame

from __init__ import *


Neighbors = namedtuple('Neighbors', ['top', 'bottom', 'left', 'right'])


class Shape(pygame.Rect):
    def __init__(self, origin, size, row, col, typ, bg_color):
        super().__init__(origin, size)
        self.row = row
        self.col = col
        self.typ = typ
        self.bg_color = bg_color
        self.screen = pygame.display.get_surface()

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self)

    def __str__(self):
        return f'{type(self).__name__} ({self.typ}) {self.row}, {self.col} {self.topleft}'

    def __repr__(self):
        return f'{type(self).__name__} ({self.typ}) {self.row}, {self.col} {self.topleft}'
