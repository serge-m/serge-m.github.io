Title: Opencv and "OpenCV Error: Bad flag"
Author: SergeM
Date: 2013-08-05 16:59:00
Slug: opencv-and-opencv-error-bad-flag
Tags: 

<div dir="ltr" style="text-align: left;" trbidi="on">
&nbsp; &nbsp;
I had pretty simple code with opencv:

**&nbsp; &nbsp; cv::Mat t;**
**&nbsp; &nbsp; t = cv::imread( "qq.bmp" ) ;**
**&nbsp; &nbsp; cv::imwrite( "q.bmp", t );**
**&nbsp; &nbsp; cv::namedWindow( "asdads", CV_WINDOW_AUTOSIZE );**
**&nbsp; &nbsp; cv::imshow( "asdads", t );**
**&nbsp; &nbsp; cv::waitKey( -1 );**
**&nbsp; &nbsp; return 0;**

It caused crash in debug configuration:

**OpenCV Error: Bad flag (parameter or structure field) (Unrecognized or unsupport**
**ed array type) in unknown function, file ..\..\..\src\opencv\modules\core\src\ar**
**ray.cpp, line 2482**
<b>
</b>In release configuration it was ok. Finally i found the solution. Both in debug and release configurations I used static libraries for release conguration
<b>
</b>**opencv_core231.lib opencv_imgproc231.lib opencv_highgui231.lib**
<b>
</b>And one should use
**opencv_core231d.lib opencv_imgproc231d.lib opencv_highgui231d.lib**
for debug.

It seems wrong libraries cause crashes only sometimes. I had used release version of static opencv libraries for my debu and release configurations for a long time an only now it caused problems


</div>