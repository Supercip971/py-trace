

# la classe couleur,
# elle contient 3 attributs: r, g, b
#  qui sont des nombres entre 0 et 1 (float)
# C'est plus utile pour les calculs et plus précis que les couleurs de 0 à 255 entiers
from math import sqrt
from vector import Vec3


class Color:

    def __init__(self, r=1.0, g=1.0, b=1.0):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __mul__(self, other):
        if (isinstance(other, Color)):
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)
        if (isinstance(other, Vec3)):
            return Color(self.r * other.x, self.g * other.y, self.b * other.z)

        return Color(self.r * other, self.g * other, self.b * other)

    def __str__(self):
        return str(f"({self.r}, {self.g}, {self.b})")

    def __div__(self, other):
        if (isinstance(other, Color)):
            return Color(self.r / other.r, self.g / other.g, self.b / other.b)
        return Color(self.r / other, self.g / other, self.b / other)
    __rmul__ = __mul__
    __rdiv__ = __div__
    # Pygame demandes des couleurs de 0 à 255 en entiers, alors on transforme
    #  les couleurs de 0 à 1 en couleurs de 0 à 255

    def tonemap_value(self, value):
        a = 2.51
        b = 0.03
        c = 2.43
        d = 0.59
        e = 0.14
        return (
            (value * (a * value + b)) / (value * (c * value + d) + e))

    def tonemapped(self):
        return Color(self.tonemap_value(self.r), self.tonemap_value(self.g), self.tonemap_value(self.b))
      #  return Color(min(sqrt((self.r)), 1.0), min(sqrt((self.g)), 1.0), min(sqrt((self.b)), 1.0))

    def pygame_color(self):
        return (
            int(self.r*255),
            int(self.g*255),
            int(self.b*255),
            255)
