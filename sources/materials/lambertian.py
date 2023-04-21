
from materials.material import Material, MaterialScatter
from color import Color
from vector import Vec3, dot
from ray import Ray
# un lambertian est un matériau qui renvoie une réflexion uniforme
# dans toutes les directions de manière uniforme (cf: doc/matériaux.pdf).


class Lambertian(Material):

    # *techniquement* on parlerais plus d'albedo que de couleur
    def __init__(self, color):
        self.color = color

    def scatter(self, ray, record):
        reflection = (
            record.normal + Vec3.random_vector_in_hemisphere(record.normal)).normalize()

    #    col = self.color * abs(dot(record.normal, ray.direction))
        return MaterialScatter(Ray(record.point, reflection), self.color)
