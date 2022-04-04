from ursina import *


class PlayerCursor(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.color = None
        self.parent = camera.ui
        self.model = "sphere"
        self.scale = Vec3(.0075)

    def update(self):
        # pass
        self.x = mouse.x
        self.y = mouse.y

    def input(self, key):
        if key == 'left down':
            self.color = color.red
        elif key == 'right down':
            self.color = color.green
        elif key == 'left up':
            self.color = color.white
        elif key == 'right up':
            self.color = color.white
