import pygame
import sys
import argparse
from random import uniform


from world import World
from color import Color
from scenes.scenes import load_scene, list_scene
# initialise le système de pygame
import numpy as np

from render import render_ray

# gestion des arguments


def help_scene():
    print("Vous devez spécifier une scène à charger avec --scene")
    print("Exemple: main.py --scene basic")
    print("Les scènes disponibles sont :")
    list_scene()
    sys.exit(1)


parser = argparse.ArgumentParser(
    prog='py-trace', description="Un raytracer (open source) codé en python")
parser.add_argument("--scene", help="Le nom de la scène à charger")
parser.add_argument("--width", help="La largeur de l'image")
parser.add_argument("--height", help="La hauteur de l'image")

args = parser.parse_args()

# gestion de la scène
if not args.scene:
    help_scene()

world = load_scene(args.scene)

if world is None:
    print(f"la scène {args.scene} n'existe pas")
    help_scene()


# gestion de la fenêtre et de pygame

ratio = 16.0/9.0
height = args.height if args.height else 480
width = args.width if args.width else int(ratio*height)

ratio = float(width)/float(height)
pygame.init()

clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((width, height))

pygame.display.set_caption('py-trace')

# une table des pixels de l'écran
screen = np.array(
    [
        [Color(0.0, 0.0, 0.0) for i in range(height)]
        for i in range(width)
    ])
sample = 1.0


def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


while True:

    clock.tick(60)
    print(f"Le rendu de l'image n°({sample}) a prit: {clock.get_rawtime()}ms")
    # Pour chaque évènements, si c'est un évènement "Exit" on quitte
    # pour chaque pixel de l'écran
    # on fait un rendu de rayon de la scène
    for y in range(height):
        pygame.display.update()
        for x in range(width):
            check_event()
            color = render_ray(world, x, y, width, height)

            screen[x][y] = screen[x][y] + color

            # on fait la moyenne des couleurs
            # pour avoir une image plus nette au fil du temps
            # Donc, on fait la moyenne des couleurs des rayons envoyés
            col = (screen[x][y]) * (1.0/float(sample))

            # on affiche la couleur au pixel
            DISPLAYSURF.set_at(
                (x, y), col.tonemapped().pygame_color())

    sample += 1.0
