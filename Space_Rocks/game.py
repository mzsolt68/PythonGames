import pygame as pg
from utils import load_a_sprite
from models import SpaceShip

class SpaceRocks:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Space Rocks")
        self.screen = pg.display.set_mode((800, 600))
        self.background = load_a_sprite("space", False)

        self.spaceship = SpaceShip((400, 300))

    def game_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_ESCAPE] or pressed_key[pg.K_q]:
            quit()
        if pressed_key[pg.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        elif pressed_key[pg.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif pressed_key[pg.K_UP]:
            self.spaceship.accelerate()

    def _game_logic(self):
        self.spaceship.move()

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        pg.display.flip()
