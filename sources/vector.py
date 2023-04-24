import math

import random


def dot(v1, v2):
    # v * v' = x * x' + y * y' + z * z'
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def cross(v1, v2):
    # v x v' = (y * z' - z * y', z * x' - x * z', x * y' - y * x')
    return Vec3(
        v1.y * v2.z - v1.z * v2.y,
        v1.z * v2.x - v1.x * v2.z,
        v1.x * v2.y - v1.y * v2.x)


class Vec3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(f"({self.x}, {self.y}, {self.z})")

    def __add__(self, other):
        # v_x = x + x'
        # v_y = y + y'
        # v_z = z + z'
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        # v_x = x - x'
        # v_y = y - y'
        # v_z = z - z'
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vec3(self.x * other, self.y * other, self.z * other)

    __rmul__ = __mul__

    def length(self):
        # |v| = sqrt(x^2 + y^2 + z^2)
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def inv_length(self):
        # 1 / |v| = 1 / sqrt(x^2 + y^2 + z^2)
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** -.5

    def squared_length(self):
        # |v|^2 = x^2 + y^2 + z^2
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def normalize(self):
        # v_x = x / |v|
        # v_y = y / |v|
        # v_z = z / |v|
        return self * self.inv_length()

    def distance(self, other):
        # d = |v - v'|
        return (self - other).length()

    def dot(self, other):
        # v * v' = x * x' + y * y' + z * z'
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle(self, other):
        dot_product = dot(self, other)
        len_self = self.length()
        len_other = other.length()
        return math.acos(dot_product / (len_self * len_other))

    # NOTE: ce n'est pas un bon moyen de calculer un vecteur aléatoire
    # il faudrait plutôt utiliser deux angles sur la sphère puis calculer
    # le vecteur qui correspond à ces angles
    @staticmethod
    def random_unit_vector():
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(-1, 1)

        return Vec3(x, y, z).normalize()

    @staticmethod
    def random_vector_in_hemisphere(normal):
        r = Vec3.random_unit_vector()

        # si r est dans la même direction que la normale, on le renvoie
        # sinon on le renvoie dans l'autre sens
        if (dot(r, normal) > 0.0):
            return r
        return -1.0 * r

def refract(v, n, ior):
    k = 1.0-  ior * ior * (1.0 - dot(v,n) * dot(v,n))
    if k <= 0.0:
        return Vec3(0,0,0)
    return ior * v - (ior * dot(n, v) + math.sqrt(k)) * n

