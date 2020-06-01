import pygame
from pygame.locals import *
pygame.init()
# mise en place de la fenetre
fenetre = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Le shooter du turfu")

# garder la fenetre ouverte ou fermé
running = True

while running:
    # si le joueur ferme la fenetre
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            running= False
            pygame.quit()
