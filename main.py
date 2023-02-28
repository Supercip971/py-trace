import pygame, sys
from pygame.locals import *
pygame.init()

RATIO = 16/9

HEIGHT = 480
WIDTH = int(RATIO*HEIGHT)

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')


# Transforme les couleurs sous la forme [0;1] vers [0;255]
# Car pygame nécéssite que les couleurs soient sous cette forme

def ucolor_to_pygame_color(r, g, b, a=1.0):
    return (int(r*255),int(g*255),int(b*255),int(a*255))
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for x in range(WIDTH): 
        for y in range(HEIGHT): 
            DISPLAYSURF.set_at((x,y), ucolor_to_pygame_color(x/WIDTH, y/HEIGHT, (x+y)/(WIDTH*HEIGHT)))
    pygame.display.update()
