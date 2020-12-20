import pygame

from __init__ import *


class Button(pygame.Rect):
    def __init__(self, pos: tuple, size: tuple, text: str):
        super().__init__(pygame.Rect(pos, size))
        self._text = text
        
    def __str__(self) -> str:
        return f'{type(self).__name__}: text={self._text}'

    def __repr__(self) -> str:
        return str(self)
