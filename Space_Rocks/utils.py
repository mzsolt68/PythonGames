from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame import Surface, Color, Font
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

def print_text(surface: Surface, text: str, font: Font, color: Color = Color("tomato")):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = Vector2(surface.get_size()) / 2
    surface.blit(text_surface, text_rect)