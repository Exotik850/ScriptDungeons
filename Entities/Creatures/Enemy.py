from ursina import *
from Entities.Creatures.Player import Player


class Enemy(Entity):
    def __init__(self, health=10, defense=0, damage=1, speed=.1, **kwargs):
        super().__init__(**kwargs)
        self.model = "sphere"
        self.scale = Vec3(.5)
        self.collider = 'circle'
        self.color = color.red
        self.health = health
        self.defense = defense
        self.damage = damage
        self.speed = speed

    def kill(self):
        destroy(self)

    def update(self):
        if self.health <= 0:
            self.kill()
        # rand_vel = Vec2(random.uniform(-1,1), random.uniform(-1,1))
        # self.x += rand_vel.x * self.speed
        # self.y += rand_vel.y * self.speed

    def on_collision(self, other):
        if isinstance(other, Player):
            other.health -= self.damage - other.defense
            self.health -= other.damage - self.defense
