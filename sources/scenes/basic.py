from camera import Camera
from vector import dot
from shapes.sphere import Sphere

from shapes.box import Box
from vector import Vec3
from materials.lambertian import Lambertian
from materials.glass import Glass
from materials.metal import Metal
from world import World

from color import Color
from materials.light import Light

def load(): 

    mat2 = Metal(Color(0.5, 0.5, 0.5), 0.001)
    mat1_1 = Glass(Color(0.8, 0.3, 0.3))
    mat1_2 = Glass(Color(0.3, 0.8, 0.3))
    mat1_3 = Lambertian(Color(0.3, 0.3, 0.8))

    sphere1_1 = Sphere(Vec3(0, 0, -1), 0.5, mat1_1)
    # sphere1_2 = Sphere(Vec3(0, 0, -1), 0.5, mat1_2)
    box1_2 = Box(Vec3(-1, 0, -1) - Vec3(0.3, 0.3, 0.3),
             Vec3(-1, 0, -1) + Vec3(0.3, 0.3, 0.3), mat1_2)

    sphere1_3 = Sphere(Vec3(1, 0, -1), 0.5, mat1_3)

    sphere2 = Sphere(Vec3(0, -100.5, -1), 100, mat2)

    camera = Camera(Vec3(0, 0, 1), Vec3(0, 0, 0), Vec3(0, 1, 0), 90, 16/9)

    world = World(camera, Color(0.5, 0.7, 1))

    world.add_shape(sphere1_1)
    world.add_shape(box1_2)
    world.add_shape(sphere1_3)

    world.add_shape(sphere2)

    return world