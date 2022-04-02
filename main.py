from ursina import *
from Entities import Player, Spell
from World import Wall

camera.orthographic = True

def main():
    app = Ursina()
    player = Player.Player()
    entities = []
    walls = []
    walls.append(Wall.Wall(-10, 10, 10, 10))

    print(player.position)

    app.run()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
