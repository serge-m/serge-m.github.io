Title: ffmpeg(avconv) jpeg quality
Author: SergeM
Date: 2015-09-06 15:52:00
Slug: ffmpegavconv-jpeg-quality
Tags: avconv,useful,ffmpeg,video processing

conversion with good jpeg quality:
```bash
avconv -i ./input.avi -q:v 1 output_frame_%05d.jpg
```
