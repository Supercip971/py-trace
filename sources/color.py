

# la classe couleur,
# elle contient 3 attributs: r, g, b
# qui sont des nombres entre 0 et 1 (float)
# C'est plus utile pour les calculs et plus précis que les couleurs de 0 à 255 entiers
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
        if(isinstance(other, Color)):
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)
        return Color(self.r * other, self.g * other, self.b * other)

    # Pygame demandes des couleurs de 0 à 255 en entiers, alors on transforme
    # les couleurs de 0 à 1 en couleurs de 0 à 255
    def pygame_color(self):
        return (
            int(self.r*255),
            int(self.g*255),
            int(self.b*255),
            255)
