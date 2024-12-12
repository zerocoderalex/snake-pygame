import pygame

class Snake:
    def __init__(self, initial_position, block_size):
        self.body = [initial_position]
        self.block_size = block_size
        self.direction = (block_size, 0)

    def move(self):
        head_x, head_y = self.body[0]
        x_dir, y_dir = self.direction
        new_head = (head_x + x_dir, head_y + y_dir)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def set_direction(self, new_direction):
        x_dir, y_dir = self.direction
        new_x_dir, new_y_dir = new_direction
        if (x_dir + new_x_dir!= 0 or
            y_dir + new_y_dir != 0):
            self.direction = new_direction

    def has_collided(self, width, height):
        head = self.body[0]
        h_x, h_y = head
        return (
            h_x < 0 or h_y < 0 or
            h_x >= width or h_y >= height or
            head in self.body[1:]
        )

    def draw(self, screen, color):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(
                    segment[0], segment[1],
                    self.block_size, self.block_size
                )
            )
