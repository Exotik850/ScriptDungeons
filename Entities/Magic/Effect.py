from ursina import *

from Entities.Particles.ParticleEmitter import ParticleEmitter


class Effect:
    target = None
    target_attribute = None
    duration = 0
    modifier = 1
    visuals = []

    def __init__(self, targ=None, targ_attribute=None, dur=0, modifier=1, color=color.white):
        self.target = targ
        self.target_attribute = targ_attribute
        self.duration = dur
        self.modifier = modifier
        self.color = color

    def particles(self, pos, color, duration, number):
        # Spawn a particle Emitter with the given parameters
        # pos: position of the emitter
        # color: color of the particles
        # duration: how long the emitter will last
        # number: how many particles will be spawned
        particle_emitter = ParticleEmitter(position=pos, color=color, duration=duration, number=number)

    def activate(self):
        t = 0
        while t < self.duration:
            self.target.target_attribute *= self.modifier
            self.particles(self.target.world_position, color=self.color, duration=self.duration, number=10)
            t += time.dt


initialEffect = Effect(targ_attribute='health_points', dur=.1, modifier=.95, color=color.red)
