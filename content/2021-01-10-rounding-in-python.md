Title: Rounding in Python
Author: SergeM
Date: 2021-01-10 21:35:00
Slug: rounding-in-python 
Tags: python, math, floating point, 


In school we round numbers like 0.5, 1123.5 towards the bigger number.
That introduce an undesired bias some cases. For example if we have a large data set and
we aggregate some column of it that contains a lot of `.5` fractions. 
In order to adjust for it in many cases a rounding of 0.5 towards nearest even number is applied.

Rounding in python, numpy and pytorch works like this.

Truncation like `int(0.5)` and `int(1.5)` just keeps the integer part.

    >>> import torch
    >>> import math
    >>> import numpy as np

Defining array with a lot of `.5`-s:    

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

    >>> torch.tensor(a, dtype=torch.int)
    tensor([0, 0, 1, 1, 2, 2, 3, 3, 4, 4], dtype=torch.int32)

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
