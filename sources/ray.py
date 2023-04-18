
from vector import Vec3


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    # Transforme un point sur une droite, en fonction de t
    def point_at(self, t):
        return self.origin + t * self.direction
