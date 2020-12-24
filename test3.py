import pygame as pg

from __init__ import *

cw = 100
ch = 100
dd = 10
rows = 4
cols = 4

pg.display.init()
screen = pg.display.set_mode((cw*cols + dd*(cols+1), ch*rows + dd*(rows+1)))
# screen = pg.display.set_mode((1000, 1000))
screen.fill(WHITE)
clock = pg.time.Clock()

dots = []
for r in range(0, rows + 1):
    row = []
    for c in range(0, cols + 1):
        rect = pg.Rect(
            (dd + cw) * c, 
            (dd + ch) * r, 
            dd, dd
        )
        row.append(rect)
        pg.draw.rect(screen, BLACK, rect)
    dots.append(row)

edges = []
for r in range(0, rows * 2 + 1):
    row = []
    for c in range(0, cols + 1):
        if is_even(r) and c < cols:
            rect = pg.Rect(
                (c + 1) * dd + c * cw,
                r // 2 * dd + r // 2 * ch, 
                cw, dd
            )
            row.append(rect)
            pg.draw.rect(screen, RED, rect)
        elif is_odd(r):
            rect = pg.Rect(
                c * dd + c * cw, 
                (r + 1) // 2 * dd + r // 2 * ch, 
                dd, ch
            )
            row.append(rect)
            pg.draw.rect(screen, RED, rect)
    edges.append(row)

cells = []
for r in range(0, rows):
    row = []
    for c in range(0, cols):
        rect = pg.Rect(
            (c + 1) * dd + c * cw, 
            (r + 1) * dd + r * ch, 
            cw, ch
        )
        row.append(rect)
        pg.draw.rect(screen, GREEN, rect)
    cells.append(row)





pg.display.flip()

while True:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            break

        clock.tick(30)

pg.quit()
