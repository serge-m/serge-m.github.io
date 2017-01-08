Title: clang: error: linker command failed with exit code 1 
Author: SergeM
Date: 2014-03-20 16:14:00
Slug: clang-error-linker-command-failed-with
Tags: c++,xcode,clang

Finally I solved the problem with broken clang compilation
I always got message

        <div class="p1"><span style="font-family: Courier New, Courier, monospace;">ld: malformed archive TOC entry for <long strange identifier>, offset 362137760 is beyond end of file 303710208</span></div><div class="p1"><span style="font-family: Courier New, Courier, monospace;">&nbsp;for architecture x86_64</span></div><div class="p1"><span style="font-family: Courier New, Courier, monospace;">clang: error: linker command failed with exit code 1 (use -v to see invocation)</span></div><div class="p1">
</div><div class="p1">when I interrupted compilation of a large project. And the only way to build a project was to clean and build again. It took a long time.&nbsp;</div><div class="p1">I found out I don;t need rebuild all if I delete all files from Debug directory. After that Xcode only relinks the project. It is much faster.</div><div class="p1">
</div>