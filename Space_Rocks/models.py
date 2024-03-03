from pygame.math import Vector2
from pygame import Surface
from pygame.transform import rotozoom
import random
from utils import load_a_sprite, wrap_position

DIRECTION_UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position: tuple, sprite: Surface, velocity: tuple, wrap: bool = True):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)
        self.wrap = wrap

    def draw(self, surface: Surface):
        draw_pos = self.position - Vector2(self.radius)
        surface.blit(self.sprite, draw_pos)

    def move(self, surface: Surface):
        move_to = self.position + self.velocity
        if self.wrap:
            self.position = wrap_position(surface, move_to)
        else:
            self.position = move_to

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

class Asteroid(GameObject):
    MIN_START_GAP = 250
    MIN_SPEED = 1
    MAX_SPEED = 3

    def __init__(self, surface: Surface, ship_position: Vector2):
        # Generate a random position that far enough from the ship
        while True:
            position = Vector2(
                random.randrange(surface.get_width()),
                random.randrange(surface.get_height())
            )

            if position.distance_to(ship_position) > self.MIN_START_GAP:
                break
        
        speed = random.randint(self.MIN_SPEED, self.MAX_SPEED)
        angle = random.randint(0, 360)
        velocity = Vector2(speed, 0).rotate(angle)
        super().__init__(position, load_a_sprite("asteroid"), velocity)

class Bullet(GameObject):
    def __init__(self, position: tuple, velocity: tuple):
        super().__init__(position, load_a_sprite("bullet"), velocity, False)