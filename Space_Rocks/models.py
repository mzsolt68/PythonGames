from pygame.math import Vector2
from pygame import Surface

class GameObject:
    def __init__(self, position: tuple, sprite: Surface, velocity: tuple):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface: Surface):
        draw_pos = self.position - Vector2(self.radius)
        surface.blit(self.sprite, draw_pos)

    def move(self):
        self.position += self.velocity

    def is_collides(self, other: 'GameObject') -> bool:
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius
