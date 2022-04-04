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
        self.projectiles = []

    def cast(self, position, rotation, caster):
        self.projectiles.append(Projectile.Projectile(size=1, speed=1, rotation=rotation, position=position,
                                                      model=self.projectile_model, target=self.target,
                                                      effect=Effect.initialEffect)
                                )
        self.projectiles[-1].spell_caster = caster
        for effect in self.initial_effects:
            effect.activate(self)

        def proj_update():
            for i in self.update_effects:
                i.activate(self)
        self.projectiles[-1].update_effects = self.update_effects
        self.projectiles[-1].damage_effects = self.damage_effects
        # self.projectile.update = proj_update

    def update(self):
        for projectile in self.projectiles:
            projectile.update()

            if projectile.dead:
                self.projectiles.remove(projectile)
                for effect in projectile.ending_effects:
                    effect.activate()



initial_spell = Spell(damage=[Effect.initialEffect])
