Title: OpenCV. Processing external byte buffer
Author: SergeM
Date: 2013-10-21 13:40:00
Slug: opencv-processing-external-byte-buffer
Tags: 



We have such an example from openCV documentation:
<blockquote class="tr_bq"><span style="font-family: 'Courier New', Courier, monospace;">Mat img(height, width, CV_8UC3, pixels, step);</span>
<span style="font-family: Courier New, Courier, monospace;">GaussianBlur(img, img, Size(7,7), 1.5, 1.5);</span></blockquote>
<div>What does it mean?&nbsp;</div><div>Lets say I have an image img:
<blockquote class="tr_bq"><span style="font-family: 'Courier New', Courier, monospace;">typedef unsigned char BYTE;</span>
<span style="font-family: Courier New, Courier, monospace;">BYTE * img = new BYTE[ w * h ];</span></blockquote></div><div>Lets assume the image is scanned line by line. So
<blockquote class="tr_bq"><span style="font-family: 'Courier New', Courier, monospace;">img[ 10 * w + 3 ] is a 3-rd pixel in 10-line of image.</span></blockquote></div><div>Then I import it in openCV is such a way:
<blockquote class="tr_bq"><span style="font-family: 'Courier New', Courier, monospace;">Mat img(h, w, CV_8UC1, dmDst, w);</span></blockquote>
last argument is a pitch or stride.








