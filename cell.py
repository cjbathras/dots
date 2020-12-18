from __init__ import *
from entity import Entity


class Cell(Entity):
    def __init__(self, origin, size, row, col, bg_color):
        super().__init__(origin, size, row, col, bg_color)
        self.is_captured = False
        self.captured_by = None
        self.edge_top = None
        self.edge_bottom = None
        self.edge_left = None
        self.edge_right = None

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self)
        pygame.display.update(self)

    def check_for_capture(self, player):
        if self.edge_top.is_activated and self.edge_bottom.is_activated \
            and self.edge_left.is_activated and self.edge_right.is_activated:
            self.is_captured = True
            self.captured_by = player
            self.bg_color = player.color
            player.increment_captured_cells()
            self.draw()
            return True
        return False
