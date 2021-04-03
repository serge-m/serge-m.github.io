---
Title: Loading numpy array from string
Author: SergeM
Date: 2014-11-17 23:01:00
Slug: loading-numpy-array-from-string
aliases: [/loading-numpy-array-from-string.html]
Tags: [ useful,numpy,python]
---



Okay children, today we learn how to convert text to numpy matrix.
Source is [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html" target="_blank).


<pre class="brush: python"># loading modules
import numpy
from StringIO import StringIO

# Using StringIO as a file-like wrapper over text
I0 = numpy.loadtxt(StringIO("""
         0         0         0         0         0
         0         0    0.5000         0         0
         0         0    1.0000         0         0
         0         0    0.5000         0         0
         0    1.0000         0         0         0
         0    0.5000         0         0         0
         0    0.5000    1.0000         0         0
         0         0         0         0         0""") )


I1 = numpy.loadtxt(StringIO("""
         0         0         0         0         0
         0    0.5000         0         0         0
         0    1.0000         0         0         0
         0    0.5000         0         0         0
         0         0    1.0000         0         0
         0         0    0.5000         0         0
         0         0    0.5000    1.0000         0
         0         0         0         0         0 """) )
</pre>  <pre class="brush: python">
#printing results:
print I0
print I1

#result
[[ 0.   0.   0.   0.   0. ]
 [ 0.   0.   0.5  0.   0. ]
 [ 0.   0.   1.   0.   0. ]
 [ 0.   0.   0.5  0.   0. ]
 [ 0.   1.   0.   0.   0. ]
 [ 0.   0.5  0.   0.   0. ]
 [ 0.   0.5  1.   0.   0. ]
 [ 0.   0.   0.   0.   0. ]]
[[ 0.   0.   0.   0.   0. ]
 [ 0.   0.5  0.   0.   0. ]
 [ 0.   1.   0.   0.   0. ]
 [ 0.   0.5  0.   0.   0. ]
 [ 0.   0.   1.   0.   0. ]
 [ 0.   0.   0.5  0.   0. ]
 [ 0.   0.   0.5  1.   0. ]
 [ 0.   0.   0.   0.   0. ]]


</pre>
