
import scenes.basic
import scenes.demometal

def load_scene(name="basic"):
    print(f"utilisation de la scene nommée: {name}")
    if name == "basic": 
        return scenes.demometal.load()
    elif name == "snowman":
        return scenes.basic.load()