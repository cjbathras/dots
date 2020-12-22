import pygame as pg

from __init__ import *


class Button:
    def __init__(self, pos, size, callback=None, font=FONT_16, text='',
                text_color=WHITE, radius=3):
        self._size = size
        self._button_down = False
        self._pos = pos
        self._callback = callback
        self._font = font
        self._text = text
        self._text_color = text_color
        self._radius = radius
        self._screen = pg.display.get_surface()

        self._surf_normal = pg.Surface(size)
        self._surf_normal.set_colorkey(COLORKEY)
        self._surf_hover = pg.Surface(size)
        self._surf_hover.set_colorkey(COLORKEY)
        self._surf_down = pg.Surface(size)
        self._surf_down.set_colorkey(COLORKEY)
        self._surf_active = self._surf_normal

        self.draw()

    def draw(self):
        # Get the button's surface and draw a rectangle on it
        self._rect = self._surf_active.get_rect()
        pg.draw.rect(self._surf_active, BUTTON_COLOR, self._rect, border_radius=self._radius)
        pg.draw.rect(self._surf_hover, BUTTON_COLOR_HOVER, self._rect, border_radius=self._radius)
        pg.draw.rect(self._surf_hover, BUTTON_COLOR_DOWN, self._rect, border_radius=self._radius, width=2)
        pg.draw.rect(self._surf_down, BUTTON_COLOR_DOWN, self._rect, border_radius=self._radius)

        # Render the text in the font and center it in the button's rectangle
        self._text_surf = self._font.render(self._text, True, self._text_color)
        self._text_rect = self._text_surf.get_rect()
        self._text_rect.center = self._rect.center

        # Finally, position self._rect at the desired position (MUST be done
        # after all of the drawing above)
        self._rect.topleft = self._pos

        # Blit the text onto the button surface
        self._surf_active.blit(self._text_surf, self._text_rect)
        # Blit the button rectangle onto the screen
        self._screen.blit(self._surf_active, self._rect)
        pg.display.update(self._rect)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(event.pos):
                self._surf_active = self._surf_down
                self._button_down = True

        elif event.type == pg.MOUSEMOTION:
            collided = self._rect.collidepoint(event.pos)
            if collided and not self._button_down:
                self._surf_active = self._surf_hover
            elif not collided:
                self._surf_active = self._surf_normal

        elif event.type == pg.MOUSEBUTTONUP:
            if self._rect.collidepoint(event.pos):
                if self._callback:
                    self._callback()
                self._surf_active = self._surf_hover
            self._button_down = False

    def __str__(self) -> str:
        return f'{type(self).__name__}: text={self._text}'

    def __repr__(self) -> str:
        return str(self)
