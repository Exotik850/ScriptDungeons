from ursina import *
import numpy as np

number_of_particles = 250  # keep this as low as possible


class ParticleEmitter(Entity):
    def __init__(self, duration=1.5, **kwargs):
        self.t = 0
        self.duration = duration
        self.points = np.array([Vec3(0) for i in range(number_of_particles)])
        self.particles = [Vec3(random.random() - .5, random.random() - .5, random.random() - .5) * .05 for i in
                          range(number_of_particles)]
        self.directions = np.array(self.particles)
        self.frames = []

        for i in range(60 * 6):
            self.points += self.directions
            self.frames.append(copy(self.points))
        super().__init__(
            model=Mesh(vertices=self.points, mode='point', static=False, render_points_in_3d=True, thickness=.01),
            **kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.t += time.dt
        if self.t >= self.duration:
            destroy(self)
            return

        self.model.vertices = self.frames[floor(self.t * 60)]
        self.model.generate()
