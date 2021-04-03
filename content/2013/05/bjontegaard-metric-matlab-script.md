---
Title: Bjontegaard metric. Matlab script.
Author: SergeM
Date: 2013-05-15 12:51:00
Slug: bjontegaard-metric-matlab-script
aliases: [/bjontegaard-metric-matlab-script.html]
Tags: [ ]
---




Bjontegaard metric (BD-PSNR) describes the distance between two RD-curved.
I is useful to determine how big is the gain between "before" and "after" versions.
Or determine what curve is better if they have complex form (for example, intersecting).

I found matlab [script](http://www.mathworks.com/matlabcentral/fileexchange/27798-bjontegaard-metric),
that calculates BD-PSNR, but it was not correct. The limits of integration were wrong.
Difference between two curves can be calculated only in the area of thein projections intersection.
Fixed script was verified by data provided the auther of the metric.

## Download
fixed [matlab script for BD-PSNR calculation](https://github.com/serge-m/bjontegaard2/blob/master/bjontegaard2.m)

[github](https://github.com/serge-m/bjontegaard2)

[original paper](http://wftp3.itu.int/av-arch/video-site/0104_Aus/VCEG-M33.doc) (doc)

[data for verification](http://wftp3.itu.int/av-arch/video-site/0104_Aus/VCEG-M34.xls) (xls)



## Original publilcation:
G. Bjontegaard, “Calculation of average PSNR differences between RD-curves (VCEG-M33),” in
VCEG Meeting (ITU-T SG16 Q.6), Austin, Texas, USA, Apr. 2001

