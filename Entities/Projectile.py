from ursina import *


class Projectile(Entity):
    def __init__(self, size, direction, speed, effect, target, **kwargs):
        super().__init__(z=0.1, scale=size, **kwargs)
        self.direction = direction
        self.speed = speed
        self.effect = effect
        self.target = target
        self.caster = raycaster
        self.collider = "sphere"
        self.dead = False
        self.collider.on_collision = self.on_collision
        self.spell_caster=None

    def update(self):
        hit_info = self.caster.raycast(self.world_position, self.rotation, self.speed)
        if hit_info.hit:
            if hit_info.entity.name == 'Enemy':
                self.effect.target = hit_info.entity
                self.effect.activate()
                self.dead = True
        # else:
        self.position += self.direction * self.speed * time.dt

    def on_collision(self, other):
        if other.name == 'Enemy':
            other.health -= self.damage
            self.daed = True

