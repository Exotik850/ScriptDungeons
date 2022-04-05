from ursina import *
from ursina.shaders import lit_with_shadows_shader

from Entities.Creatures import Player
from Entities.Creatures.Enemy import Enemy
from World import Wall

version = '.0.1b'

camera.orthographic = True

def main():
    app = Ursina()
    window.title = 'Script Dungeons Version ' + version
    window.borderless = False
    window.show_ursina_splash = True

    player = Player.Player()
    entities = [Enemy(position=(-2, 0, 0)), Enemy(position=(2, 0, 0))]
    walls = [Wall.Wall(-10, 10, 10, 10)]

    for i in entities + walls:
        i.shader = lit_with_shadows_shader

    app.run()

if __name__ == '__main__':
    main()
