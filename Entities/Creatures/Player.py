from ursina import *
from Entities.Magic import Spell
from Entities.Particles import PlayerCursor
from Entities.Particles.ParticleEmitter import ParticleEmitter
from Math import VectorMath


class Player(Entity):
    def __init__(self, mana=0, health=0, speed=3, defense=0, spells=None, particleSpawner=None, **kwargs):
        super().__init__(**kwargs)

        if spells is None:
            spells = [Spell.initial_spell]

        self.texture = "brick"
        self.mana_points = mana
        self.health_points = health
        self.speed_points = speed
        self.defense = defense
        self.model = "cube"
        self.scale = Vec3(sqrt(2)) * .5
        self.collider = "box"
        self.caster = raycaster
        self.cursor = PlayerCursor.PlayerCursor()
        self.spells = spells
        self.spell_index = 0
        self.particleSpawner = particleSpawner
        # self.light = PointLight(parent=self, shadows=True, position=Vec3(-10,0,0))

    def shoot_spell(self):
        # spell = self.spells[self.spell_index]
        # rot = VectorMath.normalize(self.rotation)
        # spell.cast(position=(self.position + (rot * 3)), rotation=VectorMath.normalize(self.rotation), caster=self)
        ps = ParticleEmitter(parent=scene, position=self.world_position + VectorMath.normalize(self.rotation) * 2,
                             rotation=self.rotation, scale=Vec3(.5))

    def open_menu(self):
        pass

    def update(self):
        hit_info = self.caster.raycast(self.world_position, self.rotation, ignore=(self,), distance=sqrt(2), debug=True)
        # if not hit_info.hit:
        self.x += held_keys['d'] * time.dt * self.speed_points
        self.y -= held_keys['s'] * time.dt * self.speed_points
        self.x -= held_keys['a'] * time.dt * self.speed_points
        self.y += held_keys['w'] * time.dt * self.speed_points
        # self.lookAt(self.cursor)

        self.rotation = VectorMath.normalize(Vec3(self.cursor.x, self.cursor.y, 0.1))

        camera.x = self.x
        camera.y = self.y
        self.cursor.position = (VectorMath.normalize(self.rotation) * 3)

    def input(self, key):
        if key == "left mouse down":
            self.shoot_spell()
        if key == "k":
            self.open_menu()

    def kill(self):
        destroy(self.cursor)
        destroy(self)
