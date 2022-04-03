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
        self.spell_caster = None

    def update(self):
        hit_info = self.caster.raycast(self.world_position, self.rotation, self.speed, ignore=(self.spell_caster,))
        if not hit_info.hit:
            self.position += self.rotation * self.speed * time.dt
        else:
            self.on_collision(hit_info.entity)

        # else:

    def on_collision(self, other):
        if other.name == 'Enemy':
            self.effect.target = other
            self.effect.activate()
            self.dead = True
