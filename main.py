import pygame
from constants import width, height
from damier import Damier
from pions import Pion


#Initialisation de Pygame
pygame.init()


fps = 60

WINS =  pygame.display.set_mode((width, height))
pygame.display.set_caption('Jeu de dames')

def main(): 
    run = True
    clock = pygame.time.Clock()
    damier = Damier()
 
    while run :
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #Affiche l'écran et met à jour la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        damier.draw(WINS)
        pygame.display.update()
    

    pygame.quit

main()