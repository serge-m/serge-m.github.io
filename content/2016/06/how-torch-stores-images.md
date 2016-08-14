Title: how torch stores images
Author: SergeM
Date: 2016-06-26 23:01:00
Slug: how-torch-stores-images
Tags: torch

```
require('image')
imgPath = "image.jpg"
img = torch.Tensor(1, 3, imgDim, imgDim)
img[1] = image.load(imgPath, 3, byte)
```
image is stored as float, conversion is (intensity/255.). stored top->bottom, line by line. format RGB.
```
display
require 'gnuplot'
gnuplot.figure(1)
gnuplot.imagesc(img[1])
```

Torch<->numpy dictionary
[https://github.com/torch/torch7/wiki/Torch-for-Numpy-users](https://github.com/torch/torch7/wiki/Torch-for-Numpy-users)