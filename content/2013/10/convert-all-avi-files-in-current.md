Title: Convert all *.avi files in current directory to png sequences 
Author: SergeM
Date: 2013-10-22 23:49:00
Slug: convert-all-avi-files-in-current
Tags: ffmpeg, python, video, image 

Using python and ffmpeg:

```python
#!/usr/bin/python

import glob
import os

t=glob.glob("*.avi" ) # search all AVI files

for v in t:
     vv = os.path.splitext(v)[0];
     os.makedirs( vv ) # make a directory for each input file
     pathDst = os.path.join( vv, "%05d.png" ) # deststination path

     os.system("ffmpeg -i {0} {1}".format( v, pathDst ) )
```
