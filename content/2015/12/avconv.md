Title: convert video to jpeg with good quality
Author: SergeM
Date: 2015-12-14 22:00:00
Slug: avconv
Tags: useful,ffmpeg,avconv


convert video to jpeg with good quality:
```bash
avconv -i input_video.mp4 -qmax 1 -qmin 1 images_%05d.jpg
```

crop video:
```bash
avconv -i input.avi -vf crop=<width>:<height>:<x>:<y> output_%05d.png
```


create gif using 

http://gifmaker.me/
