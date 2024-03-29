---
Title: Writing simple optical flow in python
Author: SergeM
Date: 2014-11-30 14:46:00
Slug: writing-simple-optical-flow-in-python
aliases: [/writing-simple-optical-flow-in-python.html]
Tags: [ python,optical flow]
---



First of all we need a couple of test images:
<pre class="brush: python">#
import numpy
from StringIO import StringIO

I0 = numpy.loadtxt(StringIO("""
         0         0         0         0         0
         0         0    0.5000         0         0
         0         0    1.0000         0         0
         0         0    0.5000         0         0
         0         0         0         0         0""") )


I1 = numpy.loadtxt(StringIO("""
         0         0         0         0         0
         0       0.5         0         0           0
         0       1.0         0         0           0
         0       0.5         0         0           0
         0         0         0         0         0 """) )</pre>Define initial horiozontal and vertical components of optical flow 
<pre class="brush: python">u = numpy.zeros_like(I0); 
v = numpy.zeros_like(I0); 
</pre>Lets write class for making warps. As OF usually deals only with small displacements, we need iterative estimation: estimate, shift image by found vectors, find again.


<pre class="brush: python">class Warper:
    def `__init__`(self, shape, u0, v0, I0, I1, display = False):
        """
            shape - shape of input function,
            u0, v0 - starting values of flow
            I0, I1 - images to compute flow between
            
        """
        # saving dimensions
        self.M, self.N = shape[0], shape[1]
        # save initial estimation
        self.u, self.v = u0.copy(), v0.copy()
        # grid of coordinates, required further
        self.idx, self.idy = np.meshgrid(np.arange(self.N), np.arange(self.M))
        # filter for partial derivatives computation
        self.mask = np.array([1, -8, 0, 8, -1], ndmin=2)/12.0; 
        # flag of debug information output
        self.display = display
        self.counter = 0
        # copy of images
        self.I0, self.I1 = I0.copy(), I1.copy()
        
        # here we create an instance of training function. On each step we will approach to minimum by gradient descent
        self.train = TrainFunctionSimple(u0, v0, rate=0.1)
        
    # main function
    def warp(self):
        if self.display:
            print 'Warp %d' % (self.counter,)
        
        # initial value 
        u0, v0 = self.u.copy(), self.v.copy()
        
        # Ends of motion vectors. From these points we will "compensate" motion
        idxx = self.idx + u0
        idyy = self.idy + v0
        
        # get linearly interpolated values from (idxx, idyy) pixels of I1
        I1warped = interp2linear(self.I1, idxx, idyy)

        # just debug output
        if self.display:
            print "I1warped", I1warped

            print "I0", I0
            print "u0", u0
            print "v0", v0
            
            pass

        It = (I1warped - self.I0)
        print "It", It

        #My first wrong version (it gives no converging, something like continuing initial vectors to infinity during warps) (***)
        #Ix = ndimage.correlate(self.I1, self.mask, mode='nearest') 
        #Iy = ndimage.correlate(self.I1, self.mask.T, mode='nearest') 

        #Much better is:
        Ix = ndimage.correlate(I1warped, self.mask, mode='nearest') 
        Iy = ndimage.correlate(I1warped, self.mask.T, mode='nearest') 

        # boundary handling
        m = (idxx > self.N - 1) | (idxx < 0) | (idyy > self.M - 1) | (idyy < 0)
        Ix[m] = 0.0
        Iy[m] = 0.0
        It[m] = 0.0
        
        self.Ix = Ix
        self.Iy = Iy
        self.It = It
        
        self.train.init(np.zeros_like(self.I0), np.zeros_like(self.I0))
        for i_sgd in range(120):
            print self.train.step(Ix, Iy, It),

        self.u += self.train.tu.get_value()
        self.v += self.train.tv.get_value()
        self.counter += 1
</pre>Now describing TrainFunction. Well design is not good yet 
<pre class="brush: python">#
class TrainFunction(object):
    def `__init__`(self, u0, v0, rate):
        self.rate = rate
        self.tu = theano.shared(u0,name='tu')
        self.tv = theano.shared(v0,name='tv')
        self.tIx = T.matrix("tIx")
        self.tIy = T.matrix("tIy")
        self.tIt = T.matrix("tIt")
        
        self.gu, self.gv = None, None
        self.E = None
        self.train_function = self.get_function()
        
    # this function must be overloaded in the derived classes
    def get_energy(self):
        raise Exception("Non implemented")
            
    # construct Theano-function for gradient descent 
    def get_function(self):
        if self.E is None:
            self.E = self.get_energy()
        
        if self.gu is None or self.gv is None:
            self.gu, self.gv = T.grad(self.E, [self.tu, self.tv])  
            
        train_function = theano.function(
            inputs=[self.tIx, self.tIy, self.tIt],
            outputs=[self.E],
            updates=((self.tu, self.tu - self.rate * self.gu), (self.tv, self.tv - self.rate * self.gv)),
            allow_input_downcast=True)
    
        return train_function
    
    # initialization of flow values
    def init(self, u0, v0):
        self.tu.set_value(u0)
        self.tv.set_value(v0)
        
    # launching step of gradiennt descent
    def step(self, *args):
        return self.train_function(*args)
</pre><pre class="brush: python">#
class TrainFunctionSimple(TrainFunction):
    def `__init__`(self, *args, **kwargs):
        self.alpha = kwargs.get('alpha', 1.1)
        
        super(self.`__class__`, self).`__init__`(*args, **kwargs)
        
    # constructs Theano-function, that calculate Energy
    def get_energy(self,):
        # data term 
        Edata = T.sum( ( self.tIx * self.tu + self.tIy * self.tv + self.tIt ) ** 2 ) 

        # regularization term
        Ereg = T.sum(
            (self.tu)**2 + 
            (self.tv)**2 )

        return Edata+self.alpha*Ereg
</pre>finally launching 
<pre class="brush: python">wrpr = Warper( I0.shape, numpy.zeros_like(I0), numpy.zeros_like(I0), I0, I1, display=True)
warps = 5
for i in range(warps):
    wrpr.warp()
</pre>Printing the results: 
<pre class="brush: python">numpy.set_printoptions(precision=3,)

print wrpr.u
print wrpr.v
</pre><pre class="brush: python">[[ 0.     0.     0.     0.     0.   ]
 [ 0.     0.    -0.523  0.     0.   ]
 [ 0.     0.    -0.941  0.     0.   ]
 [ 0.     0.    -0.523  0.     0.   ]
 [ 0.     0.     0.     0.     0.   ]]
[[ 0.     0.     0.     0.     0.   ]
 [ 0.    -0.692  0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.   ]
 [ 0.     0.692  0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.   ]]
</pre>Well, not precise enough. However the direction is right. 
<h1> UPDATE: due to my error in (***), see code, results and images below may have no sense </h1>    <h1> Some errors </h1>  In this implementation we estimate how to move I1 to match I0. So vectors points from locations of I0 to points of I1. So spatial derivatives must be calculated from I1, not I0: 
<pre class="brush: python">Ix = ndimage.correlate(self.I1, self.mask, mode='nearest') 
Iy = ndimage.correlate(self.I1, self.mask.T, mode='nearest') 
</pre>If you write instead: 
<pre class="brush: python">Ix = ndimage.correlate(self.I0, self.mask, mode='nearest') 
Iy = ndimage.correlate(self.I0, self.mask.T, mode='nearest') 
</pre>you will get pressy strange results.
Input images I0 and I1:

</div><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-right: 1em; text-align: left;"><tbody><tr><td style="text-align: center;">
![](http://3.bp.blogspot.com/-dYfZ9eUjqE4/VHtGMwxyuQI/AAAAAAAACFg/vBjZqQkILaY/s1600/I0.png)
</td><td style="text-align: center;">
![](http://4.bp.blogspot.com/-G4C3gKG5W_0/VHtGMyVkRtI/AAAAAAAACFk/d51MYVnFvjo/s1600/I1.png)
</td></tr></tbody></table>

So the "object" moves from left to right. I0 is a current frame and I1 is a previous frame. The vectors after 1 and 10 warps of correct iteration (derivatives of I1, I0 at background):

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-right: 1em; text-align: left;"><tbody><tr><td style="text-align: center;">
![](http://2.bp.blogspot.com/-RBt_zV-BwPE/VHtGBocIBhI/AAAAAAAACFY/3bTptWcs4zc/s1600/after%2B100%2Bcorrect%2Bwarp.png)
</td><td style="text-align: center;">
![](http://2.bp.blogspot.com/-UdPZ2hZ7Qaw/VHtGBmkLbAI/AAAAAAAACFE/U3Wg3lnIhV0/s1600/after%2Bone%2Bcorrect%2Bwarp.png)
</td></tr></tbody></table>
<div style="text-align: left;">The vectors after 1 and 10 warps of incorrect iteration (derivatives of I0, I0 at background): </div><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-right: 1em; text-align: left;"><tbody><tr><td style="text-align: center;">
![](http://1.bp.blogspot.com/-RGrBP9xedI0/VHtGB276WkI/AAAAAAAACFI/uvpw4JUI0Xo/s1600/after%2Bone%2Bincorrect%2Bwarp.png)
</td><td style="text-align: center;">
![](http://1.bp.blogspot.com/-N7Piixu8HBw/VHtGBgcTDSI/AAAAAAAACFA/bgQJqZQUsvY/s1600/after%2B100%2Bincorrect%2Bwarp.png)
 </td></tr></tbody></table><pre class="brush: python"></pre><pre class="brush: python"></pre><pre class="brush: python"></pre><pre class="brush: python"></pre>These pictures are made with 120 steps of gradient descent.

<h2 style="text-align: left;">Regularization term</h2><div style="text-align: left;">Ok. Now lets improve our regularization term. Instead of L2 norm, lets use Total Variation approach.</div><div style="text-align: left;">On the same settings&nbsp; lets use another train function class:</div><div style="text-align: left;"><pre class="brush: python">class TrainFunctionTV(TrainFunction):
    def `__init__`(self, *args, **kwargs):
        self.alpha = kwargs.get('alpha', 1.1)

        super(self.`__class__`, self).`__init__`(*args, **kwargs)

    def get_energy(self,):
        Edata = T.sum((self.tIx * self.tu + self.tIy * self.tv + self.tIt) ** 2)
        Ereg1 = T.sum(
            (self.tu[1:]-self.tu[:-1])**2 +
            (self.tv[1:]-self.tv[:-1])**2 )
        Ereg2 = T.sum(
            (self.tu[:,1:]-self.tu[:,:-1]) **2 +
            (self.tv[:,1:]-self.tv[:,:-1]) ** 2)

        return Edata+self.alpha*(Ereg1+Ereg2)   
</pre>
</div><div style="text-align: left;">Now we have these results:
<pre class="brush: python">print wrpr.u
print wrpr.v

 

[[-0.862 -0.903 -0.949 -0.941 -0.929]
 [-0.842 -0.92  -1.025 -0.968 -0.941]
 [-0.81  -0.933 -1.101 -0.99  -0.95 ]
 [-0.842 -0.92  -1.025 -0.968 -0.941]
 [-0.862 -0.903 -0.949 -0.941 -0.929]]
[[-0.121 -0.136 -0.093 -0.06  -0.045]
 [-0.106 -0.197 -0.083 -0.043 -0.029]
 [-0.    -0.    -0.    -0.    -0.   ]
 [ 0.106  0.197  0.083  0.043  0.029]
 [ 0.121  0.136  0.093  0.06   0.045]]

 
</pre>Visualization:

<table><tbody><tr>  <td>
![](http://2.bp.blogspot.com/-RBt_zV-BwPE/VHtGBocIBhI/AAAAAAAACFc/reFzmPZUpes/s1600/after%2B100%2Bcorrect%2Bwarp.png)
</td> <td>
![](http://4.bp.blogspot.com/-fQ1nRz2R0TA/VI9SvoUd3iI/AAAAAAAACGU/IaqihseanNY/s1600/OF%2Bwith%2BTV.png)
</td></tr><tr><td style="text-align: center;">before (L2)</td><td style="text-align: center;">after (TV)</td></tr></tbody></table></div>
