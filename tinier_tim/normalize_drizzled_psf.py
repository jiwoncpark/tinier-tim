# -*- coding: utf-8 -*-
"""Rebinning the PSF

This script normalizes the drizzled PSF.

"""

import os
import numpy as np
import argparse
import astropy.io.fits as pyfits

def parse_args():
    """Parse command-line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', default='rebinned_dir', dest='save_dir', type=str,
                        help='directory where the unnormalized drizzled PSF is located.')
    args = parser.parse_args()
    return args

def main():
    #args = parse_args()
    unnormalized_path = 'dripsf.fits'
    psf = pyfits.open(unnormalized_path)[0].data.copy()
    psf /= np.sum(psf)  
    pyfits.PrimaryHDU(psf).writeto('drizzled_PSF.fits', overwrite=True)

if __name__ == '__main__':
    main()