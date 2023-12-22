import pygame
from pions import Pion
from constants import black, rows, cols, white, square_size


# Create piece instances
# white_piece = Pion( white_piece_image)
# black_piece = Pion(black_piece_image)

class Damier:
    def __init__(self):
        self.damier = []
        self.selected_piece = None
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0

        

    def draw_cubes(self, WINS):
        WINS.fill(black)
        for row in range (rows):
            for col in range (row % 2, cols, 2):
                pygame.draw.rect(WINS, white, (row * square_size, col * square_size, square_size, square_size ))

    def create_damier(self):
        for row in range(rows):
            self.damier.append([])
            for col in range(cols):
                if col % 2 == ((row + 1) % 2):
                    # Si la case est blanche on l'ajoute a la liste des cases blanches et au nombre de pièces blanches/
                    if row < 4:
                        self.damier[row.append(black_piece)]
                    elif row > 5:
                        self.damier[row].append(white_piece)
                    else:
                        self.damier[row].append(0)
                else:
                    self.damier[row].append(0)

    def draw(self, WINS):
        self.draw_cubes(WINS)
        for row in range(rows):
            for col in range(cols):
                pion = self.damier[row][col]
                if pion != 0:
                    pion.draw(WINS)