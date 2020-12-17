import pygame

import constants as c
from config import Config

GAP = 20


class Scoreboard(pygame.Rect):
    def __init__(self, rect, bg_color):
        super().__init__(rect)
        self.bg_color = bg_color
        self.config = Config()
        self.arrow = pygame.image.load('left-arrow-24.png')

        # Player 1
        self.p1_obox = pygame.Rect(self.x, self.y, self.width // 2, self.height)

        self.p1_text = c.FONT_LATO_REGULAR_20.render('Player 1', True, c.BLACK)
        self.p1_rect = self.p1_text.get_rect()

        self.p1_scorebox = pygame.Rect(0, 0, 40, self.p1_rect.height + 8)

        self.p1_ibox = pygame.Rect(0, 0, self.p1_rect.width + GAP + self.p1_scorebox.width, self.p1_scorebox.height)
        self.p1_ibox.center = self.p1_obox.center

        self.p1_rect.x = self.p1_ibox.x
        self.p1_rect.y = self.p1_ibox.center[1] - self.p1_rect.height // 2

        self.p1_scorebox.x = self.p1_ibox.topright[0] - self.p1_scorebox.width
        self.p1_scorebox.y = self.p1_ibox.y

        self.p1_score_text = c.FONT_LATO_REGULAR_20.render('0', True, c.BLACK)
        self.p1_score_rect = self.p1_score_text.get_rect()
        self.p1_score_rect.center = self.p1_scorebox.center

        self.p1_active_box = pygame.Rect(
            (self.p1_scorebox.topright[0] + 8, self.p1_scorebox.topright[1] + 4),
            (24, 24)
        )

        # Player 2
        self.p2_obox = pygame.Rect(self.center[0], self.y, self.width // 2, self.height)

        self.p2_text = c.FONT_LATO_REGULAR_20.render('Player 2', True, c.BLACK)
        self.p2_rect = self.p2_text.get_rect()

        self.p2_scorebox = pygame.Rect(0, 0, 40, self.p2_rect.height + 8)

        self.p2_ibox = pygame.Rect(0, 0, self.p2_rect.width + GAP + self.p2_scorebox.width, self.p2_scorebox.height)
        self.p2_ibox.center = self.p2_obox.center

        self.p2_rect.x = self.p2_ibox.x
        self.p2_rect.y = self.p2_ibox.center[1] - self.p2_rect.height // 2

        self.p2_scorebox.x = self.p2_ibox.topright[0] - self.p2_scorebox.width
        self.p2_scorebox.y = self.p2_ibox.y

        self.p2_score_text = c.FONT_LATO_REGULAR_20.render('0', True, c.BLACK)
        self.p2_score_rect = self.p2_score_text.get_rect()
        self.p2_score_rect.center = self.p2_scorebox.center

        self.p2_active_box = pygame.Rect(
            (self.p2_scorebox.topright[0] + 8, self.p2_scorebox.topright[1] + 4),
            (24, 24)
        )

    def draw(self):
        surf = pygame.display.get_surface()
        pygame.draw.rect(surf, self.bg_color, self)

        pygame.draw.rect(surf, self.bg_color, self.p1_obox)
        pygame.draw.rect(surf, self.bg_color, self.p1_ibox)
        pygame.draw.rect(surf, c.PLAYER1_COLOR, self.p1_scorebox)

        pygame.draw.rect(surf, self.bg_color, self.p2_obox)
        pygame.draw.rect(surf, self.bg_color, self.p2_ibox)
        pygame.draw.rect(surf, c.PLAYER2_COLOR, self.p2_scorebox)

        surf.blit(self.p1_text, self.p1_rect)
        surf.blit(self.p2_text, self.p2_rect)

        surf.blit(self.p1_score_text, self.p1_score_rect)
        surf.blit(self.p2_score_text, self.p2_score_rect)

        surf.blit(self.arrow, self.p1_active_box)

    def set_active_box(self, player):
        surf = pygame.display.get_surface()

        if player.name == c.PLAYER1:
            surf.blit(self.arrow, self.p1_active_box)
            pygame.draw.rect(surf, self.bg_color, self.p2_active_box)
        else:
            surf.blit(self.arrow, self.p2_active_box)
            pygame.draw.rect(surf, self.bg_color, self.p1_active_box)

    def update_p1_score(self, score):
        pass

    def update_p2_score(self, score):
        pass
