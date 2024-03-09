from pygame import Surface
from pygame.math import Vector2

class GameObject:
    def __init__(self, position: tuple, sprite: Surface):
        self.position = Vector2(position)
        self.sprite = sprite

    def draw(self, surface: Surface):
        surface.blit(self.sprite, self.position)
