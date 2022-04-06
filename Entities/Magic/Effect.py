from ursina import *
import math
from Entities.Particles.ParticleEmitter import ParticleEmitter


class Effect:
    target = None
    target_attribute = None
    duration = 0
    modifier = 1
    visuals = []

    def __init__(self, targ=None, targ_attribute=None, modifier=1, color=color.white, number=0, name=None):
        self.target = targ
        self.target_attribute = targ_attribute
        self.modifier = modifier
        self.number = number
        self.name = name
        self.color = color

    def particles(self, pos, color, duration, number):
        # Spawn a particle Emitter with the given parameters
        # pos: position of the emitter
        # color: color of the particles'
        # duration: how long the emitter will last (in seconds)
        # number: how many particles will be spawned
        particle_emitter = ParticleEmitter(position=pos, color=color, duration=duration, number=number)

    def activate(self):
        print(f"Activating {self.name}")
        val = round(getattr(self.target, self.target_attribute) * self.modifier, 2)
        setattr(self.target, self.target_attribute, val)
        self.particles(self.target.world_position, color=self.color, duration=self.duration, number=self.number)


initialEffect = Effect(targ_attribute='scale', modifier=1.5, color=color.red, name='initialEffect')
