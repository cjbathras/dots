import pygame as pg

from __init__ import *

cw = 100
ch = 100
dd = 10
rows = 3
cols = 3
gutter = 20
x_shift = 0
y_shift = 100

pg.display.init()
screen = pg.display.set_mode(
    (cw*cols + dd*(cols+1) + gutter*2 + x_shift, 
    ch*rows + dd*(rows+1) + gutter*2 + y_shift)
)
# screen = pg.display.set_mode((1000, 1000))
screen.fill(WHITE)
clock = pg.time.Clock()

dots = []
for r in range(0, rows + 1):
    row = []
    for c in range(0, cols + 1):
        rect = pg.Rect(
            (dd + cw) * c + gutter + x_shift, 
            (dd + ch) * r + gutter + y_shift, 
            dd, dd
        )
        row.append(rect)
        pg.draw.rect(screen, BLACK, rect)
    dots.append(row)

edges = []
for r in range(0, rows + 1):
    row = []
    for c in range(0, cols + 1):
        h_edge, v_edge = None, None
        if c < cols:
            # horizontal edge
            h_edge = pg.Rect(
                (c + 1) * dd + c * cw + gutter + x_shift,
                r * dd + r * ch + gutter + y_shift, 
                cw, dd
            )
            pg.draw.rect(screen, RED, h_edge)
        
        if r < rows:
            # vertical edge
            v_edge = pg.Rect(
                c * dd + c * cw + gutter + x_shift, 
                (r + 1) * dd + r * ch + gutter + y_shift, 
                dd, ch
            )
            pg.draw.rect(screen, RED, v_edge)
    
        # Group the edges into tuples with (usually) two edges per tuple. Each
        # tuple is stored by row,col in the edges 2-D list. The last column
        # will only have the vertical edge in the tuple. The last row will only
        # have the horizontal edge in the tuple. The last row and column will
        # be empty.
        if h_edge and v_edge:
            row.append((h_edge, v_edge))
        elif h_edge:
            row.append((h_edge,))
        elif v_edge:
            row.append((v_edge,))
        else:
            row.append(())

    edges.append(row)

# Now when looking up the edge that contains x,y, you can quickly retrieve the
# tuple of edges that possibly contains x,y by:
# row = y // (dd + ch)
# col = x // (dd + cw)
# Then simply check collidepoint on each edge to see if it contains the x,y

cells = []
for r in range(0, rows):
    row = []
    for c in range(0, cols):
        rect = pg.Rect(
            (c + 1) * dd + c * cw + gutter + x_shift, 
            (r + 1) * dd + r * ch + gutter + y_shift, 
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
