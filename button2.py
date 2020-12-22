import pygame as pg

from __init__ import *


class Button(pg.Surface):
    def __init__(self, pos, size, callback=None, font=FONT_16, text='',
                text_color=BLACK, radius=3):
        super().__init__(size)
        self.set_colorkey(COLORKEY)
        self._button_down = False
        self._pos = pos
        self._callback = callback
        self._font = font
        self._text = text
        self._text_color = text_color
        self._radius = radius
        self._screen = pg.display.get_surface()

        # Get the button's surface and draw a rectangle on it
        self._rect = self.get_rect()
        pg.draw.rect(self, BUTTON_COLOR, self._rect, border_radius=self._radius)

        # Render the text in the font and center it in the button's rectangle
        self._text_surf = self._font.render(self._text, True, self._text_color)
        self._text_rect = self._text_surf.get_rect(center=self._rect.center)

        # Set the position of the button to the specified pos
        self._rect.topleft = self._pos
        # # Blit the text onto the button surface
        # self.blit(self._text_surf, self._text_rect)
        # # Blit the button rectangle onto the screen
        # self._screen.blit(self, self._rect)

    def draw(self):
        # Blit the text onto the button surface
        self.blit(self._text_surf, self._text_rect)
        # Blit the button rectangle onto the screen
        self._screen.blit(self, self._rect)
        pg.display.update(self._rect)

        # # Set the currently active image
        # # image and rect attributes are defined in Sprite base class
        # self.image = self._image_normal_surf
        # self.rect = self.image.get_rect(topleft=pos)

        # # Render the text in the center of the button
        # image_center = self.image.get_rect().center
        # text_surf = font.render(text, True, text_color)
        # text_rect = text_surf.get_rect(center=image_center)

        # # Blit the text onto the images
        # for image in (self._image_normal_surf, self._image_hover_surf,
        #             self._image_down_surf):
        #     image.blit(text_surf, text_rect)

    def handle_event(self, event):
    #     if event.type == pg.MOUSEBUTTONDOWN:
    #         if self.rect.collidepoint(event.pos):
    #             self.image = self._image_down_surf
    #             self._button_down = True

    #     elif event.type == pg.MOUSEBUTTONUP:
    #         if self.rect.collidepoint(event.pos) and self._button_down:
    #             if self._callback:
    #                 self._callback()
    #             self.image = self._image_hover_surf
    #         self._button_down = False

        if event.type == pg.MOUSEMOTION:
            collided = self._rect.collidepoint(event.pos)
            if collided and not self._button_down:
                print(f'hovering over: {self}')
            # elif not collided:
            #     self.image = self._image_normal_surf

    def __str__(self) -> str:
        return f'{type(self).__name__}: text={self._text}'

    def __repr__(self) -> str:
        return str(self)
