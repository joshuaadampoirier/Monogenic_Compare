import numpy as np

def fft_wavenumbers(x, y, shape_dat, shape_pdat):
    """
    Calculates the u, v Fourier wavenumbers in the x and y directions
    respectively.

    Arguments:
        * x, y: 2d-arrays
            Arrays with the x and y coordinates of the data points.
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

def fft_pad_data(f, n_pts=10, mode='linear_ramp'):
    """
    Pad data and calculate FFT.

    Arguments:
        * f: 2d-arrays
            Array with the gridded data.
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
            The FFT of the padded data.
        * mask: 2d-array
            Location of the padding points: {
                True: data points.
                False: padded points.
            }
    """

    # pad the data
    fp = np.pad(f, n_pts, mode)

    # create a data mask
    mask = np.zeros_like(fp, dtype=bool)
    mask[n_pts:n_pts+np.shape(f)[0], n_pts:n_pts+np.shape(f)[1]] = True

    # compute the FFT
    F = np.fft.fft2(fp)

    return F, mask

def ifft_unpad_data(F, mask, shape_dat):
    """
    Calculates the Inverse Fourier Transform of a padded 2d-array and masks the
    data to the original shape.

    Arguments:
        * F: 2d-array
            Array with the padded data in the wavenumber domain.
        * mask: 2d-array
            Location of padding points: {
                True: Points to be kept.
                False: Points to be removed.
            }
        * shape_dat: tube = (ny, nx)
            The number of data points in each direction before padding.

    Returns:
        * data: 2d-array
            The unpadded spatial-domain data.
    """

    # calculate the Inverse Fourier Transform
    fp = np.real(np.fft.ifft2(F))

    # mask the data to the original shape
    f = np.reshape(fp[mask], shape_dat)

    return f
