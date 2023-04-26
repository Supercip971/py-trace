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
    mat_ground = Lambertian(Color(0.8, 0.8, 0.8))

    sphere1_1 = Sphere(Vec3(0, 0, -1), 0.5, mat1_1)
    # sphere1_2 = Sphere(Vec3(0, 0, -1), 0.5, mat1_2)
    glass_box = Box(Vec3(-1, 2.5948, 2.3681),
                    Vec3(1.0, 0.5948, 4.3681), Glass(Color(0.3, 0.8, 0.3)))

    world_box = Box(Vec3(4.45, 5.9601, -4.50),
                    Vec3(-4.45, -5.9601, 4.50), mat_ground)
    ground_1 = Box(Vec3(-4.5, 0.50, -5.1),
                   Vec3(4.5, -0.50, 2.278), mat_ground)
    ground_2 = Box(Vec3(-4.5, 0.50, -5.1),
                   Vec3(4.5, -0.50, 2.278), mat_ground)
    ground_3 = Box(Vec3(-4.5, 0.5, 3.94),
                   Vec3(4.5, -0.5, 4.56), mat_ground)
    light = Box(Vec3(-4.5, -0.73, 5.5),
                Vec3(4.5, -1.75, -1.933), Light(Color(1.0, 1.0, 1.0), 4))

   # sphere1_3 = Sphere(Vec3(1, 0, -1), 0.5, mat1_3)

   # sphere2 = Sphere(Vec3(0, -100.5, -1), 100, mat2)

    camera = Camera(Vec3(0, 1.6, -4), Vec3(0, 1.6, -3),
                    Vec3(0, 1, 0), 90, 16/9)

    world = World(camera, Color(0.5, 0.7, 1))

    world.add_shape(glass_box)
    world.add_shape(world_box)

    world.add_shape(ground_1)
    world.add_shape(ground_2)

    world.add_shape(ground_3)

    world.add_shape(light)

    return world
