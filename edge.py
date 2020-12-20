from __init__ import *
from config import Config
from entity import Entity


class Edge(Entity):
    def __init__(self, origin: tuple, size: tuple, row: int, col: int, bg_color: pygame.Color):
        super().__init__(origin, size, row, col, bg_color)
        self.cfg = Config()
        self.is_activated = False
        self.cell1 = None
        self.cell2 = None

    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.bg_color, self)
        pygame.display.update(self)

    def highlight(self) -> None:
        if not self.is_activated:
            pygame.draw.rect(self.screen, self.cfg.EDGE_COLOR_ACTIVATED, self, width=1)
            pygame.display.update(self)

    def clear(self) -> None:
        self.draw()

    def activate(self) -> None:
        if not self.is_activated:
            self.is_activated = True
            self.bg_color = self.cfg.EDGE_COLOR_ACTIVATED
            self.draw()
            return True
        return False
