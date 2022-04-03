from ursina import *


class PlayerCursor(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model="sphere"
        self.scale=Vec3(.25)

    def update(self):
        self.x = mouse.x * (window.size.x / 2)
        self.y = mouse.y * (window.size.y / 2)

