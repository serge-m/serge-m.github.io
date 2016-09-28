Title: Building Pypy
Author: SergeM
Date: 2016-03-22 21:51:00
Slug: building-pypy
Tags: pypy

Pypy builds faster if using `-O2` option.

To build faster (according to pypy documentation) use prebuilt pypy from [link](http://buildbot.pypy.org/nightly/trunk/)

Using virtualenv to create virtual environment for it.

Build script (to be placed in pypy source directory):

```
#!/bin/bash
cd pypy/goal || exit 1
source <path to existing pypy environment>/bin/activate || exit 2
pypy ../../rpython/bin/rpython --batch -O2 targetpypystandalone
```