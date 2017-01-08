Title: VapourSynth: pythonic alternative to avisynth
Author: SergeM
Date: 2014-01-25 21:47:00
Slug: vapoursynth-pythonic-alternative-to
Tags: vapoursynth,avisynth

What do I know about VapourSynth

[http://www.vapoursynth.com/](http://www.vapoursynth.com/)&nbsp;- website
<h2 style="text-align: left;">How to save data from VapourSynth</h2><div>You need to use vspipe.exe from Vapour distributive</div><div>It seems it returns raw data to stdout</div><div>

</div><h3 style="text-align: left;">Render using ffmpeg</h3><div>Don't know how jet</div><div>
</div><div><h3>Render using ImageMagick/convert</h3><div>Don't know how jet</div><div>
<div><h2>Image Reading</h2></div><div>Image reading causes crash of AvsPmod, in which I using Vapoursynth</div><div>[http://forum.doom9.org/showthread.php?t=166088](http://forum.doom9.org/showthread.php?t=166088)</div><div>src:&nbsp;[https://github.com/chikuzen/vsimagereader](https://github.com/chikuzen/vsimagereader" target="_blank)</div><div>
</div><h2 style="text-align: left;">Other</h2></div></div>
AvsPmod - new version of AvsP. AvsP is a tabbed avs editor with convenient results preview.
[http://avspmod.github.io/](http://avspmod.github.io/)

In version 2.4.0 temporary support of vapour scripts was added to AvsPmod ([http://forum.doom9.org/showthread.php?t=153248](http://forum.doom9.org/showthread.php?t=153248))
And it's true.

My first working script:

<span style="background-color: #cccccc; font-family: Courier New, Courier, monospace;">import vapoursynth as vs #include vapour module</span>
<span style="background-color: #cccccc; font-family: 'Courier New', Courier, monospace;">
</span><span style="background-color: #cccccc; font-family: 'Courier New', Courier, monospace;">core = vs.get_core() # some core loading</span>
<span style="background-color: #cccccc; font-family: Courier New, Courier, monospace;">
</span><span style="background-color: #cccccc; font-family: Courier New, Courier, monospace;">src = core.avisource.AVISource('frm.avi') # opening frm.avi</span>
<span style="background-color: #cccccc; font-family: Courier New, Courier, monospace;">
</span><span style="background-color: #cccccc; font-family: Courier New, Courier, monospace;"># it doesn't work without whis line and</span>
<span style="background-color: #cccccc; font-family: Courier New, Courier, monospace;"># prints error message "Avisynth open failure:&nbsp;</span>
<span style="background-color: #cccccc;"><span style="font-family: Courier New, Courier, monospace;">#&nbsp;</span><span style="font-family: 'Courier New', Courier, monospace;">VFW module doesn't </span><span style="font-family: 'Courier New', Courier, monospace;">support RGB24 output"</span></span>
<span style="background-color: #cccccc; font-family: Courier New, Courier, monospace;">ret = core.resize.Bicubic(src, format=vs.COMPATBGR32)</span>

<span style="background-color: #cccccc; font-family: Courier New, Courier, monospace;">ret.set_output()</span>


Interesting bug:
For RGB24 avi file it outputs image flipped vertically:
![](http://1.bp.blogspot.com/-BDcligyliF4/UuP7V5bdfQI/AAAAAAAAAb4/4RDbCzqMlUg/s1600/avspmod_vapoursynth.png)In YUV format it's ok.

[AvxSynth](https://github.com/avxsynth/avxsynth/wiki)&nbsp;- linux port of Avisynth

[https://github.com/chikuzen/VapourSource](https://github.com/chikuzen/VapourSource)&nbsp;- avisynth plugin for loading VapourSynth scripts
<div>
It seems VapourSynth developer is little bit crazy: he wants everysthing be in C instead of C++ (http://www.vapoursynth.com/2012/11/vapoursynth-tasks/)


</div></div>