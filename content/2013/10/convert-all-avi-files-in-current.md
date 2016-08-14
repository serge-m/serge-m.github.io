Title: Convert all *.avi files in current directory to png sequences 
Author: SergeM
Date: 2013-10-22 23:49:00
Slug: convert-all-avi-files-in-current
Tags: 

<div dir="ltr" style="text-align: left;" trbidi="on">Using python and ffmpeg:

<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">#!/usr/bin/python</span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"># -*- coding: cp1251 -*-</span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">
</span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;">import glob</span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">import os</span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">
</span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;">t=glob.glob("*.avi" ) # search all AVI files</span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">
</span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;">for v in t:</span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp;vv = os.path.splitext(v)[0];</span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp;os.makedirs( vv ) # make a directory for each input file</span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp;pathDst = os.path.join( vv, "%05d.png" ) # deststination path</span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"> </span>
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp;os.system("ffmpeg -i {0} {1}".format( v, pathDst ) )</span></div>