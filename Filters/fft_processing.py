import numpy as np

def fft_wavenumbers(x, y, shape_dat, shape_pdat):
    """
    Calculates the u, v Fourier wavenumbers in the x and y
    directions respectively.

    Arguments:
        * x, y: 2d-arrays
            Arrays with the x and y coordinates of the data points
        * shape_dat: tube = (ny, nx)
            The number of data points in each direction before padding.
        * shape_pdat: tube = (ny, nx)
            The number of data points in each direction after padding.

    Returns:
        * u, v: 2d-arrays
            x and y Fourier wavenumbers
    """

    # calculate the sample spacing in the x and y directions
    dx = (np.amax(x) - np.amin(x)) / (shape_dat[1] - 1)
    dy = (np.amax(y) - np.amin(y)) / (shape_dat[0] - 1)

    # calculate the DFT sample frequencies
    fx = np.fft.fftfreq(shape_pdat[1], dx)
    fy = np.fft.fftfreq(shape_pdat[0], dy)

    # project the wavenumbers onto the grid
    u, v = np.meshgrid(fx, fy)

    return u, v

def fft_pad_data(data, n_pts=10, mode='linear_ramp'):
    """
    Pad data and calculate FFT.

    Arguments:
        * data: 2d-arrays
            Array with the gridded data
        * n_pts: int
            Number of array points to pad the data with. Defaults to 10.
        * mode: str
            Padding mode: {
                'linear_ramp': Pads with a linear ramp between edge value and 0.
                'edge': Pads with the edge values of the data.
                'mean': Pads with the mean value of all the data.
            }

    Returns:

        * fpad: 2d-array
            The FFT of the padded data
        * mask: 2d-array
            Location of the padding points: {
                True: data points.
                False: padded points.
            }
    """

    # pad the data
    data_p = np.pad(data, n_pts, mode)

    # create a data mask
    mask = np.zeros_like(data_p, dtype=bool)
    mask[n_pts:n_pts+np.shape(data)[0], n_pts:n_pts+np.shape(data)[1]] = True

    # compute the FFT
    fpdat = np.fft.fft2(data_p)

    return fpdat, mask

def ifft_unpad_data(data_p, mask, shape_dat, shape_pdat):
    ifft_data = np.real(np.fft.ifft2(data_p))
    data = ifft_data[mask]

    return np.reshape(data, shape_dat)
