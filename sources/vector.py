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
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
 #      return str(f"({self.x}, {self.y}, {self.z})")
        return str("")
        
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
    v = v.normalize()
    n = n.normalize()
    cos_theta = min(1.0, dot(-1.0 * v, n))
    r_out_perp = (v + (n * cos_theta)) * ior
    r_out_parl = n * -math.sqrt(abs(1.0 - r_out_perp.squared_length()))
    return r_out_perp + r_out_parl


def reflect(v, n):
    return v - 2.0 * dot(n, v) * n


def schlick(angle, ior):
    r0 = (1.0 - ior) / (1.0 + ior)
    r0 = r0 * r0
    return r0 + (1.0 - r0) * (1.0 - angle) ** 5.0
