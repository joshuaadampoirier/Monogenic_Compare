"""
    Total Derivative

    A Python program to calculate the Total Derivatives of a 2d-array.

    Note: This derivative is commonly called the Analytic Signal.

    Author: Joshua Poirier, 2017
"""

import numpy as np
from Filters.horizontal import dxdy_conv
from Filters.vertical import dz

def dt(f, x, y):
    """
    Calculates the total derivative (often called the Analytic Signal). This is
    the vector sum of the partial derivatives in the x, y, and z directions.

        Total Derivative = sqrt(dfdx^2 + dfdy^2 + dfdz^2)

        Where dfdx, dfdy, and dfdz are the first-order partial derivatives in
        the x, y, and z directions respectively.

    Arguments:
        * f: 2d-array
            Array with the data.
        * x, y: 2d-arrays
            Arrays with the x and y coordinates of the data points.

    Returns:
        * dt: 2d-array
            Array with the total derivative.
    """

    # calculate partial derivatives in the x, y, and z directions
    dfdx, dfdy = dxdy_conv(f, x, y)
    dfdz = dz(f, x, y)

    # calculate the total derivative
    dt = (dfdx**2 + dfdy**2 + dfdz**2)**0.5

    return dt
