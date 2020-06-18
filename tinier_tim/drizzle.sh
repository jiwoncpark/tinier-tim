#!/bin/bash                                                                     
#Run using iraf27 environment                
cp ../tinier_tim/dri_psf.cl ./                                   
echo "cl<dri_psf.cl; logout" | cl
python ../tinier-tim/normalize_drizzled_psf.py
rm dripsf.fits
rm dripsfw.fits