from pygame.math import Vector2
from pygame import Surface
from pygame.transform import rotozoom
from utils import load_a_sprite, wrap_position

DIRECTION_UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position: tuple, sprite: Surface, velocity: tuple):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface: Surface):
        draw_pos = self.position - Vector2(self.radius)
        surface.blit(self.sprite, draw_pos)

    def move(self, surface: Surface):
        move_to = self.position + self.velocity
        self.position = wrap_position(surface, move_to)

    def is_collides(self, other: 'GameObject') -> bool:
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius

class SpaceShip(GameObject):
    ROTATION_SPEED = 3
    ACCELERATION = 0.25

    def __init__(self, position: tuple):
        self.direction = Vector2(DIRECTION_UP)
        super().__init__(position, load_a_sprite("spaceship"), (0, 0))

    def rotate(self, clockwise: bool = True):
        sign = 1 if clockwise else -1
        angle = self.ROTATION_SPEED * sign
        self.direction.rotate_ip(angle)

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION

    def draw(self, surface: Surface):
        angle = self.direction.angle_to(DIRECTION_UP)
        rotated = rotozoom(self.sprite, angle, 1.0)
        rotated_size = Vector2(rotated.get_size())

        draw_pos = self.position - rotated_size * 0.5
        surface.blit(rotated, draw_pos)
