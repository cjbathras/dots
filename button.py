"""A general button implementation."""

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

BUTTON_NORMAL = 'normal'
BUTTON_HOVER = 'hover'
BUTTON_DOWN = 'down'


class Button:
    """A button that a user can click that performs a function."""
    def __init__(self, pos: tuple, size: tuple, callback: callable=None,
            font: pg.font.Font=FONT_16, text: str='', visible: bool=True,
            text_color: pg.Color=WHITE, radius: int=3):
        self._button_down = False
        self._pos = pos
        self._size = size
        self._callback = callback
        self._font = font
        self._text = text
        self._visible = visible
        self._text_color = text_color
        self._radius = radius
        self._screen = pg.display.get_surface()
        self._state = BUTTON_NORMAL

        self._surf = pg.Surface(size)
        self._surf.set_colorkey(COLORKEY)

    @property
    def visible(self) -> bool:
        """Get the button visibility."""
        return self._visible

    @visible.setter
    def visible(self, val: bool) -> None:
        """Set the button visibility."""
        self._visible = val

    def draw(self) -> None:
        """Draw the button on the screen."""
        if self._visible:
            # Get the button's surface and draw a rectangle on it
            self._rect = self._surf.get_rect()
            if self._state == BUTTON_NORMAL:
                pg.draw.rect(self._surf, BUTTON_COLOR, self._rect,
                    border_radius=self._radius)
            elif self._state == BUTTON_HOVER:
                pg.draw.rect(self._surf, BUTTON_COLOR_HOVER, self._rect,
                    border_radius=self._radius)
                pg.draw.rect(self._surf, BUTTON_COLOR_DOWN, self._rect,
                    border_radius=self._radius, width=2)
            else:
                pg.draw.rect(self._surf, BUTTON_COLOR_DOWN, self._rect,
                    border_radius=self._radius)

            # Render the text in the font and center it in the button's
            # rectangle
            self._text_surf = self._font.render(
                self._text, True, self._text_color)
            self._text_rect = self._text_surf.get_rect()
            self._text_rect.center = self._rect.center

            # Finally, position self._rect at the desired position (MUST be done
            # after all of the drawing above)
            self._rect.topleft = self._pos

            # Blit the text onto the button surface
            self._surf.blit(self._text_surf, self._text_rect)
            # Blit the button rectangle onto the screen
            self._screen.blit(self._surf, self._rect)
            pg.display.update(self._rect)

    def handle_event(self, event: pg.event) -> None:
        """Handle the mouse events."""
        if self._visible:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self._rect.collidepoint(event.pos):
                    self._button_down = True
                    self._state = BUTTON_DOWN

            elif event.type == pg.MOUSEMOTION:
                collided = self._rect.collidepoint(event.pos)
                if collided and not self._button_down:
                    self._state = BUTTON_HOVER
                elif not collided:
                    self._state = BUTTON_NORMAL

            elif event.type == pg.MOUSEBUTTONUP:
                if self._rect.collidepoint(event.pos):
                    if self._callback:
                        self._callback()
                    self._state = BUTTON_HOVER
                self._button_down = False

            self.draw()

    def __str__(self) -> str:
        return f'{type(self).__name__}: text={self._text}'

    def __repr__(self) -> str:
        return str(self)
