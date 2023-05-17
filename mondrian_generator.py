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
from itertools import product


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

    # randomly generate new x and y split coordinates
    xsplit = random.triangular(xmin, xmax)
    ysplit = random.triangular(ymin, ymax)

    # plot new splits as a horizontal and vertical line
    ax.axvline(xsplit, ymin, ymax, color="k", linewidth=8)
    ax.axhline(ysplit, xmin, xmax, color="k", linewidth=8)

    # if base case, color in the 4 subrectangles, plot, and return
    if n == 1:

        # choose 4 colors randomly: white, black, red, gold, or blue
        c = random.choices(
            ["w", "#28282B", "r", "gold", "#26619c"],
            weights=[6, 1, 1, 1, 1],  # white is the most likely choice
            k=4,
        )

        # get dimensions of the 4 subrectangles
        corner_coord = (xsplit, ysplit)
        widths = [xmax - xsplit, xmin - xsplit]
        heights = [ymax - ysplit, ymin - ysplit]

        # shade in the 4 subrectangles
        for i, (width, height) in zip(range(4), product(widths, heights)):
            ax.add_patch(Rectangle(corner_coord, width, height, color=c[i]))

        return ax

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


# paint the painting
paint_mondrian(3)
plt.show()
