---
Title: OpenCV tutorials (Russian)
Author: SergeM
Date: 2013-11-05 20:44:00
Slug: opencv-tutorials-in-russian
aliases: [/opencv-tutorials-in-russian.html]
Tags: [ opencv,tuturials]
---




1. Делаем детектор движения, или OpenCV — это просто
[http://habrahabr.ru/company/avi/blog/200804/](http://habrahabr.ru/company/avi/blog/200804/)
2.&nbsp;OpenCV шаг за шагом
[http://robocraft.ru/blog/computervision/265.html](http://robocraft.ru/blog/computervision/265.html)
3. Пару слов о распознавании образов
[http://habrahabr.ru/post/208090/](http://habrahabr.ru/post/208090/)

<h3 style="text-align: left;">Building opencv program in C</h3><div><span style="background-color: #f7f7f9; color: #222222; font-family: Menlo, Monaco, 'Courier New', monospace; font-size: 12px; line-height: 20px; white-space: pre-wrap;">gcc -ggdb `pkg-config --cflags opencv` -o `basename test.c .c` test.c `pkg-config --libs opencv`</span></div>**Description:**<i style="background-color: white; border: 0px; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px; margin: 0px; outline: 0px; padding: 0px; vertical-align: baseline;">`pkg-config --cflags opencv`</i><span style="background-color: white; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px;">&nbsp;— подставляет путь для инклудов через pkgconfig.</span>
<i style="background-color: white; border: 0px; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px; margin: 0px; outline: 0px; padding: 0px; vertical-align: baseline;">`pkg-config --libs opencv`</i><span style="background-color: white; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px;">&nbsp;— подставляет название либ для линковки через pkgconfig.</span>
<span style="background-color: white; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px;">При установке opencv поместила файлик .pc (в моём случае это /usr/lib/pkgconfig/opencv.pc), в котором рассказывается, где находятся заголовочные файлы этой библиотеки, а где сами либы для линковки. Таким образом первое у меня разворачивается в "-I/usr/include/opencv", а второе — в "-lopencv_calib3d -lopencv_contrib -lopencv_core -lopencv_features2d -lopencv_flann -lopencv_gpu -lopencv_highgui -lopencv_imgproc -lopencv_legacy -lopencv_ml -lopencv_nonfree -lopencv_objdetect -lopencv_ocl -lopencv_photo -lopencv_stitching -lopencv_superres -lopencv_ts -lopencv_video -lopencv_videostab", т.е. уже в прямые указания компилятору и линкеру, где искать инклуд-файлы (-Include) и библиотеки (-library), позволяющие разработчику не вбивать всё это руками.</span>
<i style="background-color: white; border: 0px; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px; margin: 0px; outline: 0px; padding: 0px; vertical-align: baseline;">-o `basename test.c .c`</i><span style="background-color: white; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px;">&nbsp;— отрезает от test.c часть с расширением (".c"), оставляя только часть имени файла «test», которое будет являться именем выходного (output) собранного исполняемого файла. Т.е. разворачивается это в "-o test".</span>
<i style="background-color: white; border: 0px; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px; margin: 0px; outline: 0px; padding: 0px; vertical-align: baseline;">-ggdb</i><span style="background-color: white; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px;">&nbsp;— смотрим в ман (а стоило бы сделать это ещё в начале ;))</span>
<blockquote style="background-color: white; border-left-color: rgb(187, 187, 187); border-left-style: solid; border-width: 0px 0px 0px 2px; clear: both; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px; margin: 0.83em 0px; outline: 0px; padding: 0px 0px 0px 15px; quotes: none; vertical-align: baseline;">-ggdb
Produce debugging information for use by GDB. This means to use the most expressive format available (DWARF 2, stabs, or the native format if neither of those are supported), including GDB extensions if at all possible.</blockquote><br style="background-color: white; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px;" /><span style="background-color: white; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px;">т.е. генерация максимально полной отладочной информации для использовании в отладчике gdb (и включение её в выходной бинарник, например замечены секции .debug_aranges, .debug_info, .debug_abbrev, .debug_line, .debug_str).</span>
<span style="background-color: white; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px;">
</span><span style="background-color: white; font-family: Arial, sans-serif; font-size: 13px; line-height: 18px;">Blog about computer vision and opencv</span>
<span style="background-color: white; font-family: Arial, sans-serif; font-size: x-small; line-height: 18px;">[http://www.uralvision.blogspot.ru/](http://www.uralvision.blogspot.ru/)</span>
<span style="background-color: white; font-family: Arial, sans-serif; font-size: x-small; line-height: 18px;">
</span>
