#!/usr/bin/env python3
"""
Functions for drawing images.
"""
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np

plt.rcParams["figure.figsize"] = (20, 20)


def draw_polygons(polygons, modulus):
    """
    Draws polygon spiral artwork.

    Arguments:
        polygons: list(Polygon)
            Datastructures defining n-gons centered about the origin.
        modulus: int
            Prints a spiral for every multiple of modulus arg.
    """
    num_sides = len(polygons[0].thetas)
    viridis = cm.get_cmap("viridis", num_sides)
    viridis(np.linspace(0, 1, num_sides))

    poly_coords = [
        [polygon.radius * func(polygon.thetas) for polygon in polygons]
        for func in (np.cos, np.sin)
    ]

    if modulus == -1:
        iterations = range(0, num_sides, 1)
    else:
        iterations = range(1, num_sides, modulus)

    for i in iterations:
        neighbour = (i + 1) % num_sides
        spiral_coords = [
            [x[i] for x in coords[1:]] + [x[neighbour] for x in coords[::-1]]
            for coords in poly_coords
        ]
        plt.fill(*spiral_coords, color=viridis(i))

    plt.gca().set_aspect("equal")
    plt.gca().axis("off")

    canvas = FigureCanvasAgg(plt.gcf())
    canvas.draw()

    stream, (width, height) = canvas.print_to_buffer()
    img = np.fromstring(stream, np.uint8).reshape((height, width, 4))

    plt.imsave("images/spiral.png", _trim_border(img))


def _trim_border(img):
    """
    Trims white space border of a numpy image.

    Arguments:
        img: np.array
            Numpy image.

    Returns:
        img: np.array
            Numpy image with no white border space.
    """
    for i in range(img.shape[0]):
        if np.any(img[i, :, :] != 255):
            img = img[i:, :, :]
            break

    for i in range(img.shape[0] - 1, 0, -1):
        if np.any(img[i, :, :] != 255):
            img = img[: i + 1, :, :]
            break

    for i in range(img.shape[1]):
        if np.any(img[:, i, :] != 255):
            img = img[:, i:, :]
            break

    for i in range(img.shape[1] - 1, 0, -1):
        if np.any(img[:, i, :] != 255):
            img = img[:, : i + 1, :]
            break

    return img
