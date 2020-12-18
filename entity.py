from abc import ABCMeta, abstractmethod
# from collections import namedtuple

import pygame

from __init__ import *


# Neighbors = namedtuple('Neighbors', ['top', 'bottom', 'left', 'right'])


class Entity(pygame.Rect, metaclass=ABCMeta):
    def __init__(self, origin, size, row, col, bg_color):
        super().__init__(origin, size)
        self.row = row
        self.col = col
        self.bg_color = bg_color
        self.screen = pygame.display.get_surface()

    @abstractmethod
    def draw(self): pass

    def __str__(self):
        return f'{self.__class__.__name__} [{self.row},{self.col}] origin={self.topleft} size={self.size}'

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.row},{self.col}] origin={self.topleft} size={self.size}'
