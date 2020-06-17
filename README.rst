==========
tinier-tim
==========

.. image:: https://readthedocs.org/projects/tinier-tim/badge/?version=latest
    :target: https://tinier-tim.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Simulating drizzled HST PSFs.

Installation
============

0. Follow the instructions on the `STScI-supported documentation <https://astroconda.readthedocs.io/en/latest/installation.html#legacy-software-stack-with-iraf>`_ to create the `iraf27` `conda` environment and activate it. This amounts to running the following:

.. code-block:: sh

    $conda config --add channels http://ssb.stsci.edu/astroconda
    $conda create -n iraf27 python=2.7 iraf-all pyraf-all stsci
    $source activate iraf27

When you run `tiny1` on terminal, you should see

.. code-block:: sh

    >> tiny1 paramfile [major=x minor=y angle=z] [jitter=x] [ebmv=x] [Av=x] [wmag=x]

1. Clone the editable version of this repo (not available yet!).

.. code-block:: sh

    $git clone https://github.com/jiwoncpark/tinier-tim.git
    $cd tinier-tim
    $pip install -e . -r requirements.txt

2. (Optional) To run the notebooks, add the Jupyter kernel.

.. code-block:: sh

    $python -m ipykernel install --user --name tinier-tim --display-name "Python (tinier-tim)"


Tutorials
=========

See the `documentation <https://tinier-tim.readthedocs.io/en/latest/?badge=latest>`_ for tutorials.

Feedback
========

Suggestions are always welcome! There is quite a bit of omission in the tutorials owing to my lack of background knowledge. If you encounter issues or areas for improvement, please message @jiwoncpark or `make an issue
<https://github.com/jiwoncpark/tinier-tim/issues>`_.


Attribution
===========

The package heavily uses the C package `Tiny Tim <https://www.stsci.edu/software/tinytim/>`_ developed by John Krist, with additional support provided by Richard Hook and Felix Stoehr. The rebinning and drizzling code was written by Xuheng Ding (@dartoon) and modularized with minor modifications by Ji Won Park (@jiwoncpark). The tutorials were also written by Ji Won Park (@jiwoncpark). 
