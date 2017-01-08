Title: Installing theano on windows
Author: SergeM
Date: 2014-12-28 01:56:00
Slug: installing-theano-on-windows
Tags: useful,windows,theano,python


0. install Anaconda
1. download Theano sources from git (install it using setup.py)
2. Setup NVIDIA GPU Toolkit. I have installed version 6.5
3. Setup Visual Studio Community Edition 2013
4. Create config file .theanorc  in c:\Users\X\:

```
[global]
floatX = float32
device = gpu
 
[nvcc]
fastmath = True
compiler_bindir=C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\cl.exe
```

Without the line with path to cl.exe I got:

```
nvcc fatal   : Cannot find compiler 'cl.exe' in PATH
['nvcc', '-shared', '-O3', '-use_fast_math', '-Xlinker', '/DEBUG', 

'-D HAVE_ROUND', '-m64', '-Xcompiler',

 '-DCUDA_NDARRAY_CUH=f411a53ee0a470fbaad3b5c4a681ef64,-D 

NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION,/Zi,/MD', 

'-Ic:\\anaconda\\theano\\theano\\sandbox\\cuda', 

'-Ic:\\anaconda\\lib\\site-packages\\numpy\\core\\include', 

'-Ic:\\anaconda\\include', '-o', 

'C:\\Users\\X\\AppData\\Local\\Theano\\compiledir_Windows-7-6.1.7601-SP1-Intel64_Family_6_Model_42_Stepping_7_GenuineIntel-2.7.7-64\\cuda_ndarray\\cuda_ndarray.pyd', 

'mod.cu', '-Lc:\\anaconda\\libs', 

'-Lc:\\anaconda', '-lpython27', '-lcublas', '-lcudart']
```
