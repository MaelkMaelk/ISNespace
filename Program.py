import pygame, sys
from pygame.locals import *

pygame.init()

#variables
FPS = 60
clock = pygame.time.Clock()

#Création de la fenetre
fenetre = pygame.display.set_mode((1920, 1080), FULLSCREEN)
pygame.display.set_caption("Le shooter du turfu")

#image en arrière plan
fond = pygame.transform.scale(pygame.image.load("images/Espace.jpg"), (1920, 1080))
#fenetre.blit(fond, (0, 0))

#Chargement et collage du personnage

#fenetre.blit(perso, position_perso)


font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def mainMenu():
    while True:
        fenetre.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), fenetre, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(fenetre, (255, 0, 0), button_1)
        pygame.draw.rect(fenetre, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(FPS)


#maj de la fenetre
pygame.display.flip()
clock.tick(FPS)

pygame.key.set_repeat(100, 100)

#BOUCLE INFINIE
def game():
    continuer = True
    while continuer:
        for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: #Si un de ces événements est de type QUIT
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

        perso = pygame.image.load("images/perso.png").convert_alpha()
        position_perso = perso.get_rect()
        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, position_perso)
        #Rafraichissement
        pygame.display.flip()

mainMenu()

pygame.quit()
