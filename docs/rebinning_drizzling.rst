.. _rebinning_drizzling:

#############################
How to rebin and drizzle PSFs
#############################

1. Rebinning is like applying a low-pass filter, by which the pixels within the "kernel" become averaged (or summed--but the normalization doesn't matter as the PSF becomes normalized to unity in the end). Depending on the location of kernels within the bigger PSF grid, we can have various rebinned PSFs.

See Fig 2 in `Ding et al 2016 <https://arxiv.org/abs/1610.08504>`_. Moving the blue frame around simulates dithering. This amounts to summing smaller pixels within each blue cell. If we do this 8 times, we end up with 8 rebinned PSFs.

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

3. Modify the drizzling config file, `dri_psf.cl`.

Note that drizzling can change the center flux by a factor of 4!
If the original PSF had 61 pixels of pixel size 0.13", we expect a finer PSF with target pixel size of 0.08" to have 99 pixels. In `dri_psf.cl`, the parameters `drizzle.outnx` and `drizzle.outny` should be greater than 99.

The `drizzle.scale` parameter is a fraction of post- and pre-drizzle pixel sizes, i.e. 0.08"/0.13" ~ 0.615.

Drizzling is slapping a lower-resolution PSF on a higher-resolution grid, defined by `drizzle.pixfrac`. So `drizzle.pixfrac` should be slightly greater than `drizzle.scale.`

4. Run `drizzle.sh`.
