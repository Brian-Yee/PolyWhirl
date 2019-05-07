#!/usr/bin/env python3
"""
Polygon data class for holding helpful values.
"""
from dataclasses import dataclass  # back port of python3.7 class
import numpy as np


@dataclass  # pylint: disable=too-few-public-methods
class Polygon:
    """
    Polygon (more precisely an n-gon) centered about the origin.

    Arguments:
        radius: float
            Radius of circumscribing circle of n-gon
        thetas: np.array
            Values of thetas defining vertices.
    """

    radius: float
    thetas: np.array
