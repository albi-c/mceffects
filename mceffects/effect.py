from .math import *
from .output import Output


class Effect:
    """
    Effects
    """

    _resolution = 0.1

    @staticmethod
    def resolution(res: int | float):
        Effect._resolution = 1.0 / res

    @staticmethod
    def interp(from_: int | float, to: int | float):
        def internal(f: callable):
            v = from_
            while v <= to:
                f(v)
                v += Effect._resolution

        return internal

    @staticmethod
    def exp_interp(from_: int | float, to: int | float, speed: int | float):
        def internal(f: callable):
            v = from_
            while v <= to:
                f(v)
                v += v * (speed * Effect._resolution) + Effect._resolution

        return internal

    @staticmethod
    def line(from_: Vec3, to: Vec3):
        def internal(f: callable):
            diff = to - from_
            length = diff.length()
            d = 0
            while d <= length:
                f(from_ + diff * d / length)
                d += Effect._resolution

        return internal

    @staticmethod
    def clock(name: str, objective: str, start: int, end: int):
        def internal(f: callable):
            for t in range(start, end + 1):
                Output.write_modifier(lambda x: f"execute if score {name} {objective} matches {t} run {x}")
                f(t)
                Output.write_modifier()

        return internal
