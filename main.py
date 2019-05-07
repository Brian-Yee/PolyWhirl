#!/usr/bin/env python3
"""
Main module containing spiral CLI and spiral drawing logic.
"""
import argparse
import numpy as np

from src.polygon import Polygon
from src import renderer


def main(num_sides, modulus, inner_radius_cutoff):
    """
    Draws polygon spiral artwork.

    Arguments:
        num_sides: int
            Number of sides to form an n-gon with.
        modulus: int
            Prints a spiral for every multiple of modulus arg.
        inner_radius_cutoff:
            Defines when a spiral should stop being generated towards the origin.
    """
    thetas = np.linspace(0, 2 * np.pi, num_sides)
    polygons = [Polygon(1, thetas)]

    while polygons[-1].radius > inner_radius_cutoff:
        dual_thetas = polygons[-1].thetas + np.diff(polygons[-1].thetas[:2]) / 2
        midpoint = [
            polygons[-1].radius * func(-polygons[-1].thetas[:2]).sum() / 2
            for func in (np.cos, np.sin)
        ]
        self_dual = Polygon(np.linalg.norm(midpoint), dual_thetas)

        polygons.append(self_dual)

    renderer.draw_polygons(polygons, modulus)


def parse_arguments():
    """
    Main CLI for interfacing with Polygon Spiral art generator.

    Returns:
        argparse.Namespace
            Argparse namespace containg CLI inputs.

    """
    parser = argparse.ArgumentParser(
        description=("Polygon Spiral art creater. Create spiral art!")
    )

    parser.add_argument(
        "polygon_sides",
        type=int,
        help="Number of sides for a polygon (more precisely an n-gon).",
    )

    parser.add_argument(
        "--modulus",
        dest="modulus",
        default=1,
        type=int,
        help="Print a spiral for every multiple of modulus arg.",
    )

    parser.add_argument(
        "--cutoff",
        dest="inner_radius_cutoff",
        default=0.01,
        type=float,
        help="Print a spiral for every multiple of modulus arg.",
    )

    return parser.parse_args()


def assert_argument_vals(args):
    """
    Various asserts to enforce CLI arguments passed are valid.

    Arguments:
        args: argparse.Namespace
            Argparse namespace containg CLI inputs.
    """
    assert args.polygon_sides >= 3, "Invalid amount of sides passed."
    assert args.modulus > 0, "Modulus must be a natural number."


if __name__ == "__main__":
    ARGS = parse_arguments()

    assert_argument_vals(ARGS)

    main(ARGS.polygon_sides + 1, ARGS.modulus, ARGS.inner_radius_cutoff)
