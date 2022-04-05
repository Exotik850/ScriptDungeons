from ursina import *
from Entities.Magic import Effect, Projectile
from Utilities.Logger import Logger


class Spell(Entity):
    def __init__(self, name=None, initial=[], update=[], damage=[], ending=[], proj='sphere', range=10, target=None, cost=0):
        super().__init__()
        self.name = name
        self.initial_effects = initial
        self.update_effects = update
        self.damage_effects = damage
        self.ending_effects = ending
        self.mana_cost = cost
        self.target = target
        self.range = range
        self.projectile_model = proj
        self.projectiles = []
        self.logger = Logger()

    def cast(self, position, rotation, caster):
        self.projectiles.append(Projectile.Projectile(size=.25, speed=1, rotation=rotation, position=position,
                                                      model=self.projectile_model, target=self.target, duration=self.range,
                                                      effect=Effect.initialEffect)
                                )
        self.projectiles[-1].spell_caster = caster
        for effect in self.initial_effects:
            effect.activate(self)


        self.projectiles[-1].update_effects = self.update_effects
        self.projectiles[-1].damage_effects = self.damage_effects
        self.logger.log(str(caster) + " cast " + self.name + " on " + str(self.target))

    def update(self):
        for projectile in self.projectiles:
            projectile.update()
            if projectile.dead:
                self.projectiles.remove(projectile)
                for effect in self.ending_effects:
                    effect.activate(self)
                return



initial_spell = Spell(name="Spark", damage=[Effect.initialEffect])
