"""
    Horizontal

    A Python program to calculate Horizontal Derivatives of a 2d-array.

    Author: Joshua Poirier, 2017
"""

import numpy as np
from Filters.fft_processing import *

def dh(f, x, y):
    """
    Calculates the Total Horizontal Derivative of a 2d-array.

        THD = sqrt(dx^2 + dy^2)

    Arguments:
        * f: 2d-array
            Array with data to calculate derivative on.
        * x, y: 2d-arrays
            Array with the x and y coordinates of the data points.

    Returns:
        * dfdh: 2d-array
            Array containing the total horizontal derivative.
    """

    # calculate the x, y partial derivatives in spatial domain using convolution
    dfdx, dfdy = dxdy_conv(f, x, y, 1)

    # calculate total horizontal derivative
    dfdh = (dfdx**2 + dfdy**2)**0.5

    return dfdh

def dxdy_conv(f, x, y, n=1):
    """
    Calculates the n-th partial derivative of a 2d-array in the x and y
    directions.

    Arguments:
        * f: 2d-array
            Array with data to calculate derivatives on.
        * x, y: 2d-arrays
            Array with the x and y coordinates of the data points.
        * n: int
            Order of the derivative to be taken.

    Returns:
        * dfdx, dfdy: 2d-arrays
            Arrays with the n-th partial derivatives of data 'f' in the x and y
            directions respectively.
    """

    # calculate the sample spacing in the x and y directions
    dx = (np.amax(x) - np.amin(x)) / (f.shape[1] - 1)
    dy = (np.amax(y) - np.amin(y)) / (f.shape[0] - 1)

    # initialize partial derivatives to the data
    dfdx = f
    dfdy = f

    # perform n convolutions yielding the n-th partial derivatives
    for i in range(1, n+1):
        dfdy, _ = np.gradient(dfdy, dx, dy)
        _, dfdx = np.gradient(dfdx, dx, dy)

    return dfdx, dfdy

def dy_fft(f, x, y, n=1):
    """
    Calculate the n-th partial derivative of 'f' in the y-direction using the
    FFT method (calculated in the wavenumber domain).

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
            Array of the n-th partial derivative of the data in the y direction.
    """

    # calculate the Fourier Transform of data and associated wavenumbers
    F, mask = fft_pad_data(f)
    u, v = fft_wavenumbers(x, y, F.shape, mask.shape)

    # calculate the derivative in the wavenumber domain
    Fdfdy = ((1j * v) ** n) * F

    # apply the Inverse Fourier Transform to get derivative in spatial domain
    dfdy = ifft_unpad_data(Fdfdy, mask, f.shape, mask.shape)

    return dfdy

def dx_fft(f, x, y, n=1):
    """
    Calculate the n-th partial derivative of 'f' in the x-direction using the
    FFT method (calculated in the wavenumber domain).

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
        dfdx: 2d-array
            Array of the n-th partial derivative of the data in the x direction.
    """

    # calculate the Fourier Transform of the data and the wavenumbers
    F, mask = fft_pad_data(f)
    u, v = fft_wavenumbers(x, y, f.shape, mask.shape)

    # calculate the derivative in the wavenumber domain
    Fdfdx = ((1j * u) ** n) * F

    # apply the Inverse Fourier Transform to get derivative in spatial domain
    dfdx = ifft_unpad_data(Fdfdx, mask, f.shape, mask.shape)

    return dfdx
