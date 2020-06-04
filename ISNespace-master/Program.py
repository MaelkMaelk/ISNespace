import pygame, sys
from pygame.locals import *
import time

pygame.init()

#variables
FPS = 60
clock = pygame.time.Clock()


#Création de la fenetre
fenetre = pygame.display.set_mode((1920, 1080), FULLSCREEN)
pygame.display.set_caption("Le shooter du turfu")

#Textures
fond = pygame.transform.scale(pygame.image.load("images/Espace.jpg"), (1920, 1080))
start = pygame.image.load("images/start.jpg").convert_alpha()
perso = pygame.image.load("images/perso.png").convert_alpha()
stop = pygame.image.load("images/stop.jpg").convert_alpha()

#Sons
son = pygame.mixer.Sound("son/son.wav")
son2 = pygame.mixer.Sound("son/piou.wav")
son3 = pygame.mixer.Sound("son/piou2.wav")
son4 = pygame.mixer.Sound("son/vehicule.wav")
son5 = pygame.mixer.Sound("son/vehicule2.wav")
son6 = pygame.mixer.Sound("son/son.wav")
son7 = pygame.mixer.Sound("son/gameover.wav")

#nique la police d'écriture
font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
#Le main menu principale
def mainMenu():
    click = False
    while True:
        fenetre.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), fenetre, 20, 20)
        draw_text('Jouer', font, (0, 255, 255), fenetre, 900, 500)
        draw_text('CAHSOHTOI', font, (255, 0, 0), fenetre, 900, 900)


        mx, my = pygame.mouse.get_pos()
        #boutton start
        fenetre.blit(start, (960-start.get_width()/2,300))
        button_1 = pygame.Rect(960-start.get_width()/2, 300, start.get_height(), start.get_width())
        #boutton stop arretez vous
        fenetre.blit(stop, (960-stop.get_width()/2,600))
        button_2 = pygame.Rect(960-stop.get_width()/2, 600, stop.get_height(), stop.get_width())
        if button_1.collidepoint((mx, my)):
            if click:
                son.play()
                time.sleep(4)
                son.stop()
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

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

def gameover(qui):
    #joueur a gagné
    if qui == True:
        son2.stop() #on stop tous les sons pour entendre le son de fin de jeu
        son3.stop()
        son4.stop()
        son5.stop()
        son6.play
        time.sleep(2)
        son7.play()
        fenetre.fill((0,0,0))
        fenetre.blit(start, (960-start.get_width()/2,300))
        draw_text('perso vicotory', font, (255, 255, 0), fenetre, 900, 500)
    #joueur 2 a gagné
    else:
        son2.stop()
        son3.stop()
        son4.stop()
        son5.stop()
        son6.play
        time.sleep(2)
        son7.play()
        fenetre.fill((0,0,0))
        fenetre.blit(stop, (960-stop.get_width()/2,600))
        draw_text('perso not vicotory', font, (0, 255, 255), fenetre, 900, 500)
    pygame.display.flip()
    time.sleep(5)
    mainMenu()


#maj de la fenetre
pygame.display.flip()
clock.tick(FPS)

def game():

#definition de la position des perso + déplacement des images
    position_perso = [0,0]
    position_perso2 =[1920-perso.get_width(),0]
    movedown = False
    moveup = False
    movedown2 = False
    moveup2 = False
    continuer = True
    Fire = False
    Fire2 = False
    lasers = []
    lasers2 = []
    dernierTir = 0
    dernierTir2 = 0
    #BOUCLE INFINIE
    time = 0
    while continuer:
        time += 0.015
        #bloquage du perso

        if movedown == True and position_perso[1] <= 1080-perso.get_height():
            position_perso[1] += 8
        if moveup == True and position_perso[1] >= 0:
            position_perso[1] -= 8
        #commandes de tirs, piou piou
        if Fire == True and (time > dernierTir+1):
            laser = {"x":position_perso[0],"y":position_perso[1]}
            lasers.append(laser)
            dernierTir = time
        if Fire2 == True and (time > dernierTir2+1):
            laser2 = {"x":position_perso2[0],"y":position_perso2[1]}
            lasers2.append(laser2)
            dernierTir2 = time
        #bloquage du perso2
        if movedown2 == True and position_perso2[1] <= 1080-perso.get_height():
            position_perso2[1] += 8
        if moveup2 == True and position_perso2[1] >= 0:
            position_perso2[1] -= 8

        jouer = pygame.Rect(position_perso[0], position_perso[1], perso.get_height(), perso.get_width()) #création d'une hitbox du fréro
        jouer2 = pygame.Rect(position_perso2[0], position_perso2[1], perso.get_height(), perso.get_width()) #création d'une hitbox du fréro









        for event in pygame.event.get(): #On parcours la liste de tous les événements reçus
            if event.type == KEYDOWN:
                #si la touche est enfoncé
                if event.key == K_ESCAPE: #Si un de ces événements est de type QUIT
                    continuer = 0 #On arrête la boucle
                if event.key == K_s: #Si "flèche bas" On descend le perso
                    movedown = True
                if event.key == K_w:
                    moveup = True
                    son4.play()
                if event.key == K_q:
                    Fire = True
                    son2.play()
                if event.key == K_DOWN: #Si "flèche bas" On descend le perso2
                    movedown2 = True
                if event.key == K_UP: #qwerty
                    moveup2 = True
                    son5.play()
                if event.key == K_SPACE: #qwerty
                    Fire2 = True
                    son3.play()

            #si la touche n'est plus enfoncé
            if event.type == KEYUP:
                if event.key == K_s:
                    movedown = False
                if event.key == K_w:
                    moveup = False
                    son4.stop()
                if event.key == K_q:
                    Fire = False

                if event.key == K_DOWN:
                    movedown2 = False
                if event.key == K_UP: #qwerty
                    moveup2 = False
                    son5.stop()
                if event.key == K_SPACE: #qwerty
                    Fire2 = False





        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, position_perso)
        fenetre.blit(perso, position_perso2)

        clock.tick(FPS)
        #création et lancement du projectile
        for key,value in enumerate(lasers):
            if lasers[key]["x"] >= 1920:
                del lasers[key]
            else:
                piou = pygame.Rect(lasers[key]["x"], lasers[key]["y"], start.get_height(), start.get_width()) #création d'une hitbox du laser
                if piou.colliderect(jouer2):
                    del lasers[key]
                    gameover(True)
                else:
                    lasers[key]["x"] += 20
                    fenetre.blit(start, (lasers[key]["x"], lasers[key]["y"]))
        for key,value in enumerate(lasers2):
            if lasers2[key]["x"] <= 0:
                del lasers2[key]
            else:
                piou2 = pygame.Rect(lasers2[key]["x"], lasers2[key]["y"], start.get_height(), start.get_width()) #création d'une hitbox du laser
                if piou2.colliderect(jouer):
                    del lasers2[key]
                    gameover(False)
                else:
                    lasers2[key]["x"] -= 20
                    fenetre.blit(start, (lasers2[key]["x"], lasers2[key]["y"]))
        pygame.display.update()



mainMenu()

pygame.quit()
#fin de notre magnifique game de jugador du jeu vidéal
