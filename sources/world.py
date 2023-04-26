from shapes.shape import Shape
from color import Color
from camera import Camera
from record import Record


class World:

    def __init__(self, camera, background):
     #   self.shapes = shapes
        self.camera = camera
        self.background = background
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    # ici on boucle sur chaque objet de la scène, et on regarde si le rayon
    # intersecte l'objet, si oui, on prend la valeur de t la plus petite
    # et on retourne le record de l'objet qui a été intersecté

    def intersect(self, ray):
        record = Record.no_intersect()
        tmin = 0.001
        tmax = 1000
        for shape in self.shapes:
            current_record = shape.intersect(ray, tmin, tmax)
            if (current_record.hitted and current_record.t < tmax and current_record.t > tmin):
                tmax = current_record.t
                record = current_record

        return record
