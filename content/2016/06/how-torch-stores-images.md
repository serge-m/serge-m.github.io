Title: how torch stores images
Author: SergeM
Date: 2016-06-26 23:01:00
Slug: how-torch-stores-images
Tags: torch

<div dir="ltr" style="text-align: left;" trbidi="on">require('image')
<div><div>imgPath = "image.jpg"</div><div>img = torch.Tensor(1, 3, imgDim, imgDim)</div></div><div><div>img[1] = image.load(imgPath, 3, byte)</div></div><div>
</div><div>image is stored as float, conversion is (intensity/255.). stored top->bottom, line by line. format RGB.</div><div>
</div><h3 style="text-align: left;">display</h3><div>require 'gnuplot'</div><div><div>gnuplot.figure(1)</div></div><div>gnuplot.imagesc(img[1])

Torch<->numpy dictionary
[https://github.com/torch/torch7/wiki/Torch-for-Numpy-users](https://github.com/torch/torch7/wiki/Torch-for-Numpy-users)</div></div>