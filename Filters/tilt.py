"""
    Tilt

    A Python program to calculate Tilt Angle and Hyperbolic Tilt Angle of a
    2d-array.

    Author: Joshua Poirier, 2017
"""

import numpy as np
from Filters.horizontal import dh
from Filters.vertical import dz

def tilt(f, x, y):
    """
    Calculates the tilt angle, defined in terms of the ratio between the first
    vertical derivative to the horizontal derivative of a given field. For
    further details, please refer to:

        Miller, H. G. and Singh V. 1994, Potential field tilt - a new concept
        for location of potential field sources, Journal of Applied Geophysics
        32 (1994) 213-217.

    The tilt is defined as:

        Theta = arctan(dfdz / dfdh)

        Where dfdz and dfdh are the first vertical and total
        horizontal derivatives respectively.

    Arguments:
        * f: 2d-array
            Array with the data.
        * x, y: 2d-arrays
            Arrays with the x and y coordinates of the data points.

    Returns:
        * theta: 2d-array
            Array containing the tilt angle of the data.
    """

    # calculate the horizontal and vertical derivatives
    dfdh = dh(f, x, y)
    dfdz = dz(f, x, y)

    # calculate the tilt (theta)
    theta = np.arctan(dfdz / dfdh)

    return theta

def hyperbolic_tilt(f, x, y, k=0.25):
    """
    Calculates the hyperbolic tilt angle. For further details please refer to:

        Cooper G. R. J. and Cowan D. R., 2006, Enhancing potential field data
        using filters based on the local phase. Computers & Geosciences 32,
        1585-1591.

        Cooper G. R. J., 2013, Reply to a discussion about the "Hyperbolic tilt
        angle method" by Zhou et al., Computers & Geosciences 52,
        496-497.

    The hyperbolic tilt is defined as:

        HTA = R ( arctanh( dfdz / (dfdh + k) ))

        Where R denotes the real component, dfdz and dfdh are the first vertical
        and horizontal derivatives respectively, and k is a positive constant
        stabilizing the HTA when the denominator of the equation is small.

    Arguments:
        * f: 2d-array
            Array with the data.
        * x, y: 2d-arrays
            Arrays with the x and y coordinates of the data points.

    Returns:
        * hta: 2d-array
            Array containing the hyperbolic tilt angle of the data.
    """

    # calculate the horizontal and vertical derivatives
    dfdh = dh(f, x, y)
    dfdz = dz(f, x, y)

    # calculate the hyperbolic tilt angle
    hta = np.real(np.arctanh(dfdz / (dfdh + k)))

    return hta
