---
Title: Symbolic math and python
Author: SergeM
Date: 2020-12-31 08:00:00
Slug: symbolic-math-and-python 
aliases: [/symbolic-math-and-python.html]
Tags: [ python, symbolic math, math, cross product, sympy]
---




With the help of python and [SymPy](https://www.sympy.org/en/index.html) module one can do pretty neat computations.
For example when I took a course about Robotic Preception on Coursera I had to find a cross product of 
two vectors `v1 x v2` represented in a generic form:

    v1 = (a, b, c)
    v2 = (d, e, 0)

Normally I would write it down on a piece of paper and do the computations myself.
Luckily python can help with that.
Unfortunately it takes a bit of work to explain to SymPy what you want. But it is worth the trouble.

First we install Sympy:

    pip install sympy


Now we can switch to python/ipython/jupyter. Import the module

    from sympy import *

For vector representation we have to define a coordinate system:

    from sympy.vector import CoordSys3D
    C = CoordSys3D('C')

also we need a could of generic symbols:

    a, b, c, d, e = symbols('a b c d e ')


Now we can define our vectors in that coordinate system using the symbols:

    v1 = a*C.i + b*C.j + c*C.k
    v2 = d*C.i + e*C.j + 0*C.k

And finally we can compute the cross product:

    >>> v1.cross(v2)
    (-c*e)*C.i + c*d*C.j + (a*e - b*d)*C.k

So the answer is `(-ce, cd, ae-bd)`.

Alternative operator for the cross product:

    >>> v1 ^ v2
    (-c*e)*C.i + c*d*C.j + (a*e - b*d)*C.k


More info about vector operations: [SymPy documentation](https://docs.sympy.org/latest/modules/physics/vector/api/classes.html#vector)
