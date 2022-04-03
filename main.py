from ursina import *
from Entities import Player, Spell
from Entities.Enemy import Enemy
from World import Wall
from ursina.shaders import lit_with_shadows_shader
# camera.orthographic = True
camera.fov=90

def main():
    app = Ursina()
    player = Player.Player()
    entities = [Enemy(position=(-2,0,0)), Enemy(position=(2,0,0))]
    walls = []
    walls.append(Wall.Wall(-10, 10, 10, 10))

    # for i in (entities + walls):
    #     i.shader = lit_with_shadows_shader
    app.run()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
