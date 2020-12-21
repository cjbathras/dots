import pygame
from pygame.constants import NOEVENT

from __init__ import *


class Button(pygame.Rect):
    def __init__(self, text: str):
        self.color = BUTTON_COLOR
        self._text = FONT_LATO_LIGHT_14.render(text, True, BLACK)
        self._text_rect = self._text.get_rect()
        size = (
            self._text_rect.width + 16,
            self._text_rect.height + 16
        )
        super().__init__(pygame.Rect(((0, 0), size)))
        self.screen = pygame.display.get_surface()

    def draw(self) -> None:
        self._text_rect.center = self.center
        pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self._text, self._text_rect)
        pygame.display.update(self)
    
    def mouse_hover(self) -> None:
        self.color = BUTTON_COLOR_HOVER
        self.draw()
        
    def __str__(self) -> str:
        return f'{type(self).__name__}: text={self._text}'

    def __repr__(self) -> str:
        return str(self)
