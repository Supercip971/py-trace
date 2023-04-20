

class Shape:
    def __init__(self, material):
        self.material = material

    # Une fonction d'intersection qui prend en paramètre un rayon,
    # le point minimum du rayon et le point maximum du rayon
    # et qui retourne un booléen si oui ou non le rayon intersecte l'objet
    def intersect(self, ray, min, max):
        return False
