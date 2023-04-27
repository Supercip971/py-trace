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


def put_white_sphere(coord, radius):
    mat = Lambertian(Color(0.8, 0.8, 0.8))
    return Sphere(coord, radius * 2.0, mat)


def put_black_sphere(coord, radius=0.066 / 2.0):
    mat = Lambertian(Color(0.0, 0.0, 0.0))
    return Sphere(coord, radius * 2.0, mat)


def load():

    camera = Camera(Vec3(0, 2.0, -19.819), Vec3(0, 2.0, 0.0),
                    Vec3(0, 1, 0), 15, 16/9)

    world = World(camera, Color(0.1, 0.1, 0.1))
    world.add_shape(put_white_sphere(Vec3(0, 0.405664, 0), 1 / 2.0))  # 000
    world.add_shape(put_white_sphere(Vec3(0, 1.6067, 0), 0.819 / 2.0))  # 001
    world.add_shape(put_white_sphere(Vec3(0, 2.6355, 0), 0.578/2.0))  # 002
    world.add_shape(put_black_sphere(Vec3(0.25273, 2.8699, -0.47055)))  # 003
    world.add_shape(put_black_sphere(Vec3(-0.28385, 2.8894, -0.44213)))  # 004
    world.add_shape(put_black_sphere(Vec3(-0.300, 2.5534, -0.49223)))  # 005
    world.add_shape(put_black_sphere(Vec3(-0.2373, 2.4607, -0.50182)))  # 006
    world.add_shape(put_black_sphere(Vec3(-0.140, 2.4094, -0.52022)))  # 007
    world.add_shape(put_black_sphere(Vec3(-0.02, 2.4075, -0.53731)))  # 008
    world.add_shape(put_black_sphere(Vec3(0.07, 2.42, -0.53894)))  # 009
    world.add_shape(put_black_sphere(Vec3(0.1465, 2.4368, -0.4273)))  # 010
    world.add_shape(put_black_sphere(Vec3(0.23, 2.49, -0.51596)))  # 011
    world.add_shape(put_black_sphere(Vec3(0.26, 2.5638, -0.51)))  # 012
    world.add_shape(put_black_sphere(Vec3(-0.02,  2.106,  -0.6428)))  # 013
    world.add_shape(put_black_sphere(Vec3(-0.01,  1.813,  -0.78823)))  # 014
    world.add_shape(put_black_sphere(Vec3(-0.012,  1.4459,  -0.811)))  # 015

    world.add_shape(put_white_sphere(
        Vec3(0.6685,  -0.43401,  -0.062591), 1 / 2.0))  # 016
    world.add_shape(put_white_sphere(
        Vec3(0.086147, -2.9711, -0.055), 3.296/2.0))  # 017
    world.add_shape(put_white_sphere(
        Vec3(-0.48733, -0.53142, -0.10152), 1/2.0))  # 018
    world.add_shape(put_white_sphere(
        Vec3(0.21733, -0.44912, -0.53142), 1/2.0))  # 019

    blue_light = Light(Color(1.0, 0.0, 0.0), 1.0)
    white_light = Light(Color(1.0, 1.0, 1.0), 3.0)

    # sphere1_2 = Sphere(Vec3(0, 0, -1), 0.5, mat1_2)
    light_box = Box(Vec3(7.77356, 1.396, 0) - Vec3(2.747, 2.0*2.747, 2.0*2.747),
                    Vec3(7.77356, 1.396, 0) + Vec3(2.747, 2.0*2.747, 2.0*2.747), blue_light)
    world.add_shape(light_box)

    light_box = Box(Vec3(-7.77356, 1.396, 0) - Vec3(2.747, 2.0*2.747, 2.0*2.747),
                    Vec3(-7.77356, 1.396, 0) + Vec3(2.747, 2.0*2.747, 2.0*2.747), white_light)
    world.add_shape(light_box)

    return world
