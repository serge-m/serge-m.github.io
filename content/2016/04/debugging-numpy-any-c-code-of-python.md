Title: Debugging numpy (any C code of Python) using gdb
Author: SergeM
Date: 2016-04-04 00:01:00
Slug: debugging-numpy-any-c-code-of-python
Tags: useful,python


I created a tiny python script that executes some python code, that executes some C code:

```
# contents of dbg_broadcast.py
import numpy
print list(numpy.broadcast([[1,2]],[[3],[4]]))
```

Running in console:
```
> gdb python
GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
.................. bla bla bla ..................................................

# Adding breakpoint to function "arraymultiter_new" (example):
(gdb) break arraymultiter_new

# There is name completition by Tab.
# Run script
(gdb) run dbg_broadcast.py

Starting program: /home/asdasd/work/bin/python dbg_broadcast.py
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Breakpoint 1, arraymultiter_new (__NPY_UNUSED_TAGGEDsubtype=0x7ffff6abbf80 <PyArrayMultiIter_Type>,
    args=0x7ffff32dd050, kwds=0x0) at numpy/core/src/multiarray/iterators.c:1578
1578 {

(gdb)
```


And here we are.