import pygame as pg
from pygame.constants import NOEVENT

from __init__ import *


class Button(pg.Rect):
    def __init__(self, pos: tuple, size: tuple, text: str='', 
            callback: callable=None):
        super().__init__(pg.Rect(pos, size))
        self._color = BUTTON_COLOR
        self._text = FONT_16.render(text, True, BLACK)
        self._text_rect = self._text.get_rect()
        self._text_rect.center = self.center
        self._visible = True
        self.screen = pg.display.get_surface()
        
        pg.draw.rect(self.screen, self._color, self, border_radius=3)

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, val: bool) -> None:
        self._visible = val

    def draw(self) -> None:
        if self._visible:
            self.screen.blit(self._text, self._text_rect)
            pg.display.update(self)

    def on_mouse_enter(self, pos) -> None:
        if self.collidepoint(pos):
            self._color = BUTTON_COLOR_HOVER
            self.draw()

    def on_mouse_down(self, pos) -> None:
        if self.collidepoint(pos):
            self._color = BUTTON_COLOR_DOWN
            self.draw()

    def on_mouse_up(self, pos) -> None:
        if self.collidepoint(pos):
            self._color = BUTTON_COLOR
            self.draw()

    def on_mouse_leave(self, pos) -> None:
        if not self.collidepoint(pos):
            self._color = BUTTON_COLOR
            self.draw()

    def __str__(self) -> str:
        return f'{type(self).__name__}: text={self._text}'

    def __repr__(self) -> str:
        return str(self)
