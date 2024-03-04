from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame import Surface
from pathlib import Path

def load_a_sprite(name: str, with_alpha: bool = True) -> Surface:
    file_name = Path(__file__).parent / Path("assets/sprites/" + name + ".png")
    sprite = load(file_name.resolve())

    if with_alpha:
        return sprite.convert_alpha()
    
    return sprite.convert()

def wrap_position(surface: Surface, position: Vector2) -> Vector2:
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

def load_sound(name: str) -> Sound:
    file_name = Path(__file__).parent / Path("assets/sounds/" + name + ".wav")
    return Sound(file_name)