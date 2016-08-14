Title: OpenCV. Copy image from unsigned char buffer, resize and save to file
Author: SergeM
Date: 2013-07-09 23:23:00
Slug: opencv-copy-image-from-unsigned-char
Tags: c++,opencv

<div dir="ltr" style="text-align: left;" trbidi="on">How to copy image from unsigned char buffer, resize and save to file.
If you use single-channel image.

<div><div>#include <opencv/cv.h></div><div>#include <opencv/highgui.h></div></div><div>
</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; int coeff = 4;</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cv::Mat src( height, width, CV_8UC1, (void *) source_byte_beffer ) );</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cv::Mat small(height/ coeff,&nbsp;width/ coeff, CV_8UC1 );</div><div>
</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cv::Size s_half(width/ coeff,&nbsp;height/ coeff);</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cv::resize( src, small, s_half, 1, 1, cv::INTER_LINEAR ); // resize from src to small</div><div>
</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; IplImage* writeImage;</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; writeImage=cvCloneImage(&amp;(IplImage)src);</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cvSaveImage("src1.bmp", writeImage);</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cvReleaseImage( &amp;writeImage );</div><div>
</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; writeImage=cvCloneImage(&amp;(IplImage)small);</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cvSaveImage("little.bmp", writeImage);</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cvReleaseImage( &amp;writeImage );</div><div>
</div><div>
</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; //Another way of writtting: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /*cvWrite("src.bmp", src );</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cv::imwrite( "small.bmp", small );*/</div><div>
</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div><div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div></div>