
from shapes.shape import Shape


class Sphere(Shape):
    def __init__(self, center, radius, material):
        Shape.__init__(self, material)
        self.center = center
        self.radius = radius

    def intersect(self, ray, min, max):
        # Timplemente ici l'intersection avec une sphere
        return False
