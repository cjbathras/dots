import pygame

import constants as c
from config import Config


class Cell(pygame.Rect):
    def __init__(self, rect, row, column, bg_color):
        super().__init__(rect)
        self.bg_color = bg_color
        self.row = row
        self.column = column
        self._config = Config()
        self._user = None
        self.is_captured = False
        self.is_dirty = False

        # Value is True if edge has been clicked, False otherwise
        self._edges = {c.TOP: False, c.BOTTOM: False, c.RIGHT: False, c.LEFT: False}
        self._top_edge_selection_area = pygame.Rect(
            self.x + self._config.dot_radius,
            self.y,
            self.width - 2 * self._config.dot_radius,
            self._config.dot_radius
        )

        self._bottom_edge_selection_area = pygame.Rect(
            self.x + self._config.dot_radius,
            self.y + self.height - self._config.dot_radius,
            self.width - 2 * self._config.dot_radius,
            self._config.dot_radius
        )

        self._left_edge_selection_area = pygame.Rect(
            self.x,
            self.y + self._config.dot_radius,
            self._config.dot_radius,
            self.height - 2 * self._config.dot_radius
        )

        self._right_edge_selection_area = pygame.Rect(
            self.x + self.width - self._config.dot_radius,
            self.y + self._config.dot_radius,
            self._config.dot_radius,
            self.height - 2 * self._config.dot_radius
        )

    def draw(self):
        surf = pygame.display.get_surface()
        pygame.draw.rect(surf, self.bg_color, self)

        if self._edges[c.TOP]:
            # Draw selected top edge
            pygame.draw.line(surf, c.BLUE, (self.x, self.y), (self.x + self.width, self.y), width=self._config.dot_radius)
        else:
            # Draw faint top line
            pygame.draw.line(surf, c.GRAY, (self.x, self.y), (self.x + self.width, self.y))

        if self._edges[c.LEFT]:
            # Draw selected left edge
            pygame.draw.line(surf, c.BLUE, (self.x, self.y), (self.x, self.y + self.height), width=self._config.dot_radius)
        else:
            # Draw faint left line
            pygame.draw.line(surf, c.GRAY, (self.x, self.y), (self.x, self.y + self.height))

        if self._edges[c.RIGHT]:
            # Draw selected right edge
            pygame.draw.line(surf, c.BLUE, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), width=self._config.dot_radius)
        else:
            # Draw faint right line
            pygame.draw.line(surf, c.GRAY, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height))

        if self._edges[c.BOTTOM]:
            # Draw selected bottom edge
            pygame.draw.line(surf, c.BLUE, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), width=self._config.dot_radius)
        else:
            # Draw faint bottom line
            pygame.draw.line(surf, c.GRAY, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height))

        # Draw top left dot
        pygame.draw.circle(surf, c.BLACK, self.topleft, self._config.dot_radius)
        # Draw top right dot
        pygame.draw.circle(surf, c.BLACK, self.topright, self._config.dot_radius)
        # Draw bottom left dot
        pygame.draw.circle(surf, c.BLACK, self.bottomleft, self._config.dot_radius)
        # Draw bottom right dot
        pygame.draw.circle(surf, c.BLACK, self.bottomright, self._config.dot_radius)

        self.is_dirty = False

    def get_clicked_edge(self, x, y):
        clicked_edge = None

        if self.is_in_rect(x, y, self._top_edge_selection_area):
            clicked_edge = c.TOP

        elif self.is_in_rect(x, y, self._bottom_edge_selection_area):
            clicked_edge = c.BOTTOM

        elif self.is_in_rect(x, y, self._left_edge_selection_area):
            clicked_edge = c.LEFT

        elif self.is_in_rect(x, y, self._right_edge_selection_area):
            clicked_edge = c.RIGHT

        return clicked_edge

    def set_clicked_edge(self, edge):
        if self._edges[edge] == False:
            self._edges[edge] = True
            self.is_dirty = True

    def is_in_rect(self, x, y, rect):
        if rect.x <= x < rect.x + rect.width and rect.y <= y < rect.y + rect.height:
            return True
        return False

    def __str__(self):
        return f'Cell [{self.row}, {self.column}]'
