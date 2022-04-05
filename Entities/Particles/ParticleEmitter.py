from ursina import *
import numpy as np
from Utilities import VectorMath

number_of_particles = 250  # keep this as low as possible


# ParticleEmitter is a class that creates a particle system

class ParticleEmitter(Entity):
    def __init__(self, number=number_of_particles, pos=Vec3(0), duration=.5, color=color.white, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.particles = np.array([Vec3(0) for i in range(number)])  # list of all particles
        self.particles_ = [Vec3(VectorMath.randomVec2d(), 0) * .05 for i in
                           range(number)]  # list of all the directions of the particles
        self.directions = np.array(self.particles_)  # list of all the directions of the particles
        self.frames = []  # list of all the frames of the particles
        self.t = 0  # time since the particle system was created
        for i in range(int(duration * 60)):
            self.particles += self.directions
            self.frames.append(copy(self.particles))

        self.model = Mesh(vertices=self.particles, mode='point', static=False, render_points_in_3d=True, thickness=.01)

        self.particle_type = 'circle'
        self.particle_size = 0.1
        self.particle_lifetime = duration
        self.particle_speed = 0.1
        self.particle_color = color
        self.particle_count = number
        self.particle_pos = pos

        self.particle_scale = Vec3(0.1, 0.1, 0.1),
        self.particle_scale_speed = Vec3(0, 0, 0),
        self.particle_scale_acceleration = Vec3(0, 0, 0),
        self.particle_texture = None

    def update(self):
        self.t += time.dt
        if self.t >= self.particle_lifetime:
            destroy(self)
            return

        self.model.vertices = self.frames[floor(self.t * 60)]
        self.model.generate()
