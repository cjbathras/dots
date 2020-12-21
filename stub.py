import pygame as pg

from __init__ import *
from button2 import Button

pg.display.init()
screen = pg.display.set_mode((640, 480))

class Stub:
    def __init__(self, screen):
        self._done = False
        self._clock = pg.time.Clock()
        self._screen = screen

        self._quit_button = Button(
            (0, pg.display.get_surface().get_height() - 30), (100, 30),
            self.quit_game, FONT_16, 'Quit')

        self._all_sprites = pg.sprite.Group()
        self._all_sprites.add(self._quit_button)

    def quit_game(self):
        self._done = True

    def run(self):
        while not self._done:
            self._dt = self._clock.tick(30) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                self._done = True

            for sprite in self._all_sprites:
                sprite.handle_event(event)

    def run_logic(self):
        self._all_sprites.update(self._dt)

    def draw(self):
        self._all_sprites.draw(self._screen)
        pg.display.flip()

    def add_sprite(self, spr):
        self._all_sprites.add(spr)


if __name__ == '__main__':
    stub = Stub(screen)

    test_button = Button((10, 10), (100, 30), None, text='Test Button')
    stub.add_sprite(test_button)

    stub.run()
    pg.quit()
