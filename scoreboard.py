import pygame

from __init__ import *
from game import Game
from player import Player

GAP = 20


class Scoreboard(pygame.Rect):
    def __init__(self, rect: pygame.Rect, bg_color: pygame.Color, game: Game):
        super().__init__(rect)
        self.bg_color = bg_color
        self.arrow = pygame.image.load('left-arrow-24.png')
        self.screen = pygame.display.get_surface()
        self.active_boxes = {}
        self.game = game

        # Player 1
        self.p1_obox = pygame.Rect(self.x, self.y, self.width // 2, self.height)

        self.p1_text = FONT_LATO_REGULAR_20.render(self.game.players[0].name, True, BLACK)
        self.p1_text_rect = self.p1_text.get_rect()

        self.p1_scorebox = pygame.Rect(0, 0, 40, self.p1_text_rect.height + 8)

        self.p1_ibox = pygame.Rect(0, 0, self.p1_text_rect.width + GAP + self.p1_scorebox.width, self.p1_scorebox.height)
        self.p1_ibox.center = self.p1_obox.center

        self.p1_text_rect.x = self.p1_ibox.x
        self.p1_text_rect.y = self.p1_ibox.center[1] - self.p1_text_rect.height // 2

        self.p1_scorebox.x = self.p1_ibox.topright[0] - self.p1_scorebox.width
        self.p1_scorebox.y = self.p1_ibox.y

        self.p1_score_text = FONT_LATO_REGULAR_20.render(f'{self.game.get_score(self.game.players[0])}', True, BLACK)
        self.p1_score_rect = self.p1_score_text.get_rect()
        self.p1_score_rect.center = self.p1_scorebox.center

        self.p1_active_box = pygame.Rect(
            (self.p1_scorebox.topright[0] + 4, self.p1_scorebox.topright[1] + 4),
            (24, 24)
        )

        # Player 2
        self.p2_obox = pygame.Rect(self.center[0], self.y, self.width // 2, self.height)

        self.p2_text = FONT_LATO_REGULAR_20.render(self.game.players[1].name, True, BLACK)
        self.p2_text_rect = self.p2_text.get_rect()

        self.p2_scorebox = pygame.Rect(0, 0, 40, self.p2_text_rect.height + 8)

        self.p2_ibox = pygame.Rect(0, 0, self.p2_text_rect.width + GAP + self.p2_scorebox.width, self.p2_scorebox.height)
        self.p2_ibox.center = self.p2_obox.center

        self.p2_text_rect.x = self.p2_ibox.x
        self.p2_text_rect.y = self.p2_ibox.center[1] - self.p2_text_rect.height // 2

        self.p2_scorebox.x = self.p2_ibox.topright[0] - self.p2_scorebox.width
        self.p2_scorebox.y = self.p2_ibox.y

        self.p2_score_text = FONT_LATO_REGULAR_20.render(f'{self.game.get_score(self.game.players[0])}', True, BLACK)
        self.p2_score_rect = self.p2_score_text.get_rect()
        self.p2_score_rect.center = self.p2_scorebox.center

        self.p2_active_box = pygame.Rect(
            (self.p2_scorebox.topright[0] + 4, self.p2_scorebox.topright[1] + 4),
            (24, 24)
        )

        # TODO: for more than two players you'll have to iterate over the list of
        #       players and active box rects to do this assignment
        # TODO: refactor to create a class for each player scorebox
        self.active_boxes[self.game.players[0]] = self.p1_active_box
        self.active_boxes[self.game.players[1]] = self.p2_active_box
        self.prev_player = self.game.players[0]
        self.prev_active_box = self.p1_active_box

    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.bg_color, self.p1_obox)
        pygame.draw.rect(self.screen, self.bg_color, self.p1_ibox)
        pygame.draw.rect(self.screen, self.game.players[0].color , self.p1_scorebox)

        pygame.draw.rect(self.screen, self.bg_color, self.p2_obox)
        pygame.draw.rect(self.screen, self.bg_color, self.p2_ibox)
        pygame.draw.rect(self.screen, self.game.players[1].color, self.p2_scorebox)

        self.screen.blit(self.p1_text, self.p1_text_rect)
        self.screen.blit(self.p2_text, self.p2_text_rect)

        self.screen.blit(self.p1_score_text, self.p1_score_rect)
        self.screen.blit(self.p2_score_text, self.p2_score_rect)

        self.screen.blit(self.arrow, self.p1_active_box)

        pygame.draw.rect(self.screen, GRAY, self, width=1)

        pygame.display.update(self)

    def set_active_box(self, player: Player) -> None:
        self.screen.blit(self.arrow, self.active_boxes[player])
        pygame.draw.rect(self.screen, self.bg_color, self.prev_active_box)
        pygame.display.update(self.active_boxes[player])
        pygame.display.update(self.prev_active_box)
        self.prev_active_box = self.active_boxes[player]

    def update_score(self, player: Player) -> None:
        if player == self.game.players[0]:
            pygame.draw.rect(self.screen, self.game.players[0].color, self.p1_scorebox)
            self.p1_score_text = FONT_LATO_REGULAR_20.render(f'{self.game.get_score(player)}', True, BLACK)
            self.p1_score_rect = self.p1_score_text.get_rect()
            self.p1_score_rect.center = self.p1_scorebox.center
            self.screen.blit(self.p1_score_text, self.p1_score_rect)
            pygame.display.update(self.p1_score_rect)

        else:
            pygame.draw.rect(self.screen, self.game.players[1].color, self.p2_scorebox)
            self.p2_score_text = FONT_LATO_REGULAR_20.render(f'{self.game.get_score(player)}', True, BLACK)
            self.p2_score_rect = self.p2_score_text.get_rect()
            self.p2_score_rect.center = self.p2_scorebox.center
            self.screen.blit(self.p2_score_text, self.p2_score_rect)
            pygame.display.update(self.p2_score_rect)
