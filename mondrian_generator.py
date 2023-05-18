#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: gracezhang

Recursive Mondrian Generator

"""

# import necessary modules
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
import numpy as np


# define function that generates the painting
def paint_mondrian(n=3, width=10, height=10):
    """
    Recursive Mondrian Generator

    - To create a Mondrian painting of recursive order n, run `paint_mondrian(n)` followed by `plt.show()`
    - The larger the choice of n, the more complicated the painting (more lines and rectangles).
    - Recommended 2 <= n <= 4.
    - Default canvas is square, but custom dimensions may be optionally specified.

    Parameters
    ----------
    n : int greater than or equal to 1, optional
        The recursive order of the painting. Default is 3.
    width: float, optional
        Width of the figure generated. Default is 10.
    height: float, optional
        Height of the figure generated. Default is 10.

    Returns
    -------
    fig: matplotlib figure object

    ax : matplotlib axes object

    """

    # initialize a new canvas
    fig, ax = plt.subplots(figsize=[width, height])
    ax.set_axis_off()  # turn off axis tick marks and labels

    # set width of the black lines to be drawn:
    # larger n or smaller figure dimensions correspond to smaller linewidth
    linewidth = 1.5 * min(width, height) * np.exp((1 - n) / 2.5)

    # helper function that makes the painting recursively
    def helper(n, xmin=0, xmax=1, ymin=0, ymax=1):

        # if this is the base case, color in the rectangle and return
        if n == 0:
            # choose a color randomly: white, black, red, gold, or blue
            c = random.choices(
                ["w", "#28282B", "r", "gold", "#26619c"],
                weights=[6, 1, 1, 1, 1],  # white is the most likely choice
            )

            # get dimensions of the rectangle
            corner_coord = (xmin, ymin)  # coords for bottom left corner
            width, height = xmax - xmin, ymax - ymin

            # shade in the rectangle
            ax.add_patch(Rectangle(corner_coord, width, height, color=c[0]))

            return None

        # otherwise randomly generate new x and y split coordinates
        # (triangular distribution gives better visual result than uniform)
        xsplit = random.triangular(xmin, xmax)
        ysplit = random.triangular(ymin, ymax)

        # plot new splits as a horizontal and vertical line
        ax.axvline(xsplit, ymin, ymax, color="k", linewidth=linewidth)
        ax.axhline(ysplit, xmin, xmax, color="k", linewidth=linewidth)

        # recurse on each of 4 subrectangles
        helper(n - 1, xmin=xmin, xmax=xsplit, ymin=ymin, ymax=ysplit)
        helper(n - 1, xmin=xsplit, xmax=xmax, ymin=ymin, ymax=ysplit)
        helper(n - 1, xmin=xmin, xmax=xsplit, ymin=ysplit, ymax=ymax)
        helper(n - 1, xmin=xsplit, xmax=xmax, ymin=ysplit, ymax=ymax)

        return None

    # call the recursive helper function
    helper(n)
    return fig, ax


# paint the painting
if __name__ == "__main__":
    fig, ax = paint_mondrian(3)
    plt.show()
