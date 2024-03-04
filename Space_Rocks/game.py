import pygame as pg
from utils import load_a_sprite, print_text
from models import SpaceShip, Asteroid

bullets = []
asteroids = []

class SpaceRocks:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Space Rocks")
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 64)
        self.message = ""

        self.screen = pg.display.set_mode((800, 600))
        self.background = load_a_sprite("space", False)

        self.spaceship = SpaceShip((400, 300))

        global asteroids
        asteroids = [
            Asteroid.create_random(self.screen, self.spaceship.position)
            for _ in range(6)
        ]

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
        
        if self.spaceship is None:
            return
        
        if pressed_key[pg.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        elif pressed_key[pg.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif pressed_key[pg.K_UP]:
            self.spaceship.accelerate()

    @property
    def game_objects(self):
        global bullets, asteroids
        objects = [*bullets, *asteroids]
        if self.spaceship:
            objects.append(self.spaceship)
        return objects

    def _game_logic(self):
        global bullets, asteroids

        for obj in self.game_objects:
            obj.move(self.screen)
        
        rect = self.screen.get_rect()
        for bullet in bullets[:]:
            if not rect.collidepoint(bullet.position):
                bullets.remove(bullet)
        
        for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                if asteroid.is_collides(bullet):
                    asteroids.remove(asteroid)
                    asteroid.split()
                    bullets.remove(bullet)
                    break
        
        if self.spaceship:
            for asteroid in asteroids:
                if asteroid.is_collides(self.spaceship):
                    self.spaceship = None
                    self.message = "Game Over"
                    break
        
        if not asteroids and self.spaceship:
            self.message = "You Won!"


    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        
        for obj in self.game_objects:
            obj.draw(self.screen)
        
        if self.message:
            print_text(self.screen, self.message, self.font)
        
        pg.display.flip()
        self.clock.tick(30)
