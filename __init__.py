import pygame

# Color definitions
BLACK         = pygame.Color(0, 0, 0)
BLUE          = pygame.Color(0, 0, 255)
CYAN          = pygame.Color(0, 255, 255)
DARK_GRAY     = pygame.Color(64, 64, 64)
GRAY          = pygame.Color(128, 128, 128)
GREEN         = pygame.Color(0, 255, 0)
LIGHT_GRAY    = pygame.Color(240, 240, 240)
MAGENTA       = pygame.Color(255, 0, 255)
RED           = pygame.Color(255, 0, 0)
WHITE         = pygame.Color(255, 255, 255)
YELLOW        = pygame.Color(255, 255, 0)
PLAYER1_COLOR = pygame.Color(107, 209, 129)
PLAYER2_COLOR = pygame.Color(204, 151, 222)

# You MUST call font.init() before loading any fonts
pygame.font.init()
FONT_LATO_REGULAR_20 = pygame.font.Font('fonts/Lato-Regular.ttf', 20)
FONT_DEFAULT = pygame.font.Font(None, 18)

# Utility functions
def is_even(a):
    return False if a % 2 else True

def is_odd(a):
    return True if a % 2 else False
