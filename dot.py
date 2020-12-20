from __init__ import *
from entity import Entity


class Dot(Entity):
    def __init__(self, origin: tuple, size: tuple, row: int, col: int, bg_color: pygame.Color):
        super().__init__(origin, size, row, col, bg_color)

    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.bg_color, self)
        pygame.display.update(self)
