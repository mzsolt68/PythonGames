import pygame as pg
from utils import load_a_sprite
from models import GameObject

class SpaceRocks:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Space Rocks")
        self.screen = pg.display.set_mode((800, 600))
        self.background = load_a_sprite("space", False)

        sprite = load_a_sprite("spaceship")
        self.spaceship = GameObject((400, 300), sprite, (0, 0))

        sprite = load_a_sprite("asteroid")
        self.asteroid = GameObject((50, 300), sprite, (1, 0))

        self.collisions = 0

    def game_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        pg.display.flip()
