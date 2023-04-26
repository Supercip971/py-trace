
# Documentation

Ici, on retrouveras la documentation du code, ainsi que les explications des algorithmes utilisés.

Ces explications démontre le processus que l'on a utilisé pour implémenter les fonctionnalités, tel que l'intersection entre une droite et une sphère, le tonemapping, une boite etc...

Cependant, si vous voulez une documentation du programme, c'est ici.
SInon c'est dans les fichiers `tonemapping.md`, `sphere.md`, ou `boite.md`.

## Execution du programme

Le programme se lance avec la commande `python main.py`.
Nous recommandons avoir installé la librairie `numpy` et `pygame`.

Si vous lancez le programme comme cela, il y aura une erreur, car il faut spécifier une scène à charger.
En effet les scènes sont décrites dans le fichier `scenes/scenes.py`. Et elles sont décrites dans le code.

Ainsi, pour sélectionner une scène il faut appeller le programme avec l'argument `--scene {nom de la scène}`,
si vous ne denez rien du tout, vous aurez une liste des scènes disponibles.

Vous pouvez également spécifier la taille de l'image avec `--width` et `--height`, par défaut c'est 480x850.

## Création de scène