import pygame
import random

class Food:
    def __init__(self, screen_width, screen_height, block_size):
        self.position = (0, 0)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.generate()

    def generate(self):
        self.position = (
            random.randint(
                0,
                (self.screen_width - self.block_size) // self.block_size
            ) * self.block_size,
            random.randint(
                0,
                (self.screen_height - self.block_size) // self.block_size
            ) * self.block_size
        )

    def draw(self, screen, color):
        pygame.draw.rect(
            screen,
            color,
            pygame.Rect(
                self.position[0], self.position[1],
                self.block_size, self.block_size
            )
        )
