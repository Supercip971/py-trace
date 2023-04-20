import math


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

    def normalize(self):
        # v_x = x / |v|
        # v_y = y / |v|
        # v_z = z / |v|
        return self * (1 / self.length())

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
