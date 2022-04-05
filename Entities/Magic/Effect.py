from ursina import *

from Entities.Particles.ParticleEmitter import ParticleEmitter


class Effect:
    target = None
    target_attribute = None
    duration = 0
    modifier = 1
    visuals = []

    def __init__(self, targ=None, targ_attribute=None, dur=0, modifier=1, color=color.white, number=0):
        self.target = targ
        self.target_attribute = targ_attribute
        self.duration = dur
        self.modifier = modifier
        self.number = number
        self.color = color

    def particles(self, pos, color, duration, number):
        # Spawn a particle Emitter with the given parameters
        # pos: position of the emitter
        # color: color of the particles
        # duration: how long the emitter will last (in seconds)
        # number: how many particles will be spawned
        particle_emitter = ParticleEmitter(position=pos, color=color, duration=duration, number=number)

    def activate(self):
        t = 0
        while t < self.duration:
            val = getattr(self.target, self.target_attribute) * self.modifier
            setattr(self.target, self.target_attribute, val)
            self.particles(self.target.world_position, color=self.color, duration=self.duration, number=self.number)
            t += time.dt


initialEffect = Effect(targ_attribute='health_points', dur=.1, modifier=.95, color=color.red)
