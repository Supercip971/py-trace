
> Note: nous recommandons de regarder la documentation sous le fichier PDF, car on utilises un markdown seulement supporté sur pandoc et non github pour les certaines fomulles mathématiques.
> Ce document répète également beaucoup de points qui sont expliqués dans le readme sans les démos et les images inutiles, c'est suelement de la doc.
# Documentation


Ici, on retrouvera la documentation du code, ainsi que les explications des algorithmes utilisés.

Ces explications démontre le processus que l'on a utilisé pour implémenter les fonctionnalités, tel que l'intersection entre une droite et une sphère, le tonemapping, une boite etc...

Cependant, si vous voulez une documentation du programme, c'est ici.
SInon c'est dans les fichiers `tonemapping.md`, `sphere.md`, ou `boite.md`.

## Execution du programme

Le programme se lance avec la commande `python main.py`.
Il est **nécéssaire** avoir installé la librairie `numpy` et `pygame`.

Si vous lancez le programme comme cela, il y aura une erreur, car il faut spécifier une scène à charger.
En effet les scènes sont décrites dans le fichier `scenes/scenes.py`. Et elles sont décrites dans le code.

Ainsi, pour sélectionner une scène il faut appeller le programme avec l'argument `--scene {nom de la scène}`,
si vous ne denez rien du tout, vous aurez une liste des scènes disponibles.

Vous pouvez également spécifier la taille de l'image avec `--width` et `--height`, par défaut c'est 480x850.

## Les scènes

On n'a pas de moyen de faire des scènes en temps réel comme on peut le faire avec blender par exemples, cependant on les représente dans le code:

```python
# On décrit la caméra, sa position, là ou elle regarde...
camera = Camera(Vec3(0, 0, 1), Vec3(0, 0, 0), Vec3(0, 1, 0), 90, 16/9)

# on définit le monde avec sa caméra et la couleur de fond
world = World(camera, Color(0.5, 0.7, 1))

# Un lambertien (matériaux équivalent à du papier, ou du plâtre)
lambert = Lambertian(Color(0.3, 0.3, 0.8))

# Un métal de couleur (0.5,0.5,0.5) et une rugosité de 0.001 (très lisse)
metallic = Metal(Color(0.5, 0.5, 0.5), 0.001)

# Nos deux sphères, avec respectivement, leur coordonées, rayon et matériaux
sphere = Sphere(Vec3(0, 0, -1), 0.5, lambert)
sphere2 = Sphere(Vec3(0, -100.5, -1), 100, metallic)

# Et finnalement on les rajoute au monde
world.add_shape(sphere)
world.add_shape(sphere2)
```

Et cela donnera ceci:
![resultat](../schema/demo-scene-construction.png)
