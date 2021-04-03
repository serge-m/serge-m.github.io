---
Title: Use Matlab function from python
Author: SergeM
Date: 2014-08-31 11:56:00
Slug: use-matlab-function-from-python
aliases: [/use-matlab-function-from-python.html]
Tags: [ python,matlab]
---



There are several solutions:
Source: [http://stackoverflow.com/questions/2883189/calling-matlab-functions-from-python](http://stackoverflow.com/questions/2883189/calling-matlab-functions-from-python)
<h2>pymat</h2>A low level interface to Matlab using the matlab engine (<code>libeng</code>) for communication (basically a library that comes with matlab). The module has to be compiled and linked with libeng.
  [http://pymat.sourceforge.net](http://pymat.sourceforge.net/" rel="nofollow)
Last updated: 2003
  <h2>pymat2</h2>A somewhat short lived continuation of the pymat development. Seems  to work on windows (including 64bit), linux and mac (with some changes).
  [https://code.google.com/p/pymat2/](https://code.google.com/p/pymat2/" rel="nofollow)
Last updated: 2012
  <h2>mlabwrap</h2>A high level interface that also comes as a module which needs compilation and linking against  <code>libeng</code>. It exposes Matlab functions to python so you can do fun stuff like
  <code>mlab.plot(x, y, 'o')</code>
  [http://mlabwrap.sourceforge.net](http://mlabwrap.sourceforge.net/" rel="nofollow)
Last updated: 2009
  <h2>mlab</h2>A repackaging effort of mlabwrap. Basically it replaces the c++ code that links against 'libeng' in <em>mlabwrap</em> with a python module ([matlabpipe](https://code.google.com/p/danapeerlab/source/browse/trunk/freecell/depends/common/python/matlabpipe.py" rel="nofollow)) that communicates with matlab through a pipe. The main advantage of this is that it doesn't need compilation of any kind.
  Unfortunately the package currently has a couple of bugs and doesn't  seem to work on the mac at all. I reported a few of them but gave up  eventually. Also, be prepared for lots of trickery and a bunch of pretty  ugly hacks if you have to go into the source code ;-) If this becomes  more mature it could be one of the best options.
  [https://github.com/ewiger/mlab](https://github.com/ewiger/mlab" rel="nofollow)
last update: 2013
  <h2>pymatlab</h2>A newer package (2010) that also interacts with Matlab through <code>libeng</code>. Unlike the other packages this one loads the engine library through [ctypes](https://docs.python.org/2/library/ctypes.html" rel="nofollow) thus no compilation required. Its not without flaws but still being  maintained and the (64bit Mac specific) issues I found should be easy  enough to fix.
(<strong>edit 2014-05-20</strong>: it seems those issues have already been fixed in the source so things should be fine with 0.2.4)
  [http://pymatlab.sourceforge.net](http://pymatlab.sourceforge.net/" rel="nofollow)
last update: 2014
  <h2>python-matlab-bridge</h2>Also a newer package that is still actively maintained. Communicates  with Matlab through some sort of socket. Unfortunately the exposed  functions are a bit limited. I couldn't figure out how to invoke a  function that takes structs as parameters. Requires zmq, pyzmq and  IPython which are easy enough to install.
  [http://arokem.github.io/python-matlab-bridge](http://arokem.github.io/python-matlab-bridge" rel="nofollow)
last update: 2014


Bug report for Mlab:

http://stackoverflow.com/questions/20659616/python-mlab-cannot-import-name-find-available-releases
Fixed here:
https://github.com/ewiger/mlab/commit/4bfa59af2a1a996a774c80d7aafc4a390f548669
&nbsp;
