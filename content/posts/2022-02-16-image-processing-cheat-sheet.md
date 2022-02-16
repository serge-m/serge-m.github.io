---
Title: Image processing cheat sheet
Author: SergeM
Date: 2022-02-16 21:30:00
Slug: learning-rust
Tags: [ image processing, cheatsheet, imagemagick, jpg, resize ]
---



In ImageMagick:

* `convert` save the result to a given (new) file
* `mogrify` is the same as `convert` but it performs processing inplace (the input files are overwritten)

Strip metadata from jpg file:

    mogrify -strip f.jpg

Rotate according the metadata, then strip:

    mogrify -auto-orient -strip f.jpg 

Find `jpg` and `jpeg` images, apply orientation from EXIF, remove metadata and resize to 1920 on the longest side
preserving the aspect ratio and save to the same files:

    find . -name "*.jp*g" -exec mogrify -auto-orient -strip -resize "1920x1920" {} \;
