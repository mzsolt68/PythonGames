from gameobject import GameObject
from utils import load_a_sprite
from pygame import Surface
from pygame.math import Vector2
from gamedefs import SCREEN_WIDTH

class Brick(GameObject):
    def __init__(self, position: tuple, filename: str):
        super().__init__(position, load_a_sprite(filename))

    def draw(self, surface: Surface):
        surface.blit(self.sprite, self.position)
