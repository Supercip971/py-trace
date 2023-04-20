
from vector import Vec3


# Un record, est un enregistrement d'une intersection entre un rayon et un objet.
# En effet, il va être retourné par la fonction d'intersection de l'objet, et
# il contiendra comme informations:
# - si il y a bel et bien eu une intersection
# - le point d'intersection
# - la normale au point d'intersection
# - la distance entre le point d'intersection et le point d'origine du rayon
# - la matière de l'objet

class Record:
    def __init__(self, hitted=False, point=Vec3(0, 0, 0), normal=Vec3(0, 0, 0), t=0.0, material=None):
        self.hitted = hitted
        self.point = point
        self.normal = normal
        self.t = t
        self.material = material

    def __str__(self):
        return "Record: (point: {}, normal: {}, t: {}, material: {})".format(self.point, self.normal, self.t, self.material)

    @staticmethod
    def no_intersect():
        return Record(False)

    @staticmethod
    def do_intersect(at, normal, t, material):
        return Record(True, at, normal, t, material)
