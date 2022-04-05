from ursina import *
from Utilities import VectorMath


class Projectile(Entity):
    def __init__(self, size, rotation, speed, target, duration, damage_effects=[], update_effects=[], ending_effects=[],
                 **kwargs):
        super().__init__(z=0.1, scale=size, **kwargs)
        self.rotation = rotation
        self.duration = duration
        self.t = 0
        self.speed = speed
        self.damage_effects = damage_effects
        self.update_effects = update_effects
        self.ending_effects = ending_effects
        self.target = target
        self.collider = 'sphere'
        self.dead = False
        self.spell_caster = None

    def kill(self):
        destroy(self)

    def update(self):
        if self.dead:
            for i in self.ending_effects:
                i.activate()
            self.kill()
        elif self.t > self.duration:
            self.dead = True
            self.kill()
        else:

            for effect in self.update_effects:
                effect.target = self
                effect.activate()

            hit_info = self.intersects()
            if not hit_info.hit:
                self.position += VectorMath.normalize(self.rotation) * self.speed * time.dt
            else:
                self.on_collision(hit_info.entity)
            self.t += time.dt

    def on_collision(self, other):
        if other.name == 'Enemy' or other.name == 'Player':
            print(f"{other.name} hit by {self.name}")
            for i in self.damage_effects:
                i.target = other
                i.activate()
            self.dead = True
