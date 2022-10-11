from .effect import Effect
from .particle import Particle
from .output import Output
from .math import *

import random

__version__ = "0.0.1"

# --- testing --- #

Effect.resolution(5)


# @Effect.interp(-5, 5)
# def xloop(x: float):
#     @Effect.interp(-5, 5)
#     def yloop(y: float):
#         Particle.flame(Vec3(x, math.sin(x) + math.cos(y), y).rel())


def spiral(h, winding: int | float = 1.5, angle_steps: int = 16):
    winding *= h

    @Effect.clock("time", "test_objective", 0, angle_steps)
    def time(t: int):
        @Effect.exp_interp(0, winding, 0.1)
        def loop(x: float):
            r = 1 - x / winding
            Particle.flame(Vec3(math.cos(x) * r, h * x / winding, math.sin(x) * r).rel().rot_y(t * 360 / angle_steps),
                           Vec3(0.1 * r, 0.1 * r, 0.1 * r), 0)
            Particle.soul_fire_flame(Vec3(-math.cos(x) * r, h * x / winding, -math.sin(x) * r).rel().rot_y(t * 360 / angle_steps),
                                     Vec3(0.1 * r, 0.1 * r, 0.1 * r), 0)


spiral(15)

# @Effect.interp(0, 2)
# def xloop(x: float):
#     Particle.flame(Vec3(math.cos(x), x, math.sin(x)).rel())
#     Particle.flame(Vec3(-math.cos(x), x, -math.sin(x)).rel())


Output.clipboard()
