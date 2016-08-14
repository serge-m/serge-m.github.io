Title: Debugging numpy (any C code of Python) using gdb
Author: SergeM
Date: 2016-04-04 00:01:00
Slug: debugging-numpy-any-c-code-of-python
Tags: useful,python

<div dir="ltr" style="text-align: left;" trbidi="on">I created a tiny python script that executes some python code, that executes some C code:

<span style="font-family: Courier New, Courier, monospace;"># contents of&nbsp;dbg_broadcast.py</span>
<span style="font-family: Courier New, Courier, monospace;">import numpy</span>
<span style="font-family: Courier New, Courier, monospace;">print list(numpy.broadcast([[1,2]],[[3],[4]]))</span>

<span style="font-family: Courier New, Courier, monospace;">> gdb python</span>
<span style="font-family: Courier New, Courier, monospace;">GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1</span>
<span style="font-family: Courier New, Courier, monospace;">Copyright (C) 2014 Free Software Foundation, Inc.</span>
<span style="font-family: Courier New, Courier, monospace;">License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html></span>
<span style="font-family: Courier New, Courier, monospace;">This is free software: you are free to change and redistribute it.</span>
<div>.................. bla bla bla ..................................................</div><div>
</div><div># Adding breakpoint to function "arraymultiter_new" (example):</div><div><span style="font-family: Courier New, Courier, monospace;">(gdb) break arraymultiter_new</span></div><div>
</div><div># There is name completition by Tab.</div><div># Run script</div><div><span style="font-family: Courier New, Courier, monospace;">(gdb) run dbg_broadcast.py&nbsp;</span></div><div><span style="font-family: Courier New, Courier, monospace;">Starting program: /home/asdasd/work/bin/python dbg_broadcast.py</span></div><div><div><span style="font-family: Courier New, Courier, monospace;">[Thread debugging using libthread_db enabled]</span></div><div><span style="font-family: Courier New, Courier, monospace;">Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".</span></div><div><span style="font-family: Courier New, Courier, monospace;">
</span></div><div><span style="font-family: Courier New, Courier, monospace;">Breakpoint 1, arraymultiter_new (__NPY_UNUSED_TAGGEDsubtype=0x7ffff6abbf80 <PyArrayMultiIter_Type>,&nbsp;</span></div><div><span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; args=0x7ffff32dd050, kwds=0x0) at numpy/core/src/multiarray/iterators.c:1578</span></div><div><span style="font-family: Courier New, Courier, monospace;">1578<span class="Apple-tab-span" style="white-space: pre;"> </span>{</span></div><div><span style="font-family: Courier New, Courier, monospace;">(gdb)&nbsp;</span></div></div><div>
</div><div>
</div><div>And here we are.</div><div>
</div>

<div>
</div><div>
</div></div>