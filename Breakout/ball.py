from gameobject import GameObject
from utils import load_a_sprite
from pygame import Surface
from pygame.math import Vector2
from gamedefs import SCREEN_WIDTH, SCREEN_HEIGHT


class Ball(GameObject):
    def __init__(self, position: tuple):
        self.position = Vector2(position)
        super().__init__(position, load_a_sprite("ball"))
        self.direction = Vector2(1, 1)
        self.radius = self.sprite.get_width() / 2
        self.speed = 3
        self.in_field = True

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

    def hit_brick(self, brick: 'GameObject') -> bool:
        if self._hit_on_top(brick) or self._hit_on_bottom(brick) or self._hit_on_left(brick) or self._hit_on_right(brick):
            return True
        return False

    def _hit_on_top(self, brick: 'GameObject') -> bool:
        if brick.position.x <= self.position.x <= brick.position.x + brick.sprite.get_width() \
                and 0 <= brick.position.y - (self.position.y + self.radius) <= self.radius:
            self.direction.y *= -1
            print("hit on top")
            return True
        return False

    def _hit_on_bottom(self, brick: 'GameObject') -> bool:
        if brick.position.x <= self.position.x <= brick.position.x + brick.sprite.get_width() \
                and 0 <= self.position.y - (brick.position.y + brick.sprite.get_height()) <= self.radius:
            self.direction.y *= -1
            print("hit on bottom")
            return True
        return False

    def _hit_on_left(self, brick: 'GameObject') -> bool:
        if brick.position.y <= self.position.y <= brick.position.y + brick.sprite.get_height() \
                and 0 <= brick.position.x - (self.position.x + self.radius) <= self.radius:
            self.direction.x *= -1
            print("hit on left")
            return True
        return False

    def _hit_on_right(self, brick: 'GameObject') -> bool:
        if brick.position.y <= self.position.y <= brick.position.y + brick.sprite.get_height() \
                and 0 <= self.position.x - (brick.position.x + brick.sprite.get_width()) <= self.radius:
            self.direction.x *= -1
            print("hit on right")
            return True
        return False
