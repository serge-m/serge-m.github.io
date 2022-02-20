---
Title: Digital color representation
Author: SergeM
Date: 2022-02-20 21:30:00
Slug: digital-color-representation
Tags: [ image processing, YUV, RGB, YCbCr ]
---

Representation of color is messed up. Here are some articles about terminology.

[Merging Computing with Studio Video: Converting Between R'G'B' and 4:2:2](https://poynton.ca/papers/Discreet_Logic/index.html) / 
[pdf](https://poynton.ca/PDFs/Merging_RGB_and_422.pdf) by Charles Poynton

>  Upon conversion from 8-bit R'G'B' to 8-bit Y'CBCR, three-quarters of the available colors are lost. Upon 4:2:2 subsampling, half the color detail is discarded.


[YUV and luminance considered harmful](https://poynton.ca/papers/YUV_and_luminance_harmful.html) /
[pdf](http://poynton.ca/PDFs/YUV_and_luminance_harmful.pdf) 
by Charles Poynton

> It was standardized for NTSC in 1953, and remains standard for all contemporary video systems, to form luma, denoted Y’, as
a weighted sum of nonlinear (gamma-corrected) R’G’B’ components.
The nonlinear transfer function is roughly comparable to a square root.
To form luma, we use the theoretical coefficients of color science, but
we use them in a block diagram different from that prescribed by color
science: As detailed in my book, in video, gamma correction is applied
before forming the weighted sum, not after. The “order of operations” is
reversed from what you might expect from color science

>  Engineers today often carelessly use the word luminance, and the symbol Y, to refer to
the weighted sum of nonlinear (gamma-corrected) R’G’B’ components

