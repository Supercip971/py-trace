from camera import Camera
from vector import dot
from shapes.sphere import Sphere

from shapes.box import Box
from vector import Vec3
from materials.lambertian import Lambertian
from materials.glass import Glass
from materials.metal import Metal
from world import World
from random import random
from color import Color
from materials.light import Light


def load():

    camera = Camera(Vec3(0, 0, -2.0), Vec3(0, 0, 0), Vec3(0, 1, 0), 90, 16/9)

    world = World(camera, Color(0.8, 0.8, 0.8))

    black_mat = Lambertian(Color(0.1, 0.1, 0.1))
    white_mat = Lambertian(Color(0.6, 0.6, 0.6))
    for x in range(-5, 5):
        for y in range(-3, 3):
            mat = black_mat if (x+y) % 2 == 0 else white_mat

            box = Box(Vec3(x, y, 1.0),
                      Vec3(x+1.0, y+1.0, 2.0), mat)
            world.add_shape(box)

    blue_sphere = Sphere(Vec3(-0.9, 0, -1.0), 0.35,
                         Glass(Color(0.1, 0.1, 0.8)))

    red_sphere = Sphere(Vec3(0, 0, -1.0), 0.35, Glass(Color(0.8, 0.1, 0.1)))
    green_sphere = Sphere(Vec3(0.9, 0, -1.0), 0.35,
                          Glass(Color(0.1, 0.8, 0.1)))

    world.add_shape(blue_sphere)
    world.add_shape(red_sphere)
    world.add_shape(green_sphere)

 # #  wall_mat = Lambertian(Color(0.8, 0.8, 0.8))
 #   left_wall = Box(Vec3(-8, -10, -6.0), Vec3(-7, 10, 8.0),
 #                   Lambertian(Color(0.8, 0.1, 0.1)))
 #   right_wall = Box(Vec3(7, -10, -6.0), Vec3(8, 10, 8.0),
 #                    Lambertian(Color(0.1, 0.8, 0.1)))

 #   world.add_shape(left_wall)
 #   world.add_shape(right_wall)
 #  # mat = Lambertian(Color(0.1, 0.8, 0.1))
 #  # box = Box(Vec3(-8, -10, -8), Vec3(8+1.0, random()-2.0, 8+1.0), mat)
 #  # world.add_shape(box)

 #   for x in range(-3, 4):
 #       c = x + 3.0
 #       mat = Metal(Color(0.5, 0.5, 0.5), (float(c)/6.0)**2.0)
 #       sphere1_1 = Sphere(Vec3(float(x)*1.8, 1.0, -3.0),
 #                          1.5/2.0, mat)
 #       world.add_shape(sphere1_1)

 #   light = Light(Color(1.0, 1.0, 1.0), 3.0)
 #   # sphere1_2 = Sphere(Vec3(0, 0, -1), 0.5, mat1_2)
 #   light_box = Box(Vec3(0, 5, -1) - Vec3(7, 0.3, 7),
 #                   Vec3(0, 5, -1) + Vec3(7, 0.3, 7), light)
 #   world.add_shape(light_box)
 #   ground_box = Box(Vec3(0, -2.0, -1) - Vec3(7, 0.3, 7),
 #                    Vec3(0, -2.0, -1) + Vec3(7, 0.3, 7), ground_mat)
 #   world.add_shape(ground_box)

    return world
