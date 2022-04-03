from ursina import *


class Effect:
    target = None
    target_attribute = None
    duration = 0
    modifier = 1

    def __init__(self, targ=None, targ_attribute=None, dur=0, modifier=1):
        self.target = targ
        self.target_attribute = targ_attribute
        self.duration = dur
        self.modifier = modifier

    def activate(self):
        t = 0
        while t < self.duration:
            self.target.target_attribute *= self.modifier
            t += time.dt
