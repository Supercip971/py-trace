
import scenes.basic
import scenes.demometal
import scenes.snowman
import scenes.demoglass
import scenes.light_demo


scenes_list = {
    "glass-demo": scenes.demoglass,
    "metal-demo": scenes.demometal,
    "light-demo": scenes.light_demo,
    "basic": scenes.basic,
    "snowman": scenes.snowman,
}


def list_scene():
    for scene in scenes_list.keys():
        print(f'- "{scene}"')


def load_scene(name):
    print(f"utilisation de la scene nommée: {name}")

    if not name in scenes_list:
        print("Erreur: Scene non supportée. ")
        return None

    return scenes_list[name].load()
