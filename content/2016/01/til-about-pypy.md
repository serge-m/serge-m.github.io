Title: TIL about PyPy
Author: SergeM
Date: 2016-01-08 08:30:00
Slug: til-about-pypy
Tags: python,pypy

Building from source root using command
<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">pypy_src$ rpython/bin/rpython -Ojit pypy/goal/targetpypystandalone.py</span>
produces structure with obsolete pypy-c and libpypy-c.so in 
<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">/tmp/usession-release-4.0.1-XXXX/build/pypy-nightly/bin/</span>

Probably pypy compiler places there files  integrated in the src distribution. To get fresh versions I had to use pypy-c and libpypy-c.so from sources root.

UPDATE:
Probably I was completely wrong.
pypy/tool/release/package.py has an option for (not) stripping resulting binary file: "--nostrip". By default it is enabled. Looks like it removed something unused from binaries. This operation updates timestamp of the pypy-c and libpypy-c.so. So probably that was the cause of my misunderstanding.


Script for packaging and creating virtual environment:


    ::::
    #!/bin/bash
    
    rm -rf ./my_builds/ || exit 2
    mkdir ./my_builds/ || exit 3
    
    DST_NAME=$1
    if [ -z "$DST_NAME" ]; then
        echo "DST_NAME is  empty"
        exit 3
    fi
    
    # runs packaging
    ./pypy/tool/release/package.py --builddir /home/pypy/builds/ --nostrip --archive-name $DST_NAME || exit 4
    
    # creates a new virtual environment
    virtualenv -p /home/pypy/builds/$DST_NAME/bin/pypy /home/pypy/env/$DST_NAME
    
    # installing nose for numpy testing (optional)
    source /home/pypy/env/$DST_NAME/bin/activate
    pip install nose
    
    

<div>
</div>
</div>