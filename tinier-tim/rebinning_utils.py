#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Written by Xuheng Ding (@dartoon)
Refactored by Ji Won Park (@jiwoncpark)

"""
import os
import numpy as np
import astropy.io.fits as pyfits
#deltaPix = 0.13/4 #  pixel size in arcsec (area per pixel = deltaPix**2)

def expand_grid(grid, pad=10):
    """Add zero padding on two sides of the given grid

    Parameters
    ----------
    grid : 2D np.array
    pad : int

    Returns
    -------
    2D np.array
        the padded grid

    """
    grid = np.concatenate([grid, np.zeros([pad, grid.shape[1]])], axis=0)
    grid = np.concatenate([grid, np.zeros([grid.shape[0], pad])], axis=1) #expand the array
    return grid 

def rebin(image, rebinned_shape, factor):
    """

    Parameters
    ----------
    image : 2D np.array
        the larger PSF grid
    rebinned_shape : iterable with size 2
        shape of the image after rebinning
    factor : int
        smoothing factor

    Returns
    -------
    2D np.array
        the rebinned image with shape `rebinned_shape`

    """
    x_dim, y_dim = rebinned_shape # shape after coarse binning
    x_kernel_dim, y_kernel_dim = image.shape[0]//x_dim, image.shape[1]//y_dim # shape of each kernel, the pixels inside of which will be averaged (should be equal to [factor, factor])
    new_shape = x_dim, x_kernel_dim, y_dim, y_kernel_dim
    rebinned_image = image.reshape(new_shape).mean(axis=-1).mean(axis=1)*factor**2 # average across the dimensions of each kernel
    return rebinned_image

def load_psf_map(psf_path):
    """Load the PSF map output by Tiny Tim 3

    Parameters
    ----------
    psf_path : str or os.path object
        path to the PSF fits file

    Returns
    -------
    2D np.array
        the PSF map

    """
    psf_file = pyfits.open(psf_path) # change to PSF you made with tinytim3
    psf_data = psf_file[0].data
    return psf_data

def rebin_psf(psf_data, pattern_x=[0, 2, 0, 2, 1, 3, 1, 3], pattern_y=[0, 0, 2, 2, 3, 3, 1, 1], factor=4, save_dir='.', eps_x_start=0, eps_x_end=0, eps_y_start=0, eps_y_end=0):
    """Rebin the PSF at the specified kernel locations

    Parameters
    ----------
    psf_data : 2D np.array
    pattern_x : list of int
        the pixel offset along the x axis representing the blocking pattern within the larger PSF grid 
    pattern_y : list of int
    factor : int
        size of the rebinning kernel
    save_dir : str or os.path object
        directory in which the rebinned PSFs will be saved
    eps_x_start : int
        pixel offset applied when centering the PSF prior to rebinning. This value is known to affect the final drizzled image significantly.
    eps_y_start : int
    eps_x_end : int
    eps_y_end : int

    """
    cut_fd = int( (psf_data.shape[0] - ((int(psf_data.shape[0]/8*2) - 1)*4+3))/2 ) # TODO: ask Xuheng what this does
    centered_psf = psf_data[1+cut_fd+eps_x_start:-cut_fd+eps_x_end, 1+cut_fd+eps_y_start:-cut_fd+eps_y_end] + 0  # To change it from 251 to 247. (centers the PSF?)
    cut_len = (int(len(centered_psf)/factor))*factor # dimension of image made to be divisible by factor
    padded_psf = expand_grid(centered_psf)
    rebinned_x_dim, rebinned_y_dim = int(cut_len/factor), int(cut_len/factor) # shape after rebinning

    # Rebin the images
    n_bins = len(pattern_x)
    cut_out_psf = np.zeros([n_bins, cut_len, cut_len])
    image_bin_psf = np.zeros([n_bins, rebinned_x_dim, rebinned_y_dim])
    for i in range(n_bins):
        cut_out_psf[i, :, :] = padded_psf[pattern_x[i]:cut_len+pattern_x[i], pattern_y[i]:cut_len+pattern_y[i]] # the size before bin
        image_bin_psf[i, :, :] = rebin(cut_out_psf[i], [rebinned_x_dim, rebinned_y_dim], factor=factor)
        image_bin_psf[i, :, :] /= np.sum(image_bin_psf[i, :, :])  # normalize to unity
        save_path = os.path.join(save_dir, 'non_drizzled_psf-{0}.fits'.format(i+1))
        pyfits.PrimaryHDU(image_bin_psf[i]).writeto(save_path, overwrite=False)
        # TODO: separate into function
        # Edit the metadata so that the exposure time of each rebinned PSF is the same,
        # so that they get weighted equally in the drizzling process
        psf_to_update = pyfits.open(save_path, mode='update')
        psf_to_update[0].header["EXPTIME"] = 1
        psf_to_update.flush()
    return image_bin_psf
