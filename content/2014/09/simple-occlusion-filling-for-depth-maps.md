---
Title: Simple occlusion filling for depth maps 
Author: SergeM
Date: 2014-09-01 12:14:00
Slug: simple-occlusion-filling-for-depth-maps
aliases: [/simple-occlusion-filling-for-depth-maps.html]
Tags: [ depth map,python]
---



As an example I use images from middleburry.
Solution is very dirty and slow.


[https://github.com/serge-m/depth_map_occlusion](https://github.com/serge-m/depth_map_occlusion" target="_blank)

<blockquote class="tr_bq"><span style="font-family: &quot;Courier New&quot;,Courier,monospace;"># In[1]:

import numpy
import scipy
import matplotlib.pyplot as plt


# In[2]:

from scipy import ndimage
import numpy as np

# kernels for shift
k = np.array([
[[0,0,0],
&nbsp;[0,0,1],
&nbsp;[0,0,0],],
[[0,1,0],
&nbsp;[0,0,0],
&nbsp;[0,0,0],],
[[0,0,0],
&nbsp;[1,0,0],
&nbsp;[0,0,0],],
[[0,0,0],
&nbsp;[0,0,0],
&nbsp;[0,1,0],],
[[1,0,0],
&nbsp;[0,0,0],
&nbsp;[0,0,0],],
[[0,0,1],
&nbsp;[0,0,0],
&nbsp;[0,0,0],],
[[0,0,0],
&nbsp;[0,0,0],
&nbsp;[0,0,1],],
[[0,0,0],
&nbsp;[0,0,0],
&nbsp;[1,0,0],],
])
</span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">

# In[8]:

from scipy import misc

from PIL import Image

#reading source data
frm = misc.imread('cones_2_6_align2_00000.png')
dpt0 = misc.imread('disp2.png')
occl0 = misc.imread('occl.png')

#initial values for results
dpt = dpt0
occl = occl0

frm_shifterd = numpy.zeros((len(k),)+frm.shape)
dif = numpy.zeros((len(k),)+frm.shape)
sumdiff = numpy.zeros((len(k),)+frm.shape[:-1])

for ik in range(len(k)):
&nbsp;&nbsp;&nbsp; for ch in range(frm.shape[-1]):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; frm_shifterd[ik,:,:,ch] = ndimage.convolve(frm[:,:,ch], k[ik], mode='nearest', cval=0.0)
&nbsp;&nbsp;&nbsp; dif[ik] = numpy.abs(frm_shifterd[ik,:,:,:]-frm[:,:,:]) 
&nbsp;&nbsp;&nbsp; sumdiff[ik] = dif[ik].sum(axis=2) 
&nbsp;&nbsp;&nbsp; 

iteration = 0


def one_iteration(dpt, occl, k, sumdiff):
&nbsp;&nbsp;&nbsp; dpt_shifted = numpy.zeros((len(k),)+dpt.shape)
&nbsp;&nbsp;&nbsp; occl_shifted = numpy.zeros((len(k),)+dpt.shape)
&nbsp;&nbsp;&nbsp; sumdiff_final = numpy.zeros((len(k),)+frm.shape[:-1])

&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp; occl_dil = ndimage.grey_dilation(occl, size=(3,3))
&nbsp;&nbsp;&nbsp; for ik in range(len(k)):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; dpt_shifted[ik,:,:] = ndimage.convolve(dpt[:,:], k[ik], mode='nearest', cval=0.0)
&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; occl_shifted[ik,:,:] = ndimage.convolve(occl[:,:], k[ik], mode='nearest', cval=0.0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sumdiff_final[ik] = sumdiff[ik] + (1-occl_shifted[ik])*1000000000
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #print 'shifted', ik, '\n', dpt_shifted[ik]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp; # chose direction where the difference is the lowest
&nbsp;&nbsp;&nbsp; good_directions = numpy.argmin(sumdiff_final, axis = 0)
&nbsp;&nbsp;&nbsp; dpt_best = numpy.choose( good_directions, dpt_shifted )
&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp; dpt_new = numpy.choose( occl==occl_dil, numpy.array([dpt_best,dpt]))
&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp; return dpt_new, occl_dil

while True:
&nbsp;&nbsp;&nbsp; iteration += 1
&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp; dpt_new, occl_dil = one_iteration(dpt, occl, k, sumdiff)
&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp; if numpy.array_equal(occl, occl_dil):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; break;
&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp; #Image.fromarray(np.cast['uint8'](dpt_new)).save('dpt_{}.png'.format(iteration))

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp; dpt = numpy.copy(dpt_new)
&nbsp;&nbsp;&nbsp; occl = numpy.copy(occl_dil)
&nbsp;&nbsp;&nbsp; 
#write output 
Image.fromarray(np.cast['uint8'](dpt)).save('processed_dpt.png')</span></blockquote>

