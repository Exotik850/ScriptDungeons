from ursina import *


class Projectile(Entity):
    speed = 10
    caster = None

    def initialize(self):
        pass

    def update(self):
        hit_info = self.caster.raycast(self.world_position, self.rotation, self.speed)
        if hit_info.hit:
            if hit_info.entity.name == 'Enemy':
                self.effect.target = hit_info.entity
                self.effect.activate()
                self.delete()
        else:
            self.position += self.direction * self.speed * time.dt

    def on_collision(self, other):
        if other.name == 'Enemy':
            other.health -= self.damage
            self.delete()

    def __init__(self, size, direction, speed, effect, target, **kwargs):
        super().__init__(texture='white', z=0.1, scale=size, **kwargs)
        self.direction = direction
        self.speed = speed
        self.effect = effect
        self.target = target
        self.caster = raycaster
        self.collider = "sphere"
        self.collider.on_collision = self.on_collision
