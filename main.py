from ursina import *
from ursina.shaders import lit_with_shadows_shader
import configparser
from Entities.Creatures import Player
from Entities.Creatures.Enemy import Enemy
from World import Wall

version = '.0.1b'
camera.orthographic = True
options = {}

def load_config():
    global options
    config = configparser.ConfigParser()

    default_options = {
        "fullscreen": False,
        "width": 800,
        "height": 600,
        "vsync": True,
        "show_ursina_splash": False,
        "show_fps": False,
        "borderless": False
    }

    try:
        config.read("config.cfg")
        for key, item in config['ScriptDungeons'].items():
            options[key] = eval(item)
    except:
        print('No config file found, creating one...')

        for key, item in default_options.items():
            config.set('ScriptDungeons', key, str(item))

        with open('config.cfg', 'w') as configfile:
            config.write(configfile)
            options = default_options


def main():
    global options
    app = Ursina()
    load_config()
    print(options)

    window.title = 'Script Dungeons Version ' + version
    window.screen_resolution = (options['width'], options['height'])
    for item, key in options.items():
        setattr(window, item, key)

    player = Player.Player()
    entities = [Enemy(position=(-2, 0, 0)), Enemy(position=(2, 0, 0))]
    walls = [Wall.Wall(-10, 10, 10, 10)]

    for i in entities + walls:
        i.shader = lit_with_shadows_shader

    app.run()


if __name__ == '__main__':
    main()
