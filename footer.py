import pygame

from __init__ import *
from player import Player


class Footer(pygame.Rect):
    def __init__(self, rect: pygame.Rect, bg_color: pygame.Color):
        super().__init__(rect)
        self.bg_color = bg_color
        self.screen = pygame.display.get_surface()

        self.play_again_text = \
            FONT_LATO_LIGHT_14.render('Play again?', True, BLACK)
        self.play_again_text_rect = self.play_again_text.get_rect()
        self.play_again_button = pygame.Rect(
            (0,0), 
            (self.play_again_text_rect.width + 10, 
            self.play_again_text_rect.height + 10)
        )
        self.play_again_button.bottomright = (self.right - 10, self.bottom - 10)
        self.play_again_text_rect.topleft = \
            (self.play_again_button.left + 5, self.play_again_button.top + 5)

    def draw(self, winner: Player) -> None:
        # Create the message text
        msg = f'{winner[0].name} Wins!' if len(winner) == 1 else "It's a TIE!"
        text = FONT_LATO_REGULAR_20.render(msg, True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = self.center

        # Draw the shapes
        pygame.draw.rect(self.screen, self.bg_color, self)
        pygame.draw.rect(self.screen, DARK_GRAY, self, width=1)
        pygame.draw.rect(self.screen, BUTTON_COLOR, self.play_again_button)

        # Blit the text to the screen
        self.screen.blit(text, text_rect)
        self.screen.blit(self.play_again_text, self.play_again_text_rect)

        pygame.display.update(self)

    def clear(self) -> None:
        pygame.draw.rect(self.screen, BACKGROUND_COLOR, self)

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
        