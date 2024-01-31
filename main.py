import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from jeu import Jeu

#Initialisation de Pygame
# pygame.init()

fps = 60

WINS =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jeu de dame')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main(): 
    run = True
    clock = pygame.time.Clock()
    jeu = Jeu(WINS)

 
    while run :
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #Affiche et met à jour la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)

                if jeu.turn == RED:
                    jeu.select(row, col)
              
        jeu.update()
    

    pygame.quit

main()