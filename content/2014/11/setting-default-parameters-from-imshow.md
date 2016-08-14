Title: Setting default parameters from imshow in pyplot
Author: SergeM
Date: 2014-11-23 22:29:00
Slug: setting-default-parameters-from-imshow
Tags: useful,python

<div dir="ltr" style="text-align: left;" trbidi="on">

 <pre class="brush: cpp">
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'
</pre></div>