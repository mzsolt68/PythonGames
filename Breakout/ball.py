from gameobject import GameObject
from utils import load_a_sprite
from pygame import Surface
from pygame.math import Vector2
from gamedefs import SCREEN_WIDTH, SCREEN_HEIGHT


class Ball(GameObject):
    def __init__(self, position: tuple):
        self.position = Vector2(position)
        self.move_x = 2
        self.move_y = 2
        super().__init__(position, load_a_sprite("ball"))

    def move(self):
        self.position.x += self.move_x
        self.position.y += self.move_y
        if self.position.x <= 0 or self.position.x >= SCREEN_WIDTH - self.sprite.get_width():
            self.move_x *= -1
        if self.position.y <= 0 or self.position.y >= SCREEN_HEIGHT - self.sprite.get_height():
            self.move_y *= -1

    def draw(self, surface: Surface):
        surface.blit(self.sprite, self.position)
