import pygame

from __init__ import *


class Button(pygame.Rect):
    def __init__(self, pos: tuple, size: tuple, text: str):
        super().__init__(pygame.Rect(pos, size):
        self._text = text
