from __init__ import *
from entity import Entity
from player import Player


class Cell(Entity):
    def __init__(self, origin: tuple, size: tuple, row: int, col: int, bg_color: pygame.Color):
        super().__init__(origin, size, row, col, bg_color)
        self.is_captured = False
        self.captured_by = None
        self.edge_top = None
        self.edge_bottom = None
        self.edge_left = None
        self.edge_right = None

    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.bg_color, self)
        pygame.display.update(self)

    def check_for_capture(self, player: Player) -> bool:
        if self.edge_top.is_activated and self.edge_bottom.is_activated \
            and self.edge_left.is_activated and self.edge_right.is_activated:
            self.is_captured = True
            self.captured_by = player
            self.bg_color = player.color
            self.draw()
            return True
        return False
