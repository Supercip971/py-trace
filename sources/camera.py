from vector import Vec3
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
        right = self.z_axis.cross(self.up)
        self.x_axis = right.normalize()
        # le dessus est la normale du plan formé par le devant et la droite de
        # la caméra.
        self.y_axis = self.x_axis.cross(self.z_axis)

        self.half_height = math.tan(math.radians(self.fov) / 2)
        self.half_width = self.aspect_ratio * self.half_height

    # ray from camera to pixel
    def get_ray(self, u, v):
        x = self.half_width * (2*u - 1)
        y = self.half_height * (2*v - 1)
        direction = x * self.x_axis + y * self.y_axis - self.z_axis
        return Ray(self.pos, direction)
