

from shapes.shape import Shape

from record import Record

from ray import Ray


from vector import dot, Vec3

import math


class Box(Shape):
    def __init__(self,  min_pos, max_pos, material):
        Shape.__init__(self, material)
        self.min_p = min_pos
        self.max_p = max_pos

    def normal_get(self, ray, t):
        p = ray.point_at(t)
        # on cherches l'axe et la face correspondant au point d'intersection,
        # il y a surement une manière beaucoup plus intelligent de le faire.
        if abs(p.x - self.min_p.x) < 0.001:
            return Vec3(-1, 0, 0)
        elif abs(p.x - self.max_p.x) < 0.001:
            return Vec3(1, 0, 0)
        elif abs(p.y - self.min_p.y) < 0.001:
            return Vec3(0, -1, 0)
        elif abs(p.y - self.max_p.y) < 0.001:
            return Vec3(0, 1, 0)
        elif abs(p.z - self.min_p.z) < 0.001:
            return Vec3(0, 0, -1)
        elif abs(p.z - self.max_p.z) < 0.001:
            return Vec3(0, 0, 1)
        else:
            return Vec3(0, 0, 0)

    def intersect(self, ray, tmin, tmax):

        tx_0 = (self.min_p.x - ray.origin.x) / ray.direction.x
        tx_1 = (self.max_p.x - ray.origin.x) / ray.direction.x

        tmin = max(tmin, min(tx_0, tx_1))
        tmax = min(tmax, max(tx_0, tx_1))
        if tmin > tmax:
            return Record.no_intersect()

        ty_0 = (self.min_p.y - ray.origin.y) / ray.direction.y
        ty_1 = (self.max_p.y - ray.origin.y) / ray.direction.y

        tmin = max(tmin, min(ty_0, ty_1))
        tmax = min(tmax, max(ty_0, ty_1))
        if tmin > tmax:
            return Record.no_intersect()

        tz_0 = (self.min_p.z - ray.origin.z) / ray.direction.z
        tz_1 = (self.max_p.z - ray.origin.z) / ray.direction.z

        tmin = max(tmin, min(tz_0, tz_1))
        tmax = min(tmax, max(tz_0, tz_1))

        if tmin > tmax:
            return Record.no_intersect()

        return Record.do_intersect(ray, ray.point_at(tmin), self.normal_get(ray, tmin), tmin, self.material)
