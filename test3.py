import pygame as pg

from __init__ import *

cw = 100
ch = 100
dd = 10
rows = 2
cols = 2
gutter = 0
x_shift = 0
y_shift = 0

pg.display.init()
screen = pg.display.set_mode(
    (cw*cols + dd*(cols+1) + gutter*2 + x_shift, 
    ch*rows + dd*(rows+1) + gutter*2 + y_shift)
)
screen = pg.display.set_mode((1000, 1000))
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

# edges = []
# for r in range(0, rows * 2 + 1):
#     row = []
#     for c in range(0, cols + 1):
#         if is_even(r) and c < cols:
#             rect = pg.Rect(
#                 (c + 1) * dd + c * cw + gutter + x_shift,
#                 r // 2 * dd + r // 2 * ch + gutter + y_shift, 
#                 cw, dd
#             )
#             row.append(rect)
#             pg.draw.rect(screen, RED, rect)
#         elif is_odd(r):
#             rect = pg.Rect(
#                 c * dd + c * cw + gutter + x_shift, 
#                 (r + 1) // 2 * dd + r // 2 * ch + gutter + y_shift, 
#                 dd, ch
#             )
#             row.append(rect)
#             pg.draw.rect(screen, RED, rect)
#     edges.append(row)

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
    
        if h_edge and v_edge:
            row.append((h_edge, v_edge))
        elif h_edge:
            row.append((h_edge,))
        elif v_edge:
            row.append((v_edge,))

    edges.append(row)

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
