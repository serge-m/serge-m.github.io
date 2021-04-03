---
Title: Installing torch for miniconda
Author: SergeM
Date: 2016-06-26 22:11:00
Slug: installing-torch-for-miniconda
aliases: [/installing-torch-for-miniconda.html]
Tags: [ workaround]
---



I got the error while installing torch for miniconda. Something like
Linking CXX executable mshrable
```
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `BC'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgetnum'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `PC'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tputs'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgetent'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgetflag'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgoto'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `UP'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgetstr
```

The same was for python3 and python2 environments. 
The solution (at least for python 2) was to remove miniconda from path and compile torch with the system python.

Solution from [here](https://github.com/ContinuumIO/anaconda-issues/issues/152)

same here, temporay fix for me is to remove conda readline from the environment:
```
conda remove --force readline
```

and install the python bindings with
```
pip install readline
```

That way, I presume it is using the system ```readline```
