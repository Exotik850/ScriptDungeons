from ursina import *

from Entities.Magic import Spell
from Entities.Particles import PlayerCursor, ParticleEmitter
from Utilities import VectorMath

player_model = load_model("Assets/Models/character.gltf")

class Player(Entity):
    def __init__(self, mana=0, health=10, speed=3, defense=0, spells=None, particleSpawner=None, **kwargs):
        super().__init__(**kwargs)

        if spells is None:
            spells = [Spell.initial_spell] * 2
        self.name = 'Player'
        self.mana_points = mana
        self.health_points = health
        self.speed_points = speed
        self.defense = defense
        self.on_menu = False
        self.model = 'cube'
        self.texture = 'brick'
        self.scale = Vec3(sqrt(2)) * .5
        self.collider = 'box'
        self.caster = raycaster
        self.cursor = PlayerCursor.PlayerCursor()
        self.spells = spells
        self.spell_index = 0
        self.particleSpawner = particleSpawner
        self.light = PointLight(parent=self, shadows=False, position=Vec3(-10, 0, 0))
        self.light.z = -5
        self.health_ui = Text(parent=self, text=str(self.health_points), size=1, color=color.red, position=(0, 0, -1))
        self.spell_ui = Text(parent=self, text=str(self.spell_index), size=1, color=color.red, position=(1, -1, -1))
        self.bg = Entity(parent=camera.ui, model='quad', texture="white_cube", scale=Vec3(10, 10, 1), z=1, visible=False)

    def shoot_spell(self):
        spell = self.spells[self.spell_index]
        rot = VectorMath.normalize(self.rotation)
        spell.cast(position=(self.position + (rot * 3)), rotation=VectorMath.normalize(self.rotation), caster=self)
        self.mana_points -= spell.mana_cost
        # ps = ParticleEmitter.ParticleEmitter(parent=scene, position=(self.world_position + self.rotation * 5, .5),
        #                                      color=color.red,
        #                                      duration=2)

    def open_menu(self):
        self.on_menu = not self.on_menu
        self.bg.visible = self.on_menu

    def update(self):
        # hit_info = self.caster.raycast(self.world_position, self.rotation, ignore=(self,), distance=sqrt(2), debug=False)
        # if not hit_info.hit:
        hit_info = self.intersects()
        if not hit_info.hit:
            self.x += held_keys['d'] * time.dt * self.speed_points
            self.y -= held_keys['s'] * time.dt * self.speed_points
            self.x -= held_keys['a'] * time.dt * self.speed_points
            self.y += held_keys['w'] * time.dt * self.speed_points

        # make rotation look at mouse
        self.rotation = VectorMath.normalize(Vec3(mouse.position.x, mouse.position.y, 0) - self.world_position)

        camera.x = self.x
        camera.y = self.y

        for spell in self.spells:
            spell.update()


    def input(self, key):
        if key == 'q':
            self.spell_index += 1
            if self.spell_index >= len(self.spells):
                self.spell_index = 0
            self.spell_ui.text = str(self.spell_index)

        if key == 'e':
            self.spell_index -= 1
            if self.spell_index < 0:
                self.spell_index = len(self.spells) - 1
            self.spell_ui.text = str(self.spell_index)
        if key == 'left mouse down':
            self.shoot_spell()
        if key == 'k':
            self.open_menu()

    def kill(self):
        destroy(self.cursor)
        destroy(self)

    def __str__(self):
        return 'Player'
