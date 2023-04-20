import pygame
import sys
from pygame.locals import *

from color import Color
# initialise le système de pygame
pygame.init()

# bonjour 2

# La fenêtre aura 480 pixels de hauteur
# Et la largeur aura 16/9 de la hauteur soit ~853 pixels
RATIO = 16/9
HEIGHT = 480
WIDTH = int(RATIO*HEIGHT)

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# Bonjour

# Transforme les couleurs sous la forme [0;1] vers [0;255]
# Car pygame nécéssite que les couleurs soient sous cette forme


while True:  # main game loop
    # Pour chaque évènements, si c'est un évènement "Exit" on quitte
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # - JUSTE POUR TESTER -
    # Pour chaque pixel de la fenêtre
    # On met la couleur à:
    # rouge: x/WIDTH
    # vert: y/HEIGHT
    # bleu: x+y/(WIDTH+HEIGHT)

    # NOTE: On utilises des couleur qui ont des valeurs de
    # 0 à 1 contrairement a d'autres cas où on a besoins
    # de couleurs de 0 à 255
    for x in range(WIDTH):
        for y in range(HEIGHT):
            DISPLAYSURF.set_at((x, y), Color(
                x/WIDTH, y/HEIGHT, (x+y)/(WIDTH*HEIGHT)).pygame_color())
    # On met à jour la fenêtre.
    pygame.display.update()
