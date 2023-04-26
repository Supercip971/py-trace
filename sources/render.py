
from camera import Camera
from vector import dot


from pygame.locals import *
from pygame import gfxdraw
from random import uniform


from world import World
from color import Color
from scenes.scenes import load_scene, list_scene


# fonction récurcive qui va calculer la couleur d'un rayon
# en fonction des objets qu'il touche
# a chaque fois, soit un rayon à touché une lumière et on retourne la couleur de la lumière
# soit il fait un rebond et on le fait rebondir
# cependant, pour éviter les rebonds infinis, on limite le nombre de rebonds (max_depth)
def ray_traverse(world, ray, max_depth, depth=0):
    rec = world.intersect(ray)

    # si le rayon n'a touché aucun objet, on retourne la couleur du fond
    if not rec.hitted:
        return world.background

    scatter = rec.material.scatter(ray, rec)

    # si on a atteint la profondeur maximale, on retourne du noir
    if depth > max_depth:
        return Color(0.0, 0.0, 0.0)

    # si le rayon rebondit, on le fait rebondir
    # sinon on retourne la couleur du rayon actuel
    # des matériaux comme les mirroirs vont rebondir,
    # mais les lumières vont retourner leur couleur sans faire de rebonds
    # (normalement la lumière ne rebondis pas sur une ampoule, vue qu'elle est
    # émise depuis cette ampoule)
    if scatter.bounce:
        return scatter.color * ray_traverse(world, scatter.scattered, max_depth, depth + 1)
    else:
        return scatter.color


# fait un rendu de la scène dans la fenêtre
# à partir des position x et y du pixel
def render_ray(world, x, y, width, height):
    # on prend une position aléatoire du pixel,
    # (donc on peut avoir pour les coordonées (1,2) -> (1.1,2.3), (1.2,2.1), (1.3,2.2) etc...
    #
    # ce qui provoque une sorte d'antialiasing naturel
    # Car on fait la moyenne des couleurs de plusieurs rayons
    rx = (float(x) + uniform(0, 1)) / width
    ry = (float(y) + uniform(0, 1)) / height

    # on prend les coordonées et on les transformes en rayon
    # depuis la caméra
    ray = world.camera.get_ray(rx, ry)
    ray.direction = ray.direction.normalize()

    return ray_traverse(world, ray, 8)
