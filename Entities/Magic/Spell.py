from ursina import *
from Entities.Magic import Effect, Projectile


class Spell(Entity):
    def __init__(self, initial=[], update=[], damage=[], ending=[], proj="arrow", target=None):
        super().__init__()
        self.initial_effects = initial
        self.update_effects = update
        self.damage_effects = damage
        self.ending_effects = ending
        self.target = target
        self.projectile_model = proj
        self.projectile = None

    def cast(self, position, rotation, caster):
        self.projectile = Projectile.Projectile(size=1, speed=1, rotation=rotation, position=position,
                                                model=self.projectile_model, target=self.target,
                                                effect=Effect.initialEffect)
        self.projectile.spell_caster = caster
        for effect in self.initial_effects:
            effect.activate(self)

        def proj_update():
            for i in self.update_effects:
                i.activate(self)

        self.projectile.update_effects = self.update_effects
        # self.projectile.update = proj_update

    def update(self):
        if self.projectile:
            self.projectile.update()
            if self.projectile.dead:
                for effect in self.ending_effects:
                    effect.activate(self)
                destroy(self.projectile)


initial_spell = Spell(damage=[Effect.initialEffect])