from __init__ import *
from entity import Entity


class Edge(Entity):
    def __init__(self, origin, size, row, col, bg_color):
        super().__init__(origin, size, row, col, bg_color)
        self.is_activated = False
        self.cell1 = None
        self.cell2 = None

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self)
        pygame.display.update(self)

    def highlight(self):
        if not self.is_activated:
            pygame.draw.rect(self.screen, EDGE_COLOR_ACTIVATED, self, width=1)
            pygame.display.update(self)

    def clear(self):
        self.draw()

    def activate(self):
        if not self.is_activated:
            self.is_activated = True
            self.bg_color = EDGE_COLOR_ACTIVATED
            self.draw()
            return True
        return False
