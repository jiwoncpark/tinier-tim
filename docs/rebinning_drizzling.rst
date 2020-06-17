.. _rebinning_drizzling:

#############################
How to rebin and drizzle PSFs
#############################

1. Rebinning is like applying a low-pass filter, by which the pixels within the "kernel" become averaged (or summed--but the normalization doesn't matter as the PSF becomes normalized to unity in the end). Depending on the location of kernels within the bigger PSF grid, we can have various rebinned PSFs. See 1610.08504 for the details of rebinning. #TODO: link

Run

.. code-block:: sh

    $python tinier-tim/rebin_psf.py <path to the PSF fits file output by tiny3> --save_dir <desired working folder>
    // from our Tiny Tim tutorial,
    // python tinier-tim/rebin_psf.py test00.fits

This script creates 8 differently-binned images, named `non_drizzled_psf-[0-8].fits` in the <desired working folder>. If the `--save_dir` argument is not provided, it will create a folder named `rebinned_dir` instead. 

2. Initialize IRAF within the working folder.

.. code-block:: sh

    $cd <desired working folder>
    $mkiraf

When prompted for the terminal type, enter `xterm` for a standard Ubuntu system.    

This will output a config file `login.cl` accepted by IRAF. Check your device's information, and locate the section containing the list `tv`, `utilities`, `noao`, and `vo`. After `vo`, add `stsdas`, `analysis`, `dither` in separate lines.

3. 
#TODO: add description of `dri_psf.cl`

4. Run `drizzle.sh`.