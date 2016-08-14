Title: avconv
Author: SergeM
Date: 2015-12-14 22:00:00
Slug: avconv
Tags: useful,ffmpeg

<div dir="ltr" style="text-align: left;" trbidi="on">convert video to jpeg with good quality
<pre class="code _bash">avconv -i input_video.mp4 -qmax 1 -qmin 1 images_%05d.jpg
</pre><div>
</div><div>crop video</div><div>avconv -i input.avi -vf crop=<width>:<height>:<x>:<y> output_%05d.png


create gif using&nbsp;http://gifmaker.me/

</div></div>