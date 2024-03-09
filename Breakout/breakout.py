
import pygame as pg
from paddle import Paddle
from ball import Ball
from gamedefs import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK

class Breakout():
    def __init__(self):
        pg.init()
        pg.display.set_caption("Breakout")
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 64)

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.paddle = Paddle((400, 575))
        self.ball = Ball((400, 300))


    def mainloop(self):
        while True:
            self.handle_input()
            self.ball.move()
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
        self.screen.fill(BLACK)
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        pg.display.flip()

