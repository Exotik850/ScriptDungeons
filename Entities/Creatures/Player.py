from ursina import *
from Entities.Magic import Spell
from Entities.Particles import PlayerCursor
from Entities.Particles.ParticleEmitter import ParticleEmitter
from Math import VectorMath


class Player(Entity):
    def __init__(self, mana=0, health=10, speed=3, defense=0, spells=None, particleSpawner=None, **kwargs):
        super().__init__(**kwargs)

        if spells is None:
            spells = [Spell.initial_spell]

        self.texture = "white_cube"
        self.mana_points = mana
        self.health_points = health
        self.health_ui = Text(parent=self, text=str(self.health_points), size=1, color=color.red, position=(0, 0, -.5))
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
        self.light = PointLight(parent=self, shadows=False, position=Vec3(-10,0,0))
        self.light.z = -5

    def shoot_spell(self):
        spell = self.spells[self.spell_index]
        rot = VectorMath.normalize(self.rotation)
        spell.cast(position=(self.position + (rot * 3)), rotation=VectorMath.normalize(self.rotation), caster=self)
        # ps = ParticleEmitter(parent=scene, position=self.world_position + VectorMath.normalize(self.rotation) * 2,
        #                      rotation=self.rotation, scale=Vec3(.5), color = color.red, duration=2)


    def open_menu(self):
        pass

    def update(self):
        # hit_info = self.caster.raycast(self.world_position, self.rotation, ignore=(self,), distance=sqrt(2), debug=False)
        # if not hit_info.hit:
        hit_info = self.intersects()
        if not hit_info.hit:
            self.x += held_keys['d'] * time.dt * self.speed_points
            self.y -= held_keys['s'] * time.dt * self.speed_points
            self.x -= held_keys['a'] * time.dt * self.speed_points
            self.y += held_keys['w'] * time.dt * self.speed_points
        # self.lookAt(self.cursor)

        self.rotation = VectorMath.normalize(Vec3(self.cursor.x, self.cursor.y, 0.1))
        self.health_ui.text = str(self.health_points)
        camera.x = self.x
        camera.y = self.y
        for spell in self.spells:
            spell.update()
        self.cursor.position = (VectorMath.normalize(self.rotation) * 3)

    def input(self, key):
        if key == "left mouse down":
            self.shoot_spell()
        if key == "k":
            self.open_menu()

    def kill(self):
        destroy(self.cursor)
        destroy(self)
