from gameobject import GameObject
from utils import load_a_sprite
from pygame import Surface
from pygame.math import Vector2

class Paddle(GameObject):
    def __init__(self, position: tuple):
        self.position = Vector2(position)
        super().__init__(position, load_a_sprite("paddle"))

    def move(self, step_x: int):
        self.position.x += step_x
        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > 800 - self.sprite.get_width():
            self.position.x = 800 - self.sprite.get_width()

    def draw(self, surface: Surface):
        surface.blit(self.sprite, self.position)
