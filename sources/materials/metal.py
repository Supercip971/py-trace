
from materials.material import Material, MaterialScatter
from color import Color
from vector import Vec3, dot, refract, reflect
from ray import Ray
from random import random
# un lambertian est un matériau qui renvoie une réflexion uniforme
# dans toutes les directions de manière uniforme (cf: doc/matériaux.pdf).


class Metal(Material):

    # *techniquement* on parlerais plus d'albedo que de couleur
    # La roughness est la granularité
    def __init__(self, color, roughness):
        self.color = color
        self.rougness = roughness

    def scatter(self, ray, record):
        # on calcule une réflexion du rayon par rapport à la normale
        # on prend une normale qui change par rapport à la granularité donnée.
        # C'est comme un mur rugueux, où à la place d'avoir qu'une seule face plate
        # on a pleins de faces de différentes directions

        refl = reflect(ray.direction, record.normal).normalize()

        refl = (refl +
                Vec3.random_vector_in_hemisphere(record.normal) * (self.rougness)).normalize()

     #   refl = reflect(ray.direction, normal).normalize()
        c = record.point - ray.direction * 0.01
        return MaterialScatter(Ray(c, refl), self.color)
