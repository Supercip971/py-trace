import pygame
import sys
from pygame.locals import *
from pygame import gfxdraw
from camera import Camera
from vector import dot
from shapes.sphere import Sphere

from shapes.box import Box
from vector import Vec3
from materials.lambertian import Lambertian
from materials.glass import Glass 


from random import uniform

from world import World
from color import Color
# initialise le système de pygame
import numpy as np


pygame.init()

#  bonjour 2

#  La fenêtre aura 480 pixels de hauteur
# Et la largeur aura 16/9 de la hauteur soit ~853 pixels
RATIO = 16.0/9.0
HEIGHT = 720
WIDTH = int(RATIO*HEIGHT)

WIDTH_R = range(WIDTH)
HEIGHT_R = range(HEIGHT)

clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('py-trace')


mat2 = Lambertian(Color(0.5, 0.5, 0.5))
mat1_1 = Glass(Color(0.8, 0.3, 0.3))
mat1_2 = Glass(Color(0.3, 0.8, 0.3))
mat1_3 = Lambertian(Color(0.3, 0.3, 0.8))


sphere1_1 = Sphere(Vec3(0, 0, -1), 0.5, mat1_1)
# sphere1_2 = Sphere(Vec3(0, 0, -1), 0.5, mat1_2)
box1_2 = Box(Vec3(-1, 0, -1) - Vec3(0.3, 0.3, 0.3),
             Vec3(-1, 0, -1) + Vec3(0.3, 0.3, 0.3), mat1_2)


sphere1_3 = Sphere(Vec3(1, 0, -1), 0.5, mat1_3)


sphere2 = Sphere(Vec3(0, -100.5, -1), 100, mat2)

camera = Camera(Vec3(0, 0, 1), Vec3(0, 0, 0), Vec3(0, 1, 0), 90, RATIO)

world = World(camera, Color(0.5, 0.7, 1))

world.add_shape(sphere1_1)
world.add_shape(box1_2)
world.add_shape(sphere1_3)

world.add_shape(sphere2)
# coloration du ciel venant de https://raytracing.github.io/books/RayTracingInOneWeekend.html


# def sky(ray):
#    unit_direction = ray.direction.normalize()
#    t = 0.5*(unit_direction.y + 1)
#    return Color(1, 1, 1)*(1-t) + Color(0.5, 0.7, 1)*t

sample = 1.0


screen = np.array([[Color(0.0, 0.0, 0.0) for i in range(HEIGHT)]
                  for i in range(WIDTH)])
while True:  # main game loop

    clock.tick(60)
    print(clock.get_rawtime())
    # Pour chaque évènements, si c'est un évènement "Exit" on quitte
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for y in HEIGHT_R:
        pygame.display.update()
        for x in WIDTH_R:
            ccolor = Color(0, 0, 0)
            for k in range(1):

                rx = (float(x) + uniform(0, 1)) / WIDTH
                ry = (float(y) + uniform(0, 1)) / HEIGHT
                ray = camera.get_ray(rx, ry)
                ray.direction = ray.direction.normalize()

                color = Color(1, 1, 1)
                for c in range(8):  #  16 rebonds
                    rec = world.intersect(ray)

                    if (rec.hitted):

                        scatter = rec.material.scatter(ray, rec)
                        ray = scatter.scattered
                        color = color * scatter.color
                     #   d = dot(rec.normal, ray.direction)
                    else:
                        color = color * world.background
                        break
                ccolor = ccolor + color

           # print(
           #     f"{x} {y} color: {color.r} {color.g} {color.b} sample: {screen[x][y]}")
            screen[x][y] = screen[x][y] + ccolor 

            col = (screen[x][y]) * (1.0/float(sample))
            DISPLAYSURF.set_at(
                (x, y), col.tonemapped().pygame_color())

    sample += 1.0
