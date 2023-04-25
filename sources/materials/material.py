from color import Color


class MaterialScatter:

    def __init__(self, scattered, color, bounce = True):
        self.scattered = scattered
        self.color = color
        self.bounce = bounce


# la classe parente du matériaux, en général un matériaux va avoir une fonction
# scatter qui donnes le rayon réfléchi et la couleur du rayon réfléchi
# donc un mirroir rouge va retourner une réflexion et une couleur rouge.
class Material:
    def __init__(self):
        pass

    def scatter(self, ray, record):
        return MaterialScatter(ray, Color(1, 0, 0))
