Title: Problems with debug run from Visual Studio with openMP
Author: SergeM
Date: 2013-05-14 12:14:00
Slug: problems-with-debug-run-from-visual
Tags: 

I had a problem while running debug+openmp configuration of my console. Meanwhile in Release+openmp configuration everything is ok. Diagnostic message I see is something about wrong parallel configurations, system log and sxstrace.exe.
![](http://4.bp.blogspot.com/-XL6WF2QIesk/UZHwxlLsObI/AAAAAAAAAYE/9_XJHGufbj8/s320/error_about_parallel_configurations.png)
The solution is following.
Folder
<blockquote class="tr_bq">Microsoft.VC90.DebugOpenMP</blockquote>with files
<blockquote class="tr_bq">Microsoft.VC90.DebugOpenMP.manifest
vcomp90d.dll&nbsp;</blockquote>were missing. I knew this problem for the folder I specify in debug properties in visual studio:
![](http://3.bp.blogspot.com/-YWMVBmpI050/UZHxfnKVd5I/AAAAAAAAAYM/8syrhPsNbIc/s320/error_about_parallel_configurations_dialog1.png)In that folder I already had Microsoft.VC90.DebugOpenMP. But to avoid error I should place it in output directory (where my binary exe file is placed):
![](http://1.bp.blogspot.com/-rCC2c5cq7Lo/UZHyERiXNRI/AAAAAAAAAYU/wbQWL9p0MbE/s320/error_about_parallel_configurations_dialog2.png)
Magick...

