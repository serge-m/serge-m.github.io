Title: Speed up make/cmake build with multiprocessing
Author: SergeM
Date: 2017-07-29 16:07:00
Slug: parallel-builds
Tags: make,cmake,python,parallel


Build time can be reduced by using multiple cores of your processor.

Parallelization for make:
```
make -j8
```

Parallelization for cmake:
```
cmake --build <bindir> -- -j 8
```


Sometimes you cannot pass parameters directly to `make`. For example you are installing a python module using 
```
python setup.py install
```
Setup script doesn't accept parameters.
Then you could pass them through environment variables:
```
export MAKEFLAGS="-j 8"
```
