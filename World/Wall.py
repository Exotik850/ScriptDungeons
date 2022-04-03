from ursina import *


class Wall(Entity):
    w = 0
    h = 0

    def __init__(self, x=0, y=0, w=0, h=0):
        super().__init__()
        self.x = x
        self.z = y
        self.w = w
        self.h = h
        self.origin_z = .5
        self.scale = Vec3(self.w, self.h, 10)
        self.model = "cube"
        self.collider = "box"
