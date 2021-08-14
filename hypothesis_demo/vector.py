# From: Fluent Python 1st edition
# customized for our purposes

import math
import numbers
import reprlib
from typing import Sequence

EQ_DIMENSIONS_MSG = "%s applies only to vectors of equal dimensions."
UNSUPPORTED_TYPE_MSG = "Unsupported type: %s."


class Vector:
    def __init__(self, components: Sequence):
        self._components = tuple(components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        return "Vector({})".format(components)

    def __iter__(self):
        return iter(self._components)

    def __str__(self):
        return str(self._components)

    def __abs__(self):
        return math.sqrt(sum(component * component for component in self))

    def __len__(self):
        return len(self._components)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError(EQ_DIMENSIONS_MSG % "Addition")
        return Vector(a + b for a, b in zip(self, other))

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Vector(comp * other for comp in self)
        elif isinstance(other, Vector):
            return self.elementwise_mul(other)
        else:
            raise ValueError(UNSUPPORTED_TYPE_MSG % str(type(other)))

    def elementwise_mul(self, other):
        if len(self) != len(other):
            raise ValueError(EQ_DIMENSIONS_MSG % "Elementwise multiplication")
        return Vector(a * b for a, b in zip(self, other))

    def __matmul__(self, other):
        if len(self) != len(other):
            raise ValueError(EQ_DIMENSIONS_MSG % "Dot product")
        return sum(a * b for a, b in zip(self, other))

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = "{.__name__} indices must be integers"
            raise TypeError(msg.format(cls))

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __bool__(self):
        return any(self)
