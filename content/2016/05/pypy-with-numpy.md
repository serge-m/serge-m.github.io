Title: pypy with numpy
Author: SergeM
Date: 2016-05-16 00:11:00
Slug: pypy-with-numpy
Tags: numpy,python,pypy

Looks like pypy now can build numpy. Well, a slightly modified numpy.

1. Get default branch of pypy. be careful cause the developers don't maintain default branch compilable.
    Revision 84341 (c86b42dd7613) works for me.

2. compile using

        ./rpython/bin/rpython -O2 ./pypy/goal/targetpypystandalone.py --withoutmod-micronumpy

3. Create package and vitual environment. Something like this:

        ./pypy/tool/release/package.py --targetdir ./my_builds/build.tar.bz2 --builddir ./tmp/ --nostrip --archive-name pypy_84341

    Needed to copy pypy-c and libpypy to pypy/goal beforehand.

4. Clone and follow instructions from
    [https://github.com/pypy/numpy/commits/cpyext-ext](https://github.com/pypy/numpy/commits/cpyext-ext)
    Revision 3299d0d76fdb831fbcb4429a89c1f53bb36ea07f worked for me

    UPDATE: link doesn't work any more. try to find corresponding link in bitbucket->pypy/

        Testing results:
        ----------------------------------------------------------------------
        Ran 5900 tests in 78.216s

        FAILED (KNOWNFAIL=3, SKIP=6, errors=218, failures=83)


scipy can be compiled if disabling submodules io/matlab and spatial. Though is still doesn't work.