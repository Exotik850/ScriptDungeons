from ursina import *
from Entities.Creatures import Player
from Entities.Creatures.Enemy import Enemy
from World import Wall

camera.orthographic = True


def main():
    app = Ursina()
    player = Player.Player()
    entities = [Enemy(position=(-2, 0, 0)), Enemy(position=(2, 0, 0))]
    walls = [Wall.Wall(-10, 10, 10, 10)]

    app.run()

if __name__ == '__main__':
    main()
