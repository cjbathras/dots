import pygame

from __init__ import *

class Footer(pygame.Rect):
    def __init__(self, rect, bg_color):
        super().__init__(rect)
        self.bg_color = bg_color
        self.screen = pygame.display.get_surface()

    def draw(self, winner):
        msg = f'{winner[0].name} Wins!' if len(winner) == 1 else "It's a TIE!"
        text = FONT_LATO_REGULAR_20.render(msg, True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = self.center

        pygame.draw.rect(self.screen, self.bg_color, self)
        pygame.draw.rect(self.screen, DARK_GRAY, self, width=1)
        self.screen.blit(text, text_rect)

        pygame.display.update(self)
