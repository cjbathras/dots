import pygame


class Player:
    def __init__(self, name: str, color: pygame.Color):
        super().__init__()
        self.name = name
        self.color = color

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'
