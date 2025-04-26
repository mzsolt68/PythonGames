from gameobject import GameObject
from utils import load_a_sprite
from pygame import Surface, Rect
from pygame.math import Vector2
from gamedefs import SCREEN_WIDTH, SCREEN_HEIGHT


class Ball(GameObject):
    def __init__(self, position: tuple):
        self.position = Vector2(position)
        super().__init__(position, load_a_sprite("ball"))
        self.direction = Vector2(1, 1)
        self.radius = self.sprite.get_width() / 2
        self.speed = 3
        self.in_field = True

    def move(self):
        self.position += self.direction * self.speed
        if self.position.x <= 0 or self.position.x >= SCREEN_WIDTH - self.sprite.get_width():
            self.direction.x *= -1
        if self.position.y <= 0:
            self.direction.y *= -1
        if self.position.y >= SCREEN_HEIGHT - self.sprite.get_height():
            self.in_field = False

    def draw(self, surface: Surface):
        surface.blit(self.sprite, self.position)

    def hit_paddle(self, paddle: 'GameObject') -> bool:
        # Create rectangles for the ball and the paddle
        ball_rect = Rect(
            self.position.x - self.radius,  # Ball's left
            self.position.y - self.radius,  # Ball's top
            self.radius * 2,                # Ball's width
            self.radius * 2                 # Ball's height
        )
        paddle_rect = Rect(
            paddle.position.x,              # Paddle's left
            paddle.position.y,              # Paddle's top
            paddle.sprite.get_width(),      # Paddle's width
            paddle.sprite.get_height()      # Paddle's height
        )

        # Check if the ball collides with the paddle
        if ball_rect.colliderect(paddle_rect):
            # Reverse the vertical direction of the ball
            self.direction.y *= -1

            # Adjust the horizontal direction based on where the ball hits the paddle
            paddle_center = paddle.position.x + paddle.sprite.get_width() / 2
            ball_center = self.position.x
            offset = (ball_center - paddle_center) / (paddle.sprite.get_width() / 2)
            self.direction.x = offset  # Adjust horizontal direction proportionally
            self.direction = self.direction.normalize()  # Normalize to maintain speed

            return True  # Collision occurred
        return False  # No collision

    def hit_brick(self, brick: 'GameObject') -> bool:
        # Create rectangles for the ball and the brick
        ball_rect = Rect(
            self.position.x - self.radius,  # Ball's left
            self.position.y - self.radius,  # Ball's top
            self.radius * 2,                # Ball's width
            self.radius * 2                 # Ball's height
        )
        brick_rect = Rect(
            brick.position.x,               # Brick's left
            brick.position.y,               # Brick's top
            brick.sprite.get_width(),       # Brick's width
            brick.sprite.get_height()       # Brick's height
        )

        # Check if the ball collides with the brick
        if ball_rect.colliderect(brick_rect):
            # Determine the collision side
            if ball_rect.bottom <= brick_rect.top + self.radius:  # Hit from the top
                self.direction.y *= -1
            elif ball_rect.top >= brick_rect.bottom - self.radius:  # Hit from the bottom
                self.direction.y *= -1
            elif ball_rect.right <= brick_rect.left + self.radius:  # Hit from the left
                self.direction.x *= -1
            elif ball_rect.left >= brick_rect.right - self.radius:  # Hit from the right
                self.direction.x *= -1

            return True  # Collision occurred
        return False  # No collision
