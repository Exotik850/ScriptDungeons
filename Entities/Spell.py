from ursina import *
from Entities import Projectile, Effect


class Spell(Entity):
    update_effects = []
    damage_effects = []
    ending_effects = []
    initial_effects = []
    target = None

    def __init__(self, initial=[], update=[], damage=[], ending=[], proj="sphere", target=None):
        super().__init__()
        self.initial_effects = initial
        self.update_effects = update
        self.damage_effects = damage
        self.ending_effects = ending
        self.target = target
        self.projectile_model = proj
        self.projectile = None

    def cast(self, location, direction, caster):
        self.projectile = Projectile.Projectile(size=1, speed=1, direction=direction, model=self.projectile_model, target=self.target, effect=Effect.initialEffect)
        self.projectile.location = location
        self.projectile.caster = caster
        for effect in self.initial_effects:
            effect.activate(self)

        def proj_update():
            for i in self.update_effects:
                i.activate(self)

        self.projectile.update_effects = self.update_effects
        self.projectile.update = proj_update


initial_spell = Spell(damage=[Effect.initialEffect])