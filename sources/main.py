import pygame
import sys
from pygame.locals import *
from pygame import gfxdraw
from camera import Camera
from vector import Vec3
from color import Color
# initialise le système de pygame
pygame.init()

# bonjour 2

# La fenêtre aura 480 pixels de hauteur
# Et la largeur aura 16/9 de la hauteur soit ~853 pixels
RATIO = 16/9
HEIGHT = 1080
WIDTH = int(RATIO*HEIGHT)

WIDTH_R = range(WIDTH)
HEIGHT_R = range(HEIGHT)

clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('py-trace')


camera = Camera(Vec3(0, 0, 1), Vec3(0, 0, 0), Vec3(0, 1, 0), 90, RATIO)


# coloration du ciel venant de https://raytracing.github.io/books/RayTracingInOneWeekend.html
def sky(ray):
    unit_direction = ray.direction.normalize()
    t = 0.5*(unit_direction.y + 1)
    return Color(1, 1, 1)*(1-t) + Color(0.5, 0.7, 1)*t


while True:  # main game loop

    clock.tick(60)
    print(clock.get_rawtime())
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

    for y in HEIGHT_R:
        pygame.display.update()
        for x in WIDTH_R:
            ray = camera.get_ray(x/WIDTH, y/HEIGHT)

            gfxdraw.pixel(DISPLAYSURF, x, y, sky(ray).pygame_color())
      #      pygame.display.update((x, y, 1, 1))

        #    DISPLAYSURF.blit(DISPLAYSURF, (x, y))
      #  DISPLAYSURF.set_at((x, y), sky(ray).pygame_color())
    # On met à jour la fenêtre.
