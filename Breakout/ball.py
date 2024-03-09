from gameobject import GameObject
from utils import load_a_sprite
from pygame import Surface
from pygame.math import Vector2
from gamedefs import SCREEN_WIDTH, SCREEN_HEIGHT


class Ball(GameObject):
    def __init__(self, position: tuple):
        self.position = Vector2(position)
        self.direction = Vector2(1, 1)
        self.speed = 2
        self.in_field = True
        super().__init__(position, load_a_sprite("ball"))

    def move(self):
        self.position += self.direction * self.speed
        if self.position.x <= 0 or self.position.x >= SCREEN_WIDTH - self.sprite.get_width():
            self.direction.x *= -1
        if self.position.y <= 0:
            self.direction.y *= -1
        if self.position.y >= SCREEN_HEIGHT - self.sprite.get_height():
            self.in_field = False

    def draw(self, surface: Surface):
        surface.blit(self.sprite, self.position)

    def hit_paddle(self, paddle: 'GameObject')-> bool:
        if self.position.y + self.sprite.get_height() >= paddle.position.y and \
                paddle.position.x <= self.position.x <= paddle.position.x + paddle.sprite.get_width():
            return True
        return False