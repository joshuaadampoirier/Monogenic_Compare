"""
    Vertical

    A Python program to calculate Vertical Derivatives of a 2d-array.

    Author: Joshua Poirier, 2017
"""

import numpy as np
from Filters.horizontal import dxdy_conv
from Filters.fft_processing import *

def dz(f, x, y, n=1):
    """
    Calculate the n-th partial derivative of 'f' in the z-direction.

    Arguments:
        * f: 2d-array
            Array with the gridded data.
        * x, y: 2d-arrays
            Arrays with the x and y coordinates of the data points.
        * n: float
            Order of the derivative to be taken.
            Must be positive number, may be non-integer for fractional
            derivatives.

    Returns:
        dfdy: 2d-array
            Array of the n-th partial derivative of the data in the z direction.
    """

    if (n == 2):
        # calculate using Laplacian
        dfdz = dz_laplace(f, x, y)
    else:
        # calculate using FFT method
        dfdz = dz_fft(f, x, y, n)

    return dfdz

def dz_laplace(f, x, y):
    """
    Calculate the second partial derivative of 'f' in the z-direction using the
    Laplace's equation in the spatial domain.

    Laplace's equation:
        0 = d2f/dx2 + d2f/dy2 + d2f/dz2
        d2f/dz2 = - (d2f/dx2 + d2f/dy2)

    Arguments:
        * f: 2d-array
            Array with the gridded data.
        * x, y: 2d-arrays
            Arrays with the x and y coordinates of the data points.
        * n: float
            Order of the derivative to be taken.
            Must be positive number, may be non-integer for fractional
            derivatives.

    Returns:
        dfdz: 2d-array
            Array of the n-th partial derivative of the data in the z direction.
    """

    # calculate second-order horizontal derivatives using convolution
    dfdx, dfdy = dxdy_conv(f, x, y, 2)

    # calulate second-order vertical derivative using Laplace's equation
    dfdz = - (dfdx + dfdy)

    return dfdz

def dz_fft(f, x, y, n=1):
    """
    Calculate the n-th partial derivative of 'f' in the z-direction using the
    Laplace's equation in the wavenumber domain.

    Laplace's equation:
        0 = d2f/dx2 + d2f/dy2 + d2f/dz2
        d2f/dz2 = - (d2f/dx2 + d2f/dy2)

        Where d2f/dx2, d2f/dy2, and d2f/dz2 are the second-ordre partial
        derivatives of f in the x, y, and z directions respectively.

    Generalized in the wavenumber domain:
        F`(f) = (f)^n * F(f)

        Where F(f) is the amplitude at a frequency f, and n is the order of
        the derivative.

    Arguments:
        * f: 2d-array
            Array with the gridded data.
        * x, y: 2d-arrays
            Arrays with the x and y coordinates of the data points.
        * n: float
            Order of the derivative to be taken.
            Must be positive number, may be non-integer for fractional
            derivatives.

    Returns:
        dfdz: 2d-array
            Array of the n-th partial derivative of the data in the z direction.
    """

    # calculate Fourier Transform of data and associated wavenumbers
    F, mask = fft_pad_data(f)
    u, v = fft_wavenumbers(x, y, f.shape, mask.shape)

    # calculate the magnitude of the wavenumbers
    freq = (u**2 + v**2)**(0.5)

    # calculate the derivative in the wavenumber domain
    Fdfdz = F * freq**n

    # apply the Inverse Fourier Transform to get derivative in spatial domain
    dfdz = ifft_unpad_data(Fdfdz, mask, f.shape)

    return dfdz
