from ursina import *
from Utilities import VectorMath


class Projectile(Entity):
    def __init__(self, size, rotation, speed, target, damage_effects=[], update_effects=[], ending_effects=[],
                 **kwargs):
        super().__init__(z=0.1, scale=size, **kwargs)
        self.rotation = rotation
        self.speed = speed
        self.damage_effects = damage_effects
        self.update_effects = update_effects
        self.ending_effects = ending_effects
        self.target = target
        self.caster = raycaster
        self.collider = "sphere"
        self.dead = False
        self.collider.on_collision = self.on_collision
        self.spell_caster = None

    def update(self):
        for effect in self.update_effects:
            effect.target = self
            effect.activate()

        hit_info = self.intersects()
        if not hit_info.hit:
            self.position += VectorMath.normalize(self.rotation) * self.speed * time.dt
        else:
            self.on_collision(hit_info.entity)


    def on_collision(self, other):
        if other.name == 'Enemy' or other.name == 'Player':
            for i in self.damage_effects:
                i.target = other
                i.activate()
            self.dead = True

