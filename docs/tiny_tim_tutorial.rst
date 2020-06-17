.. _tiny_tim_tutorial:

##################################
How to simulate PSFs with Tiny Tim
##################################

:ref:`step_1`

:ref:`step_2`

:ref:`step_3`

.. _step_1:

Step 1
======

The following sequence of commands will generate a PSF with the requested conditions. First, choose the name of the PSF, e.g. `psf0`

.. code-block:: sh

    $tiny1 psf0

When prompted, choose the desired instrument, e.g. 23 for the WFC3/IR channel.

.. code-block:: sh

    $ 23

For the position, we can choose the middle-ish pixel, i.e.

.. code-block:: sh

    $550 550

Next is the filter passband corresponding to the instrument, e.g. F160W for the WFC3/IR channel we chose.

.. code-block:: sh

    $f160w

We will then select the spectrum from which 13 wavelengths will be used to generate the PSF. Let's select one from a list.

.. code-block:: sh

    $1

A table of stars and their colors will be printed. Let's choose AOV.

.. code-block:: sh

    $7

For the PSF diameter, simply choose a reasonable diameter that will fit within your frame, e.g.

.. code-block:: sh

    $5

I don't know what the focus, secondary mirror despace parameter does. Let's just not use it.

.. code-block:: sh

    $0

Choose a rootname of PSF image files.

.. code-block:: sh

    $test

The first step is complete! 

.. _step_2:

Step 2
======

The second step is simply calling `tiny2` followed by the PSF name.

.. code-block:: sh

    $tiny2 psf0

`tiny2` will tell you that the intermediate PSF dimensions are 108 by 108, and proceed to compute the PSF at 13 wavelengths. It outputs an intermediate file called `<root name>00_psf.fits`, e.g. `test00_psf.fits` in our case, as well as a template optional parameter file required by `tiny3` called `<root name>.tt3`, e.g. `test.tt3`. The intermediate PSF is an undistorted PSF with the pixel size of 0.046241 arcsec.

.. _step_3:

Step 3
======

`tiny3` resamples and distorts the intermediate PSF from `tiny2`. If we run:

.. code-block:: sh

    $tiny3 psf0

with no arguments, the output PSF, named `<root_name>00.fits` (`test00.fits` in our case), is 46 by 46 pixels. But say we want to apply a super-resolution (subsampling) factor of 4. Then run:

.. code-block:: sh

    $tiny3 psf0 sub=4

This will yield a PSF with 184 (46 times 4) pixels on each side. 

Now we are ready to rebin. See :ref:`rebinning_drizzling`.