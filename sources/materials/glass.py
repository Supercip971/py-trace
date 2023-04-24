
from materials.material import Material, MaterialScatter
from color import Color
from vector import Vec3, dot, refract
from ray import Ray
# un lambertian est un matériau qui renvoie une réflexion uniforme
# dans toutes les directions de manière uniforme (cf: doc/matériaux.pdf).


class Glass(Material):

    # *techniquement* on parlerais plus d'albedo que de couleur
    def __init__(self, color, ior=1.5):
        self.color = color
        self.ior = ior 

    def scatter(self, ray, record):
        ef_ior = 1.0/ self.ior
        if( not record.front):
            ef_ior = self.ior
        refraction = refract(ray.direction, record.normal, ef_ior)
        return MaterialScatter(Ray(record.point, refraction), self.color)
