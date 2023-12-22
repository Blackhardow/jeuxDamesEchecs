import pygame
from constants import white, black, square_size, grey



# Load images
white_piece_image = pygame.image.load('white_dame.png')
black_piece_image = pygame.image.load('black_dame.png')

class Pion:
    padding = 10
    outline = 2
    def __init__(self, row, col,  color,):
        self.row = row
        self.col = col
        self.color = color
        self.image = black_piece_image if color == black else white_piece_image
        self.king = False
        if self.color == white:
            self.direction = -1
        else:
            self.direction = 1
        
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = square_size * self.col + square_size // 2
        self.x = square_size * self.row + square_size // 2

    def make_king(self):
        self.king = True

    def draw(self, WINS):
        radius = square_size // 2 - self.padding
        pygame.draw.circle(WINS, grey, (self.x, self.y), radius + self.outline)
        WINS.blit(self.image, (self.x, self.y))
    
    def __repr__(self):
        return f"Pion({self.color}, {self.image})"