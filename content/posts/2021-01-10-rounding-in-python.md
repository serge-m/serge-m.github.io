---
Title: Rounding in Python
Author: SergeM
Date: 2021-01-10 21:35:00
Slug: rounding-in-python 
aliases: [/rounding-in-python.html]
Tags: [ python, math, floating point, ]
---




In school we round numbers like 0.5, 1123.5 towards the bigger number. 
It's a ["round half up"](https://en.wikipedia.org/wiki/Rounding#Round_half_up) method.

That introduces an undesired bias some cases. For example if we have a large data set, and
we aggregate some column containing a lot of `.5` fractions. 
In order to adjust for it in many cases a rounding of 0.5 towards nearest even number is applied.
It's ["Rounding half to even"](https://en.wikipedia.org/wiki/Rounding#Round_half_to_even) or "banker's rounding".

This method is used in IEEE Standard for Floating-Point Arithmetic (IEEE 754).
Python, numpy and pytorch use it as well.

Truncation like `int(0.5)` and `int(1.5)` just keeps the integer part.

### Example

    >>> import torch
    >>> import math
    >>> import numpy as np

Defining an array with a lot of `.5`-s:    

    >>> a = [x / 2. for x in range(10)]
    >>> a
    [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]


Truncation just keeps the integer part:

    >>> list(map(int, a))
    [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]

Rounding introduces more even numbers:    

    >>> list(map(round, a))
    [0, 0, 1, 2, 2, 2, 3, 4, 4, 4]


Truncation in pytorch:

    >>> # deprecated
    >>> torch.tensor(a, dtype=torch.int)
    tensor([0, 0, 1, 1, 2, 2, 3, 3, 4, 4], dtype=torch.int32)

    >>> # ok
    >>> torch.tensor(a, dtype=torch.float64).type(torch.int64)
    tensor([0, 0, 1, 1, 2, 2, 3, 3, 4, 4])


Rounding in pytorch:

    >>> torch.tensor(a, dtype=torch.float64).round()
    tensor([0., 0., 1., 2., 2., 2., 3., 4., 4., 4.], dtype=torch.float64)
    

Truncation and rounding in numpy works the same way:

    >>> np.array(a, dtype=np.int)
    array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4])

    >>> np.round(a)
    array([0., 0., 1., 2., 2., 2., 3., 4., 4., 4.])


Round half up in python:

    >>> def round_half_up(x):
    >>>    return math.floor(x+0.5)
    >>>
    >>> list(map(round_half_up, a))
    [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]    


References:

* [jupyter notebbok](https://gist.github.com/serge-m/de45997d87fcc2e8a869a5f2a5cc4fb9) in github gist.
