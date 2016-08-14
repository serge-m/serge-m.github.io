Title: displaying multiple grayscale figures in python's matplotlib
Author: SM!
Date: 2014-06-06 22:12:00
Slug: displaying-multiple-grayscale-figures
Tags: python,ipython

<div dir="ltr" style="text-align: left;" trbidi="on"><span style="font-family: &quot;Courier New&quot;,Courier,monospace;">from matplotlib import pyplot as plt</span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">import matplotlib.cm as cm</span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">plt.figure()&nbsp; # without this it display one after another</span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">plt.imshow(image_one, cmap=cm.gray) # without cm.gray it displays grayscale images in colormap</span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">plt.imshow(image_two, cmap=cm.gray) #</span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">plt.show()</span>

use
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">%matplotlib inline</span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">in ipython notebook to display image inplace</span>


Shorter version:
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">%matplotlib inline
import matplotlib.pyplot as plt
plt.axis('off')
plt.imshow(dpt, cmap=plt.cm.gray, interpolation='nearest')</span></div>