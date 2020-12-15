import pygame

import constants as c
from config import Config


class Cell(pygame.Rect):
    def __init__(self, rect, row, column, bg_color):
        super().__init__(rect)
        self.bg_color = bg_color
        self.row = row
        self.column = column
        self.config = Config()
        self.user = None
        self.is_captured = False
        self.is_dirty = False

        # Value is True if edge has been clicked, False otherwise
        self.edges = {c.TOP: False, c.BOTTOM: False, c.RIGHT: False, c.LEFT: False}
        self.top_edge_selection_area = pygame.Rect(
            self.x + self.config.dot_radius,
            self.y,
            self.width - 2 * self.config.dot_radius,
            self.config.dot_radius
        )

        self.bottom_edge_selection_area = pygame.Rect(
            self.x + self.config.dot_radius,
            self.y + self.height - self.config.dot_radius,
            self.width - 2 * self.config.dot_radius,
            self.config.dot_radius
        )

        self.left_edge_selection_area = pygame.Rect(
            self.x,
            self.y + self.config.dot_radius,
            self.config.dot_radius,
            self.height - 2 * self.config.dot_radius
        )

        self.right_edge_selection_area = pygame.Rect(
            self.x + self.width - self.config.dot_radius,
            self.y + self.config.dot_radius,
            self.config.dot_radius,
            self.height - 2 * self.config.dot_radius
        )

    def draw(self):
        surf = pygame.display.get_surface()
        pygame.draw.rect(surf, self.bg_color, self)

        if self.edges[c.TOP]:
            # Draw selected top edge
            pygame.draw.line(surf, c.BLUE, (self.x, self.y), (self.x + self.width, self.y), width=self.config.dot_radius)
        else:
            # Draw faint top line
            pygame.draw.line(surf, c.GRAY, (self.x, self.y), (self.x + self.width, self.y))

        if self.edges[c.LEFT]:
            # Draw selected left edge
            pygame.draw.line(surf, c.BLUE, (self.x, self.y), (self.x, self.y + self.height), width=self.config.dot_radius)
        else:
            # Draw faint left line
            pygame.draw.line(surf, c.GRAY, (self.x, self.y), (self.x, self.y + self.height))

        if self.edges[c.RIGHT]:
            # Draw selected right edge
            pygame.draw.line(surf, c.BLUE, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), width=self.config.dot_radius)
        else:
            # Draw faint right line
            pygame.draw.line(surf, c.GRAY, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height))

        if self.edges[c.BOTTOM]:
            # Draw selected bottom edge
            pygame.draw.line(surf, c.BLUE, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), width=self.config.dot_radius)
        else:
            # Draw faint bottom line
            pygame.draw.line(surf, c.GRAY, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height))

        # Draw top left dot
        pygame.draw.circle(surf, c.BLACK, self.topleft, self.config.dot_radius)
        # Draw top right dot
        pygame.draw.circle(surf, c.BLACK, self.topright, self.config.dot_radius)
        # Draw bottom left dot
        pygame.draw.circle(surf, c.BLACK, self.bottomleft, self.config.dot_radius)
        # Draw bottom right dot
        pygame.draw.circle(surf, c.BLACK, self.bottomright, self.config.dot_radius)

        self.is_dirty = False

    def get_clicked_edge(self, x, y):
        clicked_edge = None

        if self.is_in_rect(x, y, self.top_edge_selection_area):
            clicked_edge = c.TOP

        elif self.is_in_rect(x, y, self.bottom_edge_selection_area):
            clicked_edge = c.BOTTOM

        elif self.is_in_rect(x, y, self.left_edge_selection_area):
            clicked_edge = c.LEFT

        elif self.is_in_rect(x, y, self.right_edge_selection_area):
            clicked_edge = c.RIGHT

        return clicked_edge

    def set_clicked_edge(self, edge):
        if self.edges[edge] == False:
            self.edges[edge] = True
            self.is_dirty = True

    def is_in_rect(self, x, y, rect):
        if rect.x <= x < rect.x + rect.width and rect.y <= y < rect.y + rect.height:
            return True
        return False

    def __str__(self):
        return f'Cell [{self.row}, {self.column}]'
