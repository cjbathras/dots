import pygame as pg

from __init__ import *

# Default button images/pygame.Surfaces.
IMAGE_NORMAL = pg.Surface((100, 32))
IMAGE_NORMAL.fill(BUTTON_COLOR)
IMAGE_HOVER = pg.Surface((100, 32))
IMAGE_HOVER.fill(BUTTON_COLOR_HOVER)
IMAGE_DOWN = pg.Surface((100, 32))
IMAGE_DOWN.fill(BUTTON_COLOR_DOWN)


# Button is a sprite subclass, that means it can be added to a sprite group
# You can draw and update all sprites in a group by calling group.update() and
# group.draw(screen)
class Button(pg.sprite.Sprite):
    def __init__(self, pos, size, callback, font=FONT_16, text='',
                text_color=BLACK, image_normal=IMAGE_NORMAL,
                image_hover=IMAGE_HOVER, image_down=IMAGE_DOWN):
        super().__init__()

        # Scale the images to the desired size (doesn't modify the originals)
        self._image_normal_surf = pg.transform.scale(image_normal, size)
        self._image_hover_surf = pg.transform.scale(image_hover, size)
        self._image_down_surf = pg.transform.scale(image_down, size)

        # Set the currently active image
        # image and rect attributes are defined in Sprite base class
        self.image = self._image_normal_surf
        self.rect = self.image.get_rect(topleft=pos)

        # Render the text in the center of the button
        image_center = self.image.get_rect().center
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=image_center)

        # Blit the text onto the images
        for image in (self._image_normal_surf, self._image_hover_surf,
                    self._image_down_surf):
            image.blit(text_surf, text_rect)

        # This function will be called when the button gets pressed
        self._callback = callback
        self._button_down = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.image = self._image_down_surf
                self._button_down = True

        elif event.type == pg.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos) and self._button_down:
                if self._callback:
                    self._callback()
                self.image = self._image_hover_surf
            self._button_down = False

        elif event.type == pg.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self._button_down:
                self.image = self._image_hover_surf
            elif not collided:
                self.image = self._image_normal_surf
