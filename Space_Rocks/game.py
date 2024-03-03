import pygame as pg

class SpaceRocks:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Space Rocks")
        self.screen = pg.display.set_mode((800, 600))

    def game_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.fill((0, 0, 0))
        pg.display.flip()
