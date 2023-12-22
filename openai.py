import pygame

# Initialisation de pygame
pygame.init()

# Couleurs des pions
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Création de la fenêtre de jeu
fenetre = pygame.display.set_mode((600, 600))

# Liste des pièces
pieces = []

# Ajout des pièces au tableau
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            couleur = blanc
        else:
            couleur = noir
        pieces.append((i * 75 + 50, j * 75 + 50, couleur))

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner le tableau de jeu de dame
    fenetre.fill((0, 0, 0))
    for piece in pieces:
        pygame.draw.circle(fenetre, piece[2], piece[:2], 25)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter pygame
pygame.quit()