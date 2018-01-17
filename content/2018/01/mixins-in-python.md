Title: Mixin pattern in Python
Author: SergeM
Date: 2018-01-10 07:50
Slug: mixins-in-python
Tags: mixins,python,design patterns


Design pattern [Mixin](https://en.wikipedia.org/wiki/Mixin) is often used in python. 
 There are two main situations where mixins are used [1](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful):

* You want to provide a lot of optional features for a class.
* You want to use one particular feature in a lot of different classes.


## Order of mixins definition 
Order in which you use mixins defines the behaviour. 
Quote from [2](https://www.ianlewis.org/en/mixins-and-python):

  in Python the class hierarchy is defined right to left, so in this case the Mixin2 class is the base class, extended by Mixin1 and finally by BaseClass. This is usually fine because many times the mixin classes don't override each other's, or the base class' methods. But if you do override methods or properties in your mixins this can lead to unexpected results because the priority of how methods are resolved is from left to right.

```python
class BaseClass(object):
    def test(self):
        print ("BaseClass")
        
class Mixin1(object):
    def test(self):
        print ("Mixin1")

class Mixin2(object):
    def test(self):
        print( "Mixin2")
```

Now this code 
```python
class MyClass(BaseClass, Mixin1, Mixin2):
    pass

MyClass().test()

```
prints
```
BaseClass
```

If you change the order of mixins:
```python
ass MyClass(Mixin2, Mixin1, BaseClass, ):
    pass

MyClass().test()
```
you get
```
Mixin2
```



## References
1. [What is a mixin, and why are they useful?](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful)
2. [Mixins and Python](https://www.ianlewis.org/en/mixins-and-python)






