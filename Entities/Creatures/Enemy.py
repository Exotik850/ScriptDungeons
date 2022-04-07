from ursina import *
from Entities.Creatures.Player import Player
from Utilities import Logger

class Enemy(Entity):
    def __init__(self, health=10, defense=0, damage=1, speed=.1, mana=None, **kwargs):
        super().__init__(**kwargs)
        self.logger = Logger.Logger()
        self.name = 'Enemy'
        self.model = 'sphere'
        self.texture = ''
        self.target = None
        self.scale = Vec3(.5)
        self.collider = 'sphere'
        self.color = color.red
        self.mana_points = mana
        self.damage = damage
        self.health_points = health
        self.speed_points = speed
        self.defense = defense
        self.origin_position = self.position
        self.health_ui = Text(text=f'HP: {self.health_points}', parent=self, color=color.white, size=1, scale=.5, position=Vec3(0, 0, -.5))



    def kill(self):
        self.logger.log(f'{self.name} has died')
        destroy(self)

    def update(self):
        if self.health_points <= 0:
            self.kill()
        hit_info = self.intersects()
        if hit_info.hit:
            if hit_info.entity.name == 'Player':
                self.on_collision(hit_info.entity)
        self.health_ui.text = f'HP: {self.health_points}'
        # rand_vel = Vec2(random.uniform(-1,1), random.uniform(-1,1))
        # self.x += rand_vel.x * self.speed
        # self.y += rand_vel.y * self.speed

    def on_collision(self, other):
        if isinstance(other, Player):
            other.health_points -= self.damage - other.defense
            self.health_points -= other.damage - self.defense
