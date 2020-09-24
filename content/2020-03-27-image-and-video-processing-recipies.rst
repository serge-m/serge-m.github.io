:date: 2020-03-27 07:18:23

:title: Image and video processing recipes

:author: SergeM

:slug: image-and-video-processing-recipes

:tags: ffmpeg, video, image, command line


I often need to perform some operations on video. Usually I use linux and ffmpeg to do that, but I strugle to remember all the commands.
Therefore I usually google it. I'll try to collect here some recipes that I usually use with a bit of explanations.

Video conversions
==========================

Cut a range of frames
---------------------------

Cut a range of frames (100, 130) from a video and save it to mp4 with a good quality using x264 codec:

.. code-block:: sh

  ffmpeg -i ./input_video.mp4 -vf "select=between(n\,100\,130)" -vsync 0 -vcodec libx264 -crf 15 -an ./output.mp4


Explanation:

* ``-vf "select=between(n\,100\,130)"`` - cut according to the frame numbers. Slash symbols are essential.

* ``-vsync 0`` - some synchronization magic. Without it some duplicated/ freezed frames are added.

* ``-crf 15`` - good quality, large output file. set to a bigger value if you need more compression.

* ``-an`` removes audio from the file. otherwise some black frames are added. I think there is a way to cut audio track as well, I just don't need it usually.



Cut according to time (between seconds 5.5 and 122):

.. code-block:: sh

    ffmpeg -y -i ./input_video.mp4 -vf "select=between(t\,5.5\,122)" -vsync 0 -vcodec libx264 -crf 15 -an ./output.mp4



Convert to jpeg
---------------------------

.. code-block:: sh

    ffmpeg -i ./input_video.mp4 -qmax 1 -qmin 1 -start_number 0 output_image_%05d.jpg


Stack images/videos
--------------------------------------------------

.. code-block:: sh

  # stack horizontally
  ffmpeg -i input0.mp4 -i input1.mp4 -filter_complex hstack=inputs=2 output.mp4

  # stack vertically
  ffmpeg -i input0.mp4 -i input1.mp4 -filter_complex vstack=inputs=2 output.mp4





See also
==============================

* FFmpeg libav tutorial - learn how media works from basic to transmuxing, transcoding and more

  `ffmpeg-libav-tutorial  on github <https://github.com/leandromoreira/ffmpeg-libav-tutorial>`_

  `How to Write a Video Player in Less Than 1000 Lines <http://dranger.com/ffmpeg/>`_

