
import pygame as pg

class Breakout():
    def __init__(self):
        pg.init()
        pg.display.set_caption("Breakout")
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 64)

        self.screen = pg.display.set_mode((800, 600))


    def mainloop(self):
        while True:
            self.handle_input()

    def handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_ESCAPE] or pressed_key[pg.K_q]:
            quit()
