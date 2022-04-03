from ursina import *


class PlayerCursor(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.color = None
        self.parent=camera.ui
        self.model="sphere"
        self.scale=Vec3(.0075)

    def update(self):
        self.x = mouse.x
        self.y = mouse.y