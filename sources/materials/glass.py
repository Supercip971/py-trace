
from materials.material import Material, MaterialScatter
from color import Color
from vector import Vec3, dot, refract, reflect, schlick
from ray import Ray
from random import random
from utils import remap
# un lambertian est un matériau qui renvoie une réflexion uniforme
# dans toutes les directions de manière uniforme (cf: doc/matériaux.pdf).


class Glass(Material):

    # *techniquement* on parlerais plus d'albedo que de couleur
    def __init__(self, color, ior=1.5):
        self.color = color
        self.ior = ior

    def scatter(self, ray, record):
        ef_ior = 1.0 / self.ior
        if (not record.front):
            ef_ior = self.ior

        refraction = refract(ray.direction, record.normal, ef_ior)
        p2 = record.point - ray.direction * 0.01

        if (random() < schlick(dot(-1.0 * ray.direction, record.normal), ef_ior)):
          #  color = self.color
            angle = abs(dot(-1.0 * ray.direction, record.normal))
            color = self.color * angle + Color(1.0, 1.0, 1.0) * (1.0 - angle)
            return MaterialScatter(Ray(p2, reflect(ray.direction, record.normal)), color)
        p2 = record.point + ray.direction * 0.01

        return MaterialScatter(Ray(p2, refraction), self.color)
