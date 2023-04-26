
import scenes.basic
import scenes.demometal
import scenes.snowman
import scenes.demoglass


def load_scene(name="glass-demo"):
    print(f"utilisation de la scene nommée: {name}")
    if name == "glass-demo":
        return scenes.demoglass.load()
    elif name == "metal-demo":
        return scenes.demometal.load()
    elif name == "snowman":
        return scenes.snowman.load()
    elif name == "basic":
        return scenes.basic.load()
