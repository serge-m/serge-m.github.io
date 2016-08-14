Title: pypy with numpy
Author: SergeM
Date: 2016-05-16 00:11:00
Slug: pypy-with-numpy
Tags: numpy,python,pypy

<div dir="ltr" style="text-align: left;" trbidi="on">Looks like pypy now can build numpy. Well, a slightly modified numpy.

1. Get default branch of pypy. be careful cause the developers don't maintain default branch compilable. Revision&nbsp;<span style="font-family: monospace; font-size: 9pt;">84341 (c86b42dd7613) works for me.</span>
<span style="font-family: monospace; font-size: 9pt;">2. compile using&nbsp;</span>
<span style="font-family: monospace;"><span style="font-size: 12px;">./rpython/bin/rpython -O2 ./pypy/goal/targetpypystandalone.py --withoutmod-micronumpy</span></span>
<span style="font-family: monospace;"><span style="font-size: 12px;">3. Create package and vitual environment. Something like this:</span></span>
<span style="font-family: monospace;"><span style="font-size: 12px;">./pypy/tool/release/package.py --targetdir ./my_builds/build.tar.bz2 --builddir ./tmp/ --nostrip --archive-name pypy_84341</span></span>
<span style="font-family: monospace;"><span style="font-size: 12px;">Needed to copy pypy-c and libpypy to pypy/goal beforehand.</span></span>
4. Clone and follow instructions from
https://github.com/pypy/numpy/commits/cpyext-ext
Revision 3299d0d76fdb831fbcb4429a89c1f53bb36ea07f worked for me

Testing results:
----------------------------------------------------------------------
Ran 5900 tests in 78.216s

FAILED (KNOWNFAIL=3, SKIP=6, errors=218, failures=83)
<div>


scipy can be compiled if disabling submodules io/matlab and spatial. Though is still doesn't work.</div></div>