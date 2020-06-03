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
#nique la police d'écriture
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

#BOUCLE INFINIE
def game():
    perso = pygame.image.load("images/perso.png").convert_alpha()
    position_perso = [0,0]
    movedown = False
    moveup = False
    continuer = True
    while continuer:


        if movedown == True and position_perso[1] <= 1080-perso.get_height():
            position_perso[1] += 8
        if moveup == True and position_perso[1] >= 0:
            position_perso[1] -= 8










        for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: #Si un de ces événements est de type QUIT
                    continuer = 0 #On arrête la boucle
            if event.type == KEYDOWN:
                if event.key == K_DOWN: #Si "flèche bas" On descend le perso
                    movedown = True
                if event.key == K_UP:
                    moveup = True
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    movedown = False
                if event.key == K_UP:
                    moveup = False

        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, position_perso)
        pygame.display.update()
        clock.tick(FPS)





        #Rafraichissement
        pygame.display.flip()

mainMenu()

pygame.quit()
