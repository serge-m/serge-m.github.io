---
Title: Combine images to PDF in linux
Author: SergeM
Date: 2017-05-03 07:11:00
Slug: combine-images-to-pdf
aliases: [/combine-images-to-pdf.html]
Tags: [ linux, imagemagick, useful, images, pdf]
---




Using `convert` utility we can join multiple image files (png, jpeg, pdf) into one pdf.

    convert -density 250 file1.pdf file2.JPG file3.pdf -compress JPEG -quality 70 combined.pdf

we use JPEG compression with quality =90 for images inside PDF. Otherwise the PDF will be too large.


[source](http://stackoverflow.com/questions/23160191/compressing-text-heavy-pdfs-without-ghostscript-and-only-imagemagik-causes-blurr)


For me images appear rotated inside the pdf. That's probably because EXIF information about image rotation 
is not taken into account by pdf converter.

You can remove all the meta information first with `convert <input file> -strip <output file>` and then combine it to a pdf.

Rotating of the image can be done with `-rotate 90` parameter:

    convert -rotate 90 -density 250 1.jpg 2.jpg 3.jpg -compress JPEG -quality 80 part1.pdf
