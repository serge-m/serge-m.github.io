Title: Tips for debugging of video processing console
Author: SergeM
Date: 2013-05-16 13:31:00
Slug: tips-for-debugging-of-video-processing
Tags: 

Assume we have Visual Stusio solution for console that makes some video processing.
The console takes two input videos and generates the third video:
<blockquote class="tr_bq"><span style="font-family: Courier New, Courier, monospace;">Console.exe --input1 video1.avi --input2 video2.avi --output result.avi</span></blockquote>While debugging we need to run console on several datasets.
1) dataset1 conststs of videos set1_video1.avi and set1_video2.avi
2) dataset2 conststs of videos set2_video1.avi and set2_video2.avi
....
n) ....

It seem rather convenient to distrubute videos between folders. One folder for each dataset. Insise the folder we should give template names to files (e.g. video1.avi and video2.avi)
Therefore now we can set "Command Arguments" in "Project Properties->Configuration properties->Debugging" the same arguments for all cases and configurations,
The thing should vary is "Working directory" in "Properties->Configuration properties->Debugging".


Another usefull thing is setting &nbsp;"Environment". Just write there
<span style="font-family: Courier New, Courier, monospace;">PATH=%PATH%;<path to dll></span>
and you don't need to copy all dependency dll's in every debug folder.&nbsp;