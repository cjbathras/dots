import pygame as pg


class Player:
    def __init__(self, name: str, color: pg.Color):
        super().__init__()
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return f'{type(self).__name__}: {self.name}'

    def __repr__(self) -> str:
        return str(self)
