Title: Error spawning cmd.exe
Author: SergeM
Date: 2013-05-12 14:11:00
Slug: error-spawning-cmdexe
Tags: c++,errors,visual studio

I got error message&nbsp;<blockquote class="tr_bq"><span style="font-family: Courier New, Courier, monospace;">Error spawning cmd.exe</span></blockquote>during compiling of Blender sources.
The cause was in system PATH environment variable. Some buggy software I had installed and uninstalled before erased all contents of PATH. So I found out that Visual Studio 2008 has missing paths to
<blockquote class="tr_bq"><span style="font-family: Courier New, Courier, monospace;">%SystemRoot%\system32;
%SystemRoot%;
%SystemRoot%\System32\Wbem;</span></blockquote>A added it and the problem gone.&nbsp;