"""
    Vertical v1.0

    A Python program to calculate the Vertical Derivative of a 2d-array.

    Author: Joshua Poirier, 2017
"""

import numpy as np
from horizontal import dxdy_conv
from fft_processing import *

def dz(f, x, y, n=1):

    if (n == 2):
        # calculate using Laplacian
        dfdz = dz_laplace(f, x, y)
    else:
        # calculate using FFT
        dfdz = dz_fft(f, x, y, n)

    return dfdz

def dz_laplace(f, x, y):
    n = 2

    dfdx, dfdy = dxdy_conv(f, x, y, 2)
    dfdz = - (dfdx + dfdy)

    return dfdz

def dz_fft(f, x, y, n=1):

    fdata_p, mask = fft_pad_data(f)
    u, v = fft_wavenumbers(x, y, f.shape, mask.shape)

    freq = (u**2 + v**2)**(0.5)

    dfdz = ifft_unpad_data(fdata_p * freq**n, mask, f.shape, mask.shape)

    return dfdz
