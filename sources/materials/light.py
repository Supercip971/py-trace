
from materials.material import Material, MaterialScatter
from color import Color
from vector import Vec3, dot, refract, reflect
from ray import Ray
from random import random
# un lambertian est un matériau qui renvoie une réflexion uniforme
# dans toutes les directions de manière uniforme (cf: doc/matériaux.pdf).


class Light(Material):

    # On gère la puissance comme une unité fictive. 
    def __init__(self, color, power = 1.0):
        self.color = color
        self.power = power

    def scatter(self, ray, record):
        # La réflexion est un peut inutiles car on passe l'attribut "Bounce" à False dans MaterialScatter
        # En effet, lorsque l'on touches une lumière, on ne continues pas le chemins. 
        refl = reflect(ray.direction, record.normal).normalize()
        c = record.point
        return MaterialScatter(Ray(c, refl), self.color * self.power, False)
