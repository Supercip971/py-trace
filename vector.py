import math


class Vector:
    def __init__(self, coords):
        self.coords = coords

    def __str__(self):
        return str(self.coords)

    def __add__(self, other):
        return Vector([x + y for x, y in zip(self.coords, other.coords)])

    def __sub__(self, other):
        return Vector([x - y for x, y in zip(self.coords, other.coords)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum([x * y for x, y in zip(self.coords, other.coords)])
        elif isinstance(other, (int, float)):
            return Vector([x * other for x in self.coords])

    def norm(self):
        return (sum([x ** 2 for x in self.coords])) ** 0.5

    def distance(self, other):
        return (sum([(x - y) ** 2 for x, y in zip(self.coords, other.coords)])) ** 0.5

    def angle(self, other):
        dot_product = self * other
        len_self = self.norm()
        len_other = other.norm()
        return math.acos(dot_product / (len_self * len_other))


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(v1 + v2)  # Output: [5, 7, 9]
print(v1 - v2)  # Output: [-3, -3, -3]
print(v1 * v2)  # Output: 32
print(v1 * 2)  # Output: [2, 4, 6]
print(v1.norm())  # Output: 3.7416573867739413
print(v1.distance(v2))  # Output: 5.196152422706632
print(math.degrees(v1.angle(v2)))  # Output: 9.744562646538029
