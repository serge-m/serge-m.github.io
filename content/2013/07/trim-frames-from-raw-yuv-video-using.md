Title: Trim frames from raw YUV video using FFMPEG
Author: SergeM
Date: 2013-07-02 19:01:00
Slug: trim-frames-from-raw-yuv-video-using
Tags: 

Trim 5 frames starting from 160-th frame and write to png sequence

<blockquote class="tr_bq">ffmpeg -pix_fmt yuv420p -s 1920x1088 &nbsp;-r 1 -i input_video.yuv -r 1 -ss 160 -frames 5 &nbsp;output_sequence_%d.png</blockquote>
size of input video is 1920x1088, format YUV420 progressive

UPD:
ffmpeg is renamed to avconv.
Using it for trimming AVI video:

avconv -ss 00:58:00 -t 00:59:30 -i ./video.avi frame_%05d.png 

