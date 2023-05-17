#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gracezhang

Recursive Mondrian Generator

- To create a Mondrian painting of order n, 
run `paint_mondrian(n)` followed by `plt.show()`

- The larger the choice of n, the more complicated the painting

- recommended n between 2 and 4

"""

# import necessary modules
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random


# define function that recursively paints the painting
def paint_mondrian(n, ax=None, xmin=0, xmax=1, ymin=0, ymax=1):
    """
    Recursive Mondrian Generator

    - To create a Mondrian painting of order n, run `paint_mondrian(n)` followed by `plt.show()`
    - The larger the choice of n, the more complicated the painting (more lines and rectangles)
    - recommended n between 2 and 4

    Parameters
    ----------
    n : int, greater than or equal to 1
        the recursive order of the painting.
        This is the only input which should be specified by the user.

    ax : matplotlib axes object, optional
        Used in recursion, should not be specified manually by user.

    xmin : float, optional
        left coordinate of current subcanvas.
        Used in recursion, should not be specified manually by user.

    xmax : float, optional
        right coordinate of current subcanvas.
        Used in recursion, should not be specified manually by user.

    ymin : float, optional
        bottom coordinate of current subcanvas.
        Used in recursion, should not be specified manually by user.

    ymax : float, optional
        top coordinate of current subcanvas.
        Used in recursion, should not be specified manually by user.

    Returns
    -------
    ax : matplotlib axes object

    """

    # if this is the outermost recursion layer, initialize a new square canvas
    if ax is None:
        fig, ax = plt.subplots(figsize=[10, 10])
        ax.set_axis_off()  # turn off axis tick marks and labels

    # if this is the base case, color in the rectangle and return
    if n == 0:
        # choose a color randomly: white, black, red, gold, or blue
        c = random.choices(
            ["w", "#28282B", "r", "gold", "#26619c"],
            weights=[6, 1, 1, 1, 1],  # white is the most likely choice
        )

        # get dimensions of the rectangle
        corner_coord = (xmin, ymin)  # coords for bottom left corner
        width = xmax - xmin
        height = ymax - ymin

        # shade in the rectangle
        ax.add_patch(Rectangle(corner_coord, width, height, color=c[0]))

        return None

    # randomly generate new x and y split coordinates
    # (triangular distribution gives better aesthetic result than uniform)
    xsplit = random.triangular(xmin, xmax)
    ysplit = random.triangular(ymin, ymax)

    # plot new splits as a horizontal and vertical line
    ax.axvline(xsplit, ymin, ymax, color="k", linewidth=8)
    ax.axhline(ysplit, xmin, xmax, color="k", linewidth=8)

    # recurse on each of 4 subrectangles
    paint_mondrian(
        n - 1, ax=ax, xmin=xmin, xmax=xsplit, ymin=ymin, ymax=ysplit
    )
    paint_mondrian(
        n - 1, ax=ax, xmin=xsplit, xmax=xmax, ymin=ymin, ymax=ysplit
    )
    paint_mondrian(
        n - 1, ax=ax, xmin=xmin, xmax=xsplit, ymin=ysplit, ymax=ymax
    )
    paint_mondrian(
        n - 1, ax=ax, xmin=xsplit, xmax=xmax, ymin=ysplit, ymax=ymax
    )

    return ax


# paint the painting
ax = paint_mondrian(3)
plt.show()
