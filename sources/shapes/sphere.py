
from shapes.shape import Shape

from record import Record

from ray import Ray

from vector import dot

from math import sqrt


class Sphere(Shape):
    def __init__(self, center, radius, material):
        Shape.__init__(self, material)
        self.center = center
        self.radius = radius

    def intersect(self, ray, tmin, tmax):

        pprime = ray.origin - self.center

        a = dot(ray.direction, ray.direction)
        b = 2.0 * dot(ray.direction, pprime)

        c = dot(pprime, pprime) - self.radius * self.radius

        discriminant = b * b - 4 * a * c

        if discriminant > 0:
            # on prend les deux valeurs de t1 et t2, et on vérifie si elles sont
            # entre le point minimum et le point maximum du rayon
            t1 = (-b - sqrt(discriminant)) / (2.0 * a)
            t2 = (-b + sqrt(discriminant)) / (2.0 * a)

            # on prend la plus petite valeur de t1 et t2 et c'est la valeur 't'
            # de la droite, ainsi, si on l'applique à la droite, on obtient le
            # point d'intersection

            # la normale d'un cercle est le vecteur qui va du centre du cercle
            # au point d'intersection, on le normalize pour qu'il ait une
            # longueur de 1

            # FIXME: on ne prend pas en compte les cas où t2 est plus petit que t1

            t = t1

            if t < tmin or t > tmax:
                t = t2
                if t < tmin or t > tmax:
                    return Record.no_intersect()

            at = ray.point_at(t)

            normal = (at - self.center).normalize()
            return Record.do_intersect(ray, at, normal, t, self.material)

        return Record.no_intersect()
