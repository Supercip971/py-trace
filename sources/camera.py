from vector import Vec3, cross
from ray import Ray
import math


class Camera:
    def __init__(self, pos, target, up, fov, aspect_ratio):
        self.pos = (pos)
        self.target = (target)
        self.up = (up)
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.compute_params()

    def compute_params(self):
        forward = self.target - self.pos
        self.z_axis = forward.normalize()
        # La normale du plan formé depuis le dessus de la caméra et le devant de
        # la caméra est la droite/gauche de la caméra.
        right = cross(self.z_axis, self.up)
        self.x_axis = right.normalize()
        # le dessus est la normale du plan formé par le devant et la droite de
        # la caméra.
        self.y_axis = cross(self.x_axis, self.z_axis)

        self.half_height = math.tan(math.radians(self.fov) / 2)
        self.half_width = self.aspect_ratio * self.half_height

    # ray from camera to pixel
    def get_ray(self, u, v):
        # u et v sont des valeurs entre 0 et 1 qui représentent la position du
        # pixel sur l'écran

        z = self.z_axis
        x = self.x_axis * self.half_width * (2 * u - 1)
        y = self.y_axis * self.half_height * (2 * v - 1)
        direction = z - x - y
        return Ray(self.pos, direction)
