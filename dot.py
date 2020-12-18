from __init__ import *
from entity import Entity


class Dot(Entity):
    def __init__(self, origin, size, row, col, bg_color):
        super().__init__(origin, size, row, col, bg_color)

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self)
        pygame.display.update(self)
