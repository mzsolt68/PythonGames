
import pygame as pg
from paddle import Paddle

class Breakout():
    def __init__(self):
        pg.init()
        pg.display.set_caption("Breakout")
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 64)

        self.screen = pg.display.set_mode((800, 600))
        self.paddle = Paddle((400, 575))


    def mainloop(self):
        while True:
            self.handle_input()
            self.draw()
            self.clock.tick(60)

    def handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_ESCAPE] or pressed_key[pg.K_q]:
            quit()
        elif pressed_key[pg.K_LEFT]:
            self.paddle.move(-5)
        elif pressed_key[pg.K_RIGHT]:
            self.paddle.move(5)
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle.draw(self.screen)
        pg.display.flip()

