import pygame
from pygame.locals import *
pygame.init()

#variables
FPS = 60
clock = pygame.time.Clock()

#Création de la fenetre
fenetre = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Le shooter du turfu")

#image en arrière plan
fond = pygame.transform.scale(pygame.image.load("images/Espace.jpg"), (1920, 1080))
fenetre.blit(fond, (0, 0))

#Chargement et collage du personnage
perso = pygame.image.load("images/perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)



def menue():
    menu = False
    while menu:
        for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
            fenetre.blit(fond, (0, 0))

#maj de la fenetre
pygame.display.flip()
clock.tick(FPS)

pygame.key.set_repeat(100, 100)

#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
        if event.type == QUIT: #Si un de ces événements est de type QUIT
            continuer = 0 #On arrête la boucle


        if event.type == KEYDOWN:
            if event.key == K_DOWN: #Si "flèche bas" On descend le perso
                position_perso = position_perso.move(0,30)
            if event.key == K_UP:
                position_perso = position_perso.move(0,-10)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(20,0)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-20,0)


    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
    #Rafraichissement
    pygame.display.flip()
pygame.quit()
