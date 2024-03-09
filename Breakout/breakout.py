
import pygame as pg
from pygame.math import Vector2
from paddle import Paddle
from ball import Ball
from brick import Brick
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
        self.bricks = []
        self._create_bricks()

    def mainloop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _handle_input(self):
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

    def _game_logic(self):
        self.ball.move()
        if self.ball.hit_paddle(self.paddle):
            self.ball.direction.y *= -1
        if not self.ball.in_field:
            self.ball.direction = Vector2(0, 0)
    
    def _draw(self):
        self.screen.fill(BLACK)
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        for brick in self.bricks:
            brick.draw(self.screen)
        pg.display.flip()
        self.clock.tick(60)

    def _create_bricks(self):
        for i in range(9):
            for j in range(13):
                self.bricks.append(Brick((j * 60 + 10, i * 30 + 30), "green_brick"))