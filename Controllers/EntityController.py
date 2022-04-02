from ursina import *

class EntityController:
    self.entities = []


    def __init__(self):
        self.entities = []

    def update(self):
        for entity in self.entities:
            entity.update()

