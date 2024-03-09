from pathlib import Path
from pygame.image import load
from pygame import Surface


def load_a_sprite(name: str, with_alpha: bool = True) -> Surface:
    file_name = Path(__file__).parent / Path("assets/sprites/" + name + ".png")
    sprite = load(file_name.resolve())

    if with_alpha:
        return sprite.convert_alpha()

    return sprite.convert()
