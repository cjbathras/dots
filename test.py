import math
import sys
import time

import pygame
from pygame.locals import *

from __init__ import *


def main():
    pygame.display.init()
    pygame.display.set_caption('Test')

    display = pygame.display.set_mode(CELL_SIZE)
    surf = pygame.display.get_surface()

    # Prefix of r_ means variable is a Rect
    # tl = top left
    # tr = top right
    # bl = bottom left
    # br = bottom right
    # Define all of the component rectangles
    r_cell = pygame.Rect(CELL_ORIGIN, CELL_SIZE)

    # Corner dots
    r_dot_tl = pygame.Rect(r_cell.x - DOT_RAD, r_cell.y - DOT_RAD, DOT_DIA, DOT_DIA)
    r_dot_tr = pygame.Rect(r_cell.topright[0] - DOT_RAD, r_cell.y - DOT_RAD, DOT_DIA, DOT_DIA)
    r_dot_bl = pygame.Rect(r_cell.bottomleft[0] - DOT_RAD, r_cell.bottomleft[1] - DOT_RAD, DOT_DIA, DOT_DIA)
    r_dot_br = pygame.Rect(r_cell.bottomright[0] - DOT_RAD, r_cell.bottomright[1] - DOT_RAD, DOT_DIA, DOT_DIA)

    # Edges
    r_top_edge = pygame.Rect(CELL_ORIGIN, (CELL_WIDTH, DOT_DIA * 0.707))
    r_top_edge.center = r_cell.midtop
    r_bottom_edge = pygame.Rect(CELL_ORIGIN, (CELL_WIDTH, DOT_DIA * 0.707))
    r_bottom_edge.center = r_cell.midbottom
    r_left_edge = pygame.Rect(CELL_ORIGIN, (DOT_DIA * 0.707, CELL_HEIGHT))
    r_left_edge.center = r_cell.midleft
    r_right_edge = pygame.Rect(CELL_ORIGIN, (DOT_DIA * 0.707, CELL_HEIGHT))
    r_right_edge.center = r_cell.midright

    # Edge highlights
    r_top_highlight = r_top_edge.move(0, 0)
    r_top_highlight.width -= (DOT_DIA * 2)
    r_top_highlight.height = HIGHLIGHT_WIDTH
    r_top_highlight.center = r_top_edge.center

    r_bottom_highlight = r_bottom_edge.move(0, 0)
    r_bottom_highlight.width -= (DOT_DIA * 2)
    r_bottom_highlight.height = HIGHLIGHT_WIDTH
    r_bottom_highlight.center = r_bottom_edge.center

    r_left_highlight = r_left_edge.move(0, 0)
    r_left_highlight.width = HIGHLIGHT_WIDTH
    r_left_highlight.height -= (DOT_DIA * 2)
    r_left_highlight.center = r_left_edge.center

    r_right_highlight = r_right_edge.move(0, 0)
    r_right_highlight.width = HIGHLIGHT_WIDTH
    r_right_highlight.height -= (DOT_DIA * 2)
    r_right_highlight.center = r_right_edge.center

    # Draw the component shapes
    pygame.draw.rect(surf, WHITE, r_cell)

    pygame.draw.circle(surf, BLACK, r_dot_tl.center, DOT_RAD)
    pygame.draw.circle(surf, BLACK, r_dot_tr.center, DOT_RAD)
    pygame.draw.circle(surf, BLACK, r_dot_bl.center, DOT_RAD)
    pygame.draw.circle(surf, BLACK, r_dot_br.center, DOT_RAD)

    pygame.display.update()
    current_highlight = None

    while True:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pass

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = x, y = pygame.mouse.get_pos()
                if r_top_edge.collidepoint(mouse_pos):
                    print(f'top_edge: mouse_pos={mouse_pos}')
                    pygame.draw.rect(surf, GREEN, r_top_highlight, width=0)
                    current_highlight = r_top_highlight
                elif r_bottom_edge.collidepoint(mouse_pos):
                    print(f'bottom_edge: mouse_pos={mouse_pos}')
                    pygame.draw.rect(surf, GREEN, r_bottom_highlight, width=0)
                    current_highlight = r_bottom_highlight
                elif r_left_edge.collidepoint(mouse_pos):
                    print(f'left_edge: mouse_pos={mouse_pos}')
                    pygame.draw.rect(surf, GREEN, r_left_highlight, width=0)
                    current_highlight = r_left_highlight
                elif r_right_edge.collidepoint(mouse_pos):
                    print(f'right_edge: mouse_pos={mouse_pos}')
                    pygame.draw.rect(surf, GREEN, r_right_highlight, width=0)
                    current_highlight = r_right_highlight
                else:
                    if current_highlight:
                        pygame.draw.rect(surf, WHITE, current_highlight, width=0)
                        current_highlight = None

        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
