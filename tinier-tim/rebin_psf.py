# -*- coding: utf-8 -*-
"""Rebinning the PSF

This script rebins the given PSF and stores the rebinned PSFs in the specified directory.

"""

import os
import argparse
import rebinning_utils

def parse_args():
    """Parse command-line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('psf_file_path', help='path to the fits file of the PSF to be rebinned')
    parser.add_argument('--factor', default=4, dest='factor', type=int,
                        help='size of rebinning kernel in number of pixels')
    parser.add_argument('--save_dir', default='rebinned_dir', dest='rebinned_dir', type=str,
                        help='directory in which the rebinned (non-drizzled) PSFs will be stored. If it does not exist, it will be created.')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    input_psf = rebinning_utils.load_psf_map(args.psf_file_path)
    if not os.path.exists(args.rebinned_dir):
        os.makedirs(args.rebinned_dir)
    _ = rebinning_utils.rebin_psf(input_psf, factor=args.factor, save_dir=args.rebinned_dir)

if __name__ == '__main__':
    main()