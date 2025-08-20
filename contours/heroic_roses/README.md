Heroic Roses
=============

Heroic Roses is a painting by Paul Klee and this directory contains contour files
that can be used with Axom's `SamplingShaper` class to create a representation
of the painting on a mesh via sampling using volume fractions to represent various
colored regions.

There are multiple versions of the contours in different subdirectories:

* c2c - The original C2C versions of the contours with 1 file per shape
* mfem - An MFEM representation of the contours (converted from C2C) with 1 file per shape
* mfem_cp - An MFEM representation of the contours with contours for each "color" merged into a single file, and able to work with the SamplingShaper using the Winding Number sampler.
