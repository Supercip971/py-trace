
from shapes.shape import Shape

from ray import Ray

from vector import dot


class Sphere(Shape):
    def __init__(self, center, radius, material):
        Shape.__init__(self, material)
        self.center = center
        self.radius = radius

    def intersect(self, ray: Ray, min, max):

        pprime = ray.origin - self.center

        a = 1.0
        b = 2.0 * dot(ray.direction, pprime)
        c = dot(pprime, pprime) - self.radius * self.radius

        discriminant = b * b - 4 * a * c

        if discriminant > 0:
            # on prend les deux valeurs de t1 et t2, et on vérifie si elles sont
            # entre le point minimum et le point maximum du rayon
            t1 = (-b - discriminant**0.5) / (2.0 * a)
            t2 = (-b + discriminant**0.5) / (2.0 * a)
            print('t1: ', t1, 't2: ', t2, 'min: ', min, 'max: ', max)
            if t1 < max and t1 > min:
                return True
            if t2 < max and t2 > min:
                return True

            return False

        # Timplemente ici l'intersection avec une sphere
        return False
