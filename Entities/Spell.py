from ursina import *


class Spell(Entity):
    update_effects = []
    damage_effects = []
    ending_effects = []
    initial_effects = []
    target = None

    def __init__(self, initial=[], update=[], damage=[], ending=[], target=None):
        super().__init__()
        self.initial_effects = initial
        self.update_effects = update
        self.damage_effects = damage
        self.ending_effects = ending
        self.target = target
