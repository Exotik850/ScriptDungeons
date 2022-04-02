from ursina import *
from Entities import PlayerCursor, Effect, Spell

class Player(Entity):
    mana_points = 0
    health_points = 0
    speed_points = 5
    defense_points = 0
    cursor = None

    def __init__(self, mana=0, health=0, speed=3, defense=0):
        super().__init__()
        self.mana_points = mana
        self.health_points = health
        self.speed_points = speed
        self.defense = defense
        self.model = "cube"
        self.scale = Vec3(sqrt(2)) * .5
        self.collider = "box"
        self.caster = raycaster
        self.cursor = PlayerCursor.PlayerCursor()

    def shoot_spell(self):
        pass

    def open_menu(self):
        pass

    def update(self):
        hit_info = self.caster.raycast(self.world_position, self.rotation, ignore=(self,), distance=sqrt(2))
        if not hit_info.hit:
            self.x += held_keys['d'] * time.dt * self.speed_points
            self.y -= held_keys['s'] * time.dt * self.speed_points
            self.x -= held_keys['a'] * time.dt * self.speed_points
            self.y += held_keys['w'] * time.dt * self.speed_points

    def input(self, key):
        if key == "left mouse down":
            self.shoot_spell()
        if key == "k":
            self.open_menu()

