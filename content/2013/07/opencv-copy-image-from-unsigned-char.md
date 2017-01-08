Title: OpenCV. Copy image from unsigned char buffer, resize and save to file
Author: SergeM
Date: 2013-07-09 23:23:00
Slug: opencv-copy-image-from-unsigned-char
Tags: c++,opencv


How to copy image from unsigned char buffer, resize and save to file.
If you use single-channel image.

```
#include <opencv/cv.h>
#include <opencv/highgui.h>

int coeff = 4;
cv::Mat src( height, width, CV_8UC1, (void *) source_byte_beffer ) );
cv::Mat small(height/ coeff, width/ coeff, CV_8UC1 );

cv::Size s_half(width/ coeff, height/ coeff);
cv::resize( src, small, s_half, 1, 1, cv::INTER_LINEAR ); // resize from src to small

IplImage* writeImage;
writeImage=cvCloneImage(&(IplImage)src);
cvSaveImage("src1.bmp", writeImage);
cvReleaseImage( &writeImage );

writeImage=cvCloneImage(&(IplImage)small);
cvSaveImage("little.bmp", writeImage);
cvReleaseImage( &writeImage );


//Another way of writtting:
/*cvWrite("src.bmp", src );
cv::imwrite( "small.bmp", small );*/
```