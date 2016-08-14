Title: Building Pypy
Author: SergeM
Date: 2016-03-22 21:51:00
Slug: building-pypy
Tags: pypy

<div dir="ltr" style="text-align: left;" trbidi="on">Pypy builds faster if using -O2 option.



To build faster (according to pypy documentation) use prebuilt pypy from&nbsp;[http://buildbot.pypy.org/nightly/trunk/](http://buildbot.pypy.org/nightly/trunk/)

Using virtualenv to create virtual environment for it.

Build script (to be placed in pypy source directory):

<span style="font-family: Courier New, Courier, monospace;">#!/bin/bash</span>
<span style="font-family: Courier New, Courier, monospace;">cd pypy/goal || exit 1</span>
<span style="font-family: Courier New, Courier, monospace;">source <path to existing pypy environment>/bin/activate || exit 2</span>
<span style="font-family: Courier New, Courier, monospace;">pypy ../../rpython/bin/rpython --batch -O2 targetpypystandalone</span>
<div>
</div><div>
</div><div>
</div></div>