import pygame as pg
from pygame.locals import *
from __init__ import *
from button2 import Button

pg.display.init()
pg.display.set_caption('Test')
pg.font.init()

screen = pg.display.set_mode((500, 500))
screen.fill(WHITE)
pg.display.update()



button1 = Button((10, 10), (50, 30), text='foo')
button2 = Button((10, 100), (50, 30), text='bar')
buttons = [button1, button2]



run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        elif event.type == pg.MOUSEMOTION:
            for b in buttons:
                b.handle_event(event)
                b.draw()

        elif event.type == pg.MOUSEBUTTONDOWN:
            for b in buttons:
                b.handle_event(event)
                b.draw()

        elif event.type == pg.MOUSEBUTTONUP:
            for b in buttons:
                b.handle_event(event)
                b.draw()
