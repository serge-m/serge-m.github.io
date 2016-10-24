Title: Refactoring python code. Extracting variables and other.
Author: SergeM
Date: 2016-10-08 01:10:00
Slug: refactoring-python-extract-variable
Tags: python, useful, youtube, video

[Pycon2016 talk by Brett Slatkin](https://www.youtube.com/watch?v=D_6ybDcU5gc)
[Example 1: Extract variable](https://github.com/bslatkin/pycon2016/blob/master/Extract%20Variable.ipynb)

```
import random
month = random.choice(MONTHS)

if (month.lower().endswith('r') or
        month.lower().endswith('ary')):
    print('%s is a good time to eat oysters' % month)
elif 8 > MONTHS.index(month) > 4:
    print('%s is a good time to eat tomatoes' % month)
else:
    print('%s is a good time to eat asparagus' % month)
```


Becomes:

```
class OystersGood:
    def __init__(self, month):
        month = month
        month_lowered = month.lower()
        self.ends_in_r = month_lowered.endswith('r')
        self.ends_in_ary = month_lowered.endswith('ary')
        self._result = self.ends_in_r or self.ends_in_ary

    def __bool__(self):  # Equivalent to __nonzero__ in Python 2
        return self._result


class TomatoesGood:
    def __init__(self, month):
        self.index = MONTHS.index(month)
        self._result = 8 > self.index > 4

    def __bool__(self):  # Equivalent to __nonzero__ in Python 2
        return self._result
```


```
time_for_oysters = OystersGood(month)
time_for_tomatoes = TomatoesGood(month)

if time_for_oysters:
    print('%s is a good time to eat oysters' % month)
elif time_for_tomatoes:
    print('%s is a good time to eat tomatoes' % month)
else:
    print('%s is a good time to eat asparagus' % month)
```

November is a good time to eat oysters

Now the helper function is easy to test and introspect.
```
test = OystersGood('November')
assert test
assert test.ends_in_r
assert not test.ends_in_ary

test = OystersGood('July')
assert not test
assert not test.ends_in_r
assert not test.ends_in_ary
```

[Dependency injection for better testing](http://mauveweb.co.uk/posts/2014/09/every-mock-patch-is-a-little-smell.html)
