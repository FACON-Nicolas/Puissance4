import sys
import pygame
import random
from pygame.locals import *
from joueur import Joueur

pygame.init()

def Create_Platform():
    # print platform
    for x in range(0,700,100):
        for y in range(100,700,100):
            surface.blit(square, (x,y))

def platform_is_full():
    for i in range(len(Grille[0])):
        if Grille[0][i] == 0: return False
    font=pygame.font.Font(pygame.font.match_font('arialblack'), 50, bold=True)
    text = font.render("Fin de Partie",True,(230,170, 230))
    return True

def direction(g,case, direction):
    l,c = case
    dl, dc = direction
    j = g[l][c]
    for i in range(1,4):
        l,c = l+dl, c+dc
        if l < 0 or l >= 6 or c < 0 or c >= 7: return False
        if g[l][c] != j or g[l][c] == 0: 
            return False
    return True

def gagne_direction(g):
    for l in range(6):
        for c in range(7):
            for dl in range(-1,2):
                for dc in range(-1,2):
                    if (dl,dc) != (0,0):
                     p = direction(g,(l,c), (dl,dc))
                     if p : 
                         font=pygame.font.Font(pygame.font.match_font('arialblack'), 100, bold=True)
                         text = font.render("Victoire",True,(230,170, 230))
                         surface.blit(text, (140,300))
                         return True
    return False

def print_game(j):
    #update game
    surface.fill((0,0,0))
    Create_Platform()
    for l in range(6):
        for c in range(7):
            if Grille[l][c] != 0:
                if Grille[l][c] == 1:
                    coin = jaune.copy()
                elif Grille[l][c] == 2:
                    coin = rouge.copy()
                surface.blit(coin, (9 + (c * 100), 109 + (l * 100)))
    surface.blit(j.image, (j.x,j.y))

def place_coin(j):
    #place coin in the platform
    c = int((j.x - 9) / 100)
    l = 0
    while True:
        if Grille[l+1][c] == 0 and (l+1) < 5: l += 1
        else:
            if Grille[l+1][c] == 0: l += 1 
            Grille[l][c] = j.value
            break

def random_place():
    i = random.randint(0, len(Grille))
    return 9 + (i*100)

# const initialization
LONGUEUR = 700
LARGEUR = 700

# platform initialization
Grille = [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]

# display initialization
surface = pygame.display.set_mode((LONGUEUR, LARGEUR))
title = pygame.display.set_caption("Puissance 4")
icon = pygame.image.load('P4.png')
pygame.display.set_icon(icon)
pygame.mouse.set_visible(False)

# image initialization
square = pygame.image.load('case.png').convert_alpha()
jaune = pygame.image.load('jaune.png').convert_alpha()
rouge = pygame.image.load('rouge.png').convert_alpha()

j1 = True
isDown = False
win = False
game_running = True
clock = pygame.time.Clock()

joueur1 = Joueur(jaune,1)
joueur2 = Joueur(rouge,2)

Touches = []

# print game
Create_Platform()
surface.blit(joueur1.image, (joueur1.x, joueur1.y))

# loop to keep the pygame window open
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
        elif event.type == KEYDOWN and event.key not in Touches:
            Touches.append(event.key)
        elif event.type == KEYUP and event.key in Touches:
            Touches.remove(event.key)
            isDown = False

    # player's input
    if not win:
        if j1:
            if K_RIGHT in Touches and 609 > joueur1.x >= 9:
                if not isDown:
                    isDown = True
                    joueur1.move_coin(100, surface)
                    print_game(joueur1)
                    joueur1.i = int((joueur1.x - 9) / 100)
            elif K_LEFT in Touches and 609 >= joueur1.x > 9:
                if not isDown:
                    isDown = True
                    joueur1.move_coin(-100, surface)
                    print_game(joueur1)
                    joueur1.i = int((joueur1.x - 9) / 100)
            elif K_SPACE in Touches and Grille[0][joueur1.i] == 0:
                if not isDown:
                    isDown = True
                    place_coin(joueur1)
                    print_game(joueur2)
                    win = platform_is_full()
                    if not win:
                        win = gagne_direction(Grille)
                        j1 = False
            elif K_ESCAPE in Touches:
                game_running = False
        #"AI"
        elif not j1:
            pygame.time.wait(1000)
            joueur2.x = random_place() 
            joueur2.i = int((joueur2.x - 9) / 100)
            if Grille[0][joueur2.i] == 0:
                place_coin(joueur2)
                print_game(joueur1)
                win = platform_is_full()
                if not win:
                    win = gagne_direction(Grille)
                    j1 = True
    else:
        if K_SPACE in Touches:
            if not isDown:
                isDown = True
                win = False
                j1 = True
                joueur1.x = joueur2.x = 9
                Grille = [[0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0]]
                print_game(joueur1)
            
    # display's update 
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
