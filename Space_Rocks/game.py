import pygame as pg
from utils import load_a_sprite
from models import SpaceShip, Asteroid

class SpaceRocks:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Space Rocks")
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((800, 600))
        self.background = load_a_sprite("space", False)

        self.bullets = []

        self.spaceship = SpaceShip((400, 300), self.bullets)

        self.asteroids = [Asteroid(self.screen, self.spaceship.position) for _ in range(6)]

    def game_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.spaceship.shoot()
        
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_ESCAPE] or pressed_key[pg.K_q]:
            quit()
        if pressed_key[pg.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        elif pressed_key[pg.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif pressed_key[pg.K_UP]:
            self.spaceship.accelerate()

    @property
    def game_objects(self):
        return [*self.asteroids, *self.bullets, self.spaceship]

    def _game_logic(self):
        for obj in self.game_objects:
            obj.move(self.screen)
        
        rect = self.screen.get_rect()
        for bullet in self.bullets[:]:
            if not rect.collidepoint(bullet.position):
                self.bullets.remove(bullet)

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        
        for obj in self.game_objects:
            obj.draw(self.screen)
        
        pg.display.flip()
        self.clock.tick(30)
