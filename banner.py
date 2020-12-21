import pygame as pg

from __init__ import *
from player import Player


class Banner(pg.Rect):
    def __init__(self, rect: pg.Rect, bg_color: pg.Color):
        super().__init__(rect)
        self.bg_color = bg_color
        self.screen = pg.display.get_surface()

        self.center = (self.screen.get_width() // 2,
            self.screen.get_height() // 2)

    def draw(self, winner: Player) -> None:
        # Create the message text
        msg = f'{winner[0].name} Wins!' if len(winner) == 1 else "It's a TIE!"
        text = FONT_20.render(msg, True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = self.center

        # Draw the shapes
        pg.draw.rect(self.screen, self.bg_color, self)
        pg.draw.rect(self.screen, DARK_GRAY, self, width=1)

        # Blit the text to the screen
        self.screen.blit(text, text_rect)

        pg.display.update(self)

    def clear(self) -> None:
        pg.draw.rect(self.screen, BACKGROUND_COLOR, self)

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
