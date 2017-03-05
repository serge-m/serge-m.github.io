Title: Mocking in Python
Author: SergeM
Date: 2017-03-06 00:01:00
Slug: mocking-in-python
Tags: python, testing, unittests


Let's consider  how python standard unittest module suppose to use mocks.
Let's say we have a following class:

```python
class Foo:
  def 
```

Here is how we can test object creation (Snippet is taken example from [official documentation](https://docs.python.org/3/library/unittest.mock.html)):
```python
from unittest.mock import patch
@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
    module.ClassName1()
    module.ClassName2()
    assert MockClass1 is module.ClassName1
    assert MockClass2 is module.ClassName2
    assert MockClass1.called
    assert MockClass2.called

test()
```




https://github.com/kaste/mockito-python
