import numpy as np
from fft_processing import *

def dxdy_conv(f, x, y, n=1):

    # calculate the sample spacing in the x and y directions
    dx = (np.amax(x) - np.amin(x)) / (f.shape[1] - 1)
    dy = (np.amax(y) - np.amin(y)) / (f.shape[0] - 1)

    dfdx = f
    dfdy = f

    for i in range(1, n+1):
        dfdy, _ = np.gradient(dfdy, dx, dy)
        _, dfdx = np.gradient(dfdx, dx, dy)

    return dfdx, dfdy

def dy_fft(f, x, y, n=1):

    fdata_p, mask = fft_pad_data(f)
    u, v = fft_wavenumbers(x, y, f.shape, mask.shape)

    dfdy = ifft_unpad_data(((1j * v) ** n) * fdata_p, mask, f.shape, mask.shape)

    return dfdy

def dx_fft(f, x, y, n=1):

    fdata_p, mask = fft_pad_data(f)
    u, v = fft_wavenumbers(x, y, f.shape, mask.shape)

    dfdx = ifft_unpad_data(((1j * u) ** n) * fdata_p, mask, f.shape, mask.shape)

    return dfdx
