import pygame as pg
from pygame.constants import NOEVENT

from __init__ import *


class Button(pg.Rect):
    def __init__(self, text: str):
        self.color = BUTTON_COLOR
        self._text = FONT_16.render(text, True, BLACK)
        self._text_rect = self._text.get_rect()
        self._visible = True
        size = (
            self._text_rect.width + 16,
            self._text_rect.height + 16
        )
        super().__init__(pg.Rect(((0, 0), size)))
        self.screen = pg.display.get_surface()

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, val: bool) -> None:
        self._visible = val

    def draw(self) -> None:
        if self._visible:
            self._text_rect.center = self.center
            pg.draw.rect(self.screen, self.color, self, border_radius=3)
            self.screen.blit(self._text, self._text_rect)
            pg.display.update(self)

    def on_mouse_enter(self, pos) -> None:
        if self.collidepoint(pos):
            self.color = BUTTON_COLOR_HOVER
            self.draw()

    def on_mouse_down(self, pos) -> None:
        if self.collidepoint(pos):
            self.color = BUTTON_COLOR_DOWN
            self.draw()

    def on_mouse_up(self, pos) -> None:
        if self.collidepoint(pos):
            self.color = BUTTON_COLOR
            self.draw()

    def on_mouse_leave(self, pos) -> None:
        if not self.collidepoint(pos):
            self.color = BUTTON_COLOR
            self.draw()

    def __str__(self) -> str:
        return f'{type(self).__name__}: text={self._text}'

    def __repr__(self) -> str:
        return str(self)
