
from vector import Vec3, dot

from ray import Ray

# Un record, est un enregistrement d'une intersection entre un rayon et un objet.
# En effet, il va être retourné par la fonction d'intersection de l'objet, et
# il contiendra comme informations:
# - si il y a bel et bien eu une intersection
# - le point d'intersection
# - la normale au point d'intersection
# - la distance entre le point d'intersection et le point d'origine du rayon
# - la matière de l'objet


class Record:
    def __init__(self, hitted=False, ray=Ray(), point=Vec3(0, 0, 0), normal=Vec3(0, 0, 0), t=0.0, material=None):
        self.hitted = hitted
        self.point = point
        self.normal = normal
        self.t = t
        self.material = material
        self.in_ray = ray
        self.front = True

    def __str__(self):
        return "Record: (point: {}, normal: {}, t: {}, material: {})".format(self.point, self.normal, self.t, self.material)

    @staticmethod
    def no_intersect():
        return Record(False)

    def check_normal(self):

        # ici on fait que la normalle pointe toujours vers le point d'origine du rayon
        # Càd, si le rayon vient de l'extérieur, la normale pointe vers l'extérieur
        # et si le rayon vient de l'intérieur la normale serra inversé (pointe vers l'intérieur)
        # Comme cela, on sait si on est à l'intérieur ou à l'extérieur de l'objet.
        # Ce qui est nécéssaire pour des matériaux complexes comme le verre.
        if dot(self.in_ray.direction, self.normal) > 0:
            self.normal = self.normal * -1.0
            self.front = False
        else:
            self.front = True
        return self

    @staticmethod
    def do_intersect(ray, at, normal, t, material):
        return Record(True, ray,  at, normal, t, material).check_normal()
