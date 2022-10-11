from __future__ import annotations
import math

from .error import *


class Vec:
    """
    Vector
    """

    data: list[int | float]

    def __init__(self, data: list[int | float]):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return "[" + ", ".join([f"{val:.2f}" for val in self.data]) + "]"

    def __str__(self):
        return " ".join([f"{val:.2f}" for val in self.data])

    def length(self):
        return math.sqrt(sum([val * val for val in self.data]))

    def _operator(self, other: Vec | int | float, op: callable) -> Vec:
        if isinstance(other, Vec):
            return Vec([op(a, b) for a, b in zip(self.data, other.data)])

        return Vec([op(val, other) for val in self.data])

    def _ioperator(self, other: Vec | int | float, op: callable):
        if isinstance(other, Vec):
            self.data = [op(a, b) for a, b in zip(self.data, other.data)]

        self.data = [op(val, other) for val in self.data]

    def dot(self, other: Vec):
        return sum((self + other).data)

    def __add__(self, other: Vec | int | float):
        return self._operator(other, lambda a, b: a + b)

    def __sub__(self, other: Vec | int | float):
        return self._operator(other, lambda a, b: a - b)

    def __mul__(self, other: Vec | int | float):
        return self._operator(other, lambda a, b: a * b)

    def __truediv__(self, other: Vec | int | float):
        return self._operator(other, lambda a, b: a / b)

    def __floordiv__(self, other: Vec | int | float):
        return self._operator(other, lambda a, b: a // b)

    def __iadd__(self, other: Vec | int | float):
        return self._ioperator(other, lambda a, b: a + b)

    def __isub__(self, other: Vec | int | float):
        return self._ioperator(other, lambda a, b: a - b)

    def __imul__(self, other: Vec | int | float):
        return self._ioperator(other, lambda a, b: a * b)

    def __itruediv__(self, other: Vec | int | float):
        return self._ioperator(other, lambda a, b: a / b)

    def __ifloordiv__(self, other: Vec | int | float):
        return self._ioperator(other, lambda a, b: a // b)

    def __neg__(self):
        return Vec([-val for val in self.data])


class Vec3(Vec):
    """
    3-dimensional vector
    """

    is_relative: bool
    is_local: bool

    def __init__(self,
                 a: int | float | list[int | float] | None = None,
                 b: int | float | None = None,
                 c: int | float | None = None,
                 relative: bool = False,
                 local: bool = False):

        if isinstance(a, list):
            super().__init__(a)

        elif a is None:
            super().__init__([0, 0, 0])

        else:
            if b is not None and c is not None:
                super().__init__([a, b, c])

            else:
                super().__init__([a, a, a])

        self.is_relative = relative
        self.is_local = local

    def __repr__(self):
        return "[" + ", ".join([
            ("~" if self.is_relative else "^" if self.is_local else "") + f"{val:.2f}" for val in self.data
        ]) + "]"

    def __str__(self):
        return " ".join([
            ("~" if self.is_relative else "^" if self.is_local else "") + f"{val:.2f}" for val in self.data
        ])

    @property
    def x(self):
        return self.data[0]

    @x.setter
    def x(self, value):
        self.data[0] = value

    @property
    def y(self):
        return self.data[1]

    @y.setter
    def y(self, value):
        self.data[1] = value

    @property
    def z(self):
        return self.data[2]

    @z.setter
    def z(self, value):
        self.data[2] = value

    def rel(self) -> Vec3:
        if self.is_local:
            raise MathError(f"Trying to make a local vector relative")

        return Vec3(self.data.copy(), relative=True)

    def loc(self) -> Vec3:
        if self.is_relative:
            raise MathError(f"Trying to make a relative vector local")

        return Vec3(self.data.copy(), local=True)

    @staticmethod
    def relative() -> Vec3:
        return Vec3([0, 0, 0], relative=True)

    @staticmethod
    def local() -> Vec3:
        return Vec3([0, 0, 0], local=True)

    def _operator(self, other: Vec | int | float, op: callable) -> Vec3:
        if isinstance(other, Vec3):
            if (self.is_local and other.is_relative) or (self.is_relative and other.is_local):
                raise MathError("Trying to operate on a relative and a local vector")

            return Vec3(super()._operator(other, op).data, relative=(self.is_relative or other.is_relative),
                        local=(self.is_local or other.is_local))

        return Vec3(super()._operator(other, op).data, relative=self.is_relative, local=self.is_local)

    def _ioperator(self, other: Vec | int | float, op: callable):
        if isinstance(other, Vec3) and (self.is_local and other.is_relative) or (self.is_relative and other.is_local):
            raise MathError("Trying to operate on a relative and a local vector")

        super()._ioperator(other, op)

    def __neg__(self):
        return Vec3([-val for val in self.data], relative=self.is_relative, local=self.is_local)

    def rot_x(self, r: float):
        r /= 180
        r *= math.pi

        return Vec3([
            self.x,
            self.y * math.cos(r) - self.z * math.sin(r),
            self.y * math.sin(r) + self.z * math.cos(r)
        ], relative=self.is_relative, local=self.is_local)

    def rot_y(self, r: float):
        r /= 180
        r *= math.pi

        return Vec3([
            self.x * math.cos(r) + self.z * math.sin(r),
            self.y,
            -self.x * math.sin(r) + self.z * math.cos(r)
        ], relative=self.is_relative, local=self.is_local)

    def rot_z(self, r: float):
        r /= 180
        r *= math.pi

        return Vec3([
            self.x * math.cos(r) - self.y * math.sin(r),
            self.x * math.sin(r) + self.y * math.cos(r),
            self.z
        ], relative=self.is_relative, local=self.is_local)

class Vec4(Vec):
    """
    4-dimensional vector
    """

    def __init__(self,
                 a: int | float | list[int | float] | None = None,
                 b: int | float | None = None,
                 c: int | float | None = None,
                 d: int | float | None = None):

        if isinstance(a, list):
            super().__init__(a)

        elif a is None:
            super().__init__([0, 0, 0, 0])

        else:
            if b is not None and c is not None and d is not None:
                super().__init__([a, b, c, d])

            else:
                super().__init__([a, a, a, a])

    @property
    def x(self):
        return self.data[0]

    @x.setter
    def x(self, value):
        self.data[0] = value

    @property
    def y(self):
        return self.data[1]

    @y.setter
    def y(self, value):
        self.data[1] = value

    @property
    def z(self):
        return self.data[2]

    @z.setter
    def z(self, value):
        self.data[2] = value

    @property
    def w(self):
        return self.data[3]

    @w.setter
    def w(self, value):
        self.data[3] = value

