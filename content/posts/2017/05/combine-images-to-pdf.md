---
Title: Combine images to PDF in linux
Author: SergeM
Date: 2017-05-03 07:11:00
Slug: combine-images-to-pdf
aliases: [/combine-images-to-pdf.html]
Tags: [ linux, imagemagick, useful, images]
---




Using `convert` utility we can join multiple image files (png, jpeg, pdf) into one pdf.

```
convert -density 250 file1.pdf file2.JPG file3.pdf -compress JPEG -quality 70 combined.pdf
```

we use JPEG compression with quality =90 for images inside PDF. Otherwise the PDF will be too large.


[source](http://stackoverflow.com/questions/23160191/compressing-text-heavy-pdfs-without-ghostscript-and-only-imagemagik-causes-blurr)

