import pygame as pg

from __init__ import *
from player import Player
from scorebox import Scorebox

pg.display.init()
screen = pg.display.set_mode((500, 500))
screen.fill(WHITE)
clock = pg.time.Clock()

# r1 = pg.Rect((0, 0), (100, 100))
# print(id(r1))
# r1.centerx = 200
# r1.centery = 200
# print(id(r1))
# pg.draw.rect(screen, RED, r1)

p = Player('Foobar', get_color())
sb = Scorebox((100, 100), p)
sb.draw()

pg.display.update()

while True:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            break

        clock.tick(30)
    
pg.quit()
