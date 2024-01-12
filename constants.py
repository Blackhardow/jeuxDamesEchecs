import pygame
import sys

WIDTH, HEIGHT = 650, 650
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

#couleur du damiers RGB
ABS_WHITE = (255,255,255)
WHITE = (238,238,228)
BLACK = (79, 74, 70)
BLUE= (190, 224, 236)
GREY = (128, 128, 128)
RED = (255, 0, 0) 


CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
NOIR = pygame.transform.scale(pygame.image.load('assets/black_dame.png'), (64, 64))
BLANC = pygame.transform.scale(pygame.image.load('assets/white_dame.png'), (64, 64))



