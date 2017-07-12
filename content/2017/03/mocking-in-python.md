Title: Mocking in Python
Author: SergeM
Date: 2017-03-06 00:01:00
Slug: mocking-in-python
Tags: python, testing, unittests


Let's consider  how python standard unittest module suppose to use mocks.

Assume we want to test a method that creates and uses objects of other classes:

```python
# content of module.py

# classes that we want to mock
class ClassName1: 
  pass
  
class ClassName2:
  pass

# class that we want to test
class ProductionClass:
  def foo(self, parameter1, parameter2):
    object1 = module.ClassName1("some_initial_parameter1")
    intermediate_result = object1.run(parameter1)
    
    object2 = module.ClassName2("some_initial_parameter2")
    final_result = object2.run(intermediate_result, parameter2)
    
    return final_result
    
```

Here is how we can test object creation (Snippet is taken from [official documentation](https://docs.python.org/3/library/unittest.mock.html)):
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

I would say that in our case we need also to check that each object (`object1` and `object2`) were instanciated and called with correct parameters. Then we can use `assert_called_once_with` like this (example from [official documentation](https://docs.python.org/3/library/unittest.mock.html#quick-guide)):
```python
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, 2, 3)

mock_method.assert_called_once_with(1, 2, 3)
```

Combining things together:

```python

mocked_intermediate_result = "some-intermediate-result"
mocked_final_result = "some-final-result"

from unittest.mock import patch

@patch('module.ClassName2')
@patch('module.ClassName1')
def test_foo(MockClass1, MockClass2):
    MockClass1.return_value.run.return_value = mocked_intermediate_result
    MockClass2.return_value.run.return_value = mocked_final_result
    
    actual_result = module.ProductionClass().foo("parameter1", "parameter2")
    
    assert actual_result == mocked_final_result
    MockClass1.assert_called_once_with("some_initial_parameter1")
    MockClass1.return_value.run.assert_called_once_with("parameter1")
    MockClass2.assert_called_once_with("some_initial_parameter2")
    MockClass2.return_value.run.assert_called_once_with(mocked_intermediate_result, "parameter2")
    
```

Seems good but a little bit too verbose. Assertions on calls could be eliminated. I would like to do it like in Java with [Mockito](http://static.javadoc.io/org.mockito/mockito-core/2.7.13/org/mockito/Mockito.html#stubbing):
```java
when(mockedObject.foo("parameter")).thenReturn("mocked-result");
```

That means you don't need to verify intermediate calls. If they fail, the consequent calls fail as well.

The test would look like this:
```python
@patch('module.ClassName2')
@patch('module.ClassName1')
def test_foo(MockClass1, MockClass2):
    when(MockClass1).__call__("some_initial_parameter1").then_when().run("parameter1").then_return(mocked_intermediate_result)
    when(MockClass2).__call__("some_initial_parameter2").then_when().run(mocked_intermediate_result, "parameter2").then_return(mocked_final_result)
        
    actual_result = module.ProductionClass().foo("parameter1", "parameter2")
    
    assert actual_result == mocked_final_result    
```

You don't need calls assertions in the end. If for example `object1.run(parameter1)` returns something else, then condition of the second mock object is not met and the test fails.


*Question: is there a way to achieve that?*


There is a port of Mockito to Python: [mockito-python](https://github.com/kaste/mockito-python) 
There you can do virtually the same as in Java:
```
from mockito import when, mock, unstub

when(os.path).exists('/foo').thenReturn(True)

# or:
import requests  # the famous library
# you actually want to return a Response-like obj, we'll fake it
response = mock({'status_code': 200, 'text': 'Ok'})
when(requests).get(...).thenReturn(response)

# use it
requests.get('http://google.com/')

# clean up
unstub()
```

But:

* clean up is required

* the module seems not integrating standard unittest's mocks . Maybe I am wrong, more investigation is required. I want to use `mock.patch` and have `when-thenReturn` construction working for it. 

## Similar articles
* [Python Mocking 101: Fake It Before You Make It](https://blog.fugue.co/2016-02-11-python-mocking-101.html)
* [Using the Python mock library to fake regular functions during tests](http://fgimian.github.io/blog/2014/04/10/using-the-python-mock-library-to-fake-regular-functions-during-tests/)

## How to avoid mocking
Python is ~~very~~ too flexible with respect to types. Sometimes it plays agains the developers. If interface of the mocked class `A` changes you don't notice that tests for a dependent class `B` are failing if you mock `A` in `test_B`.

Possible way to avoid it is to pass a factory to the dependent class.

```python
class ClassName1: pass
  
class ClassName2: pass

class ClassFactory:
  def create_instance_class1(self, parameter):
    return ClassName1(parameter)
  
  def create_instance_class2(self, parameter):
    return ClassName2(parameter)
    
  
# class that we want to test
class ProductionClassWithFactory:
  def __init__(self, factory):
    self.factory = factory
    
  def foo(self, parameter1, parameter2)):
    object1 = self.factory.create_instance_class1("some_initial_parameter1")
    intermediate_result = object1.run("parameter1")
    
    object2 = self.factory.create_instance_class2("some_initial_parameter2")
    final_result = object2.run(intermediate_result, parameter2)
    
    return final_result
    
```
Let's test:

```python
def test_foo():
    mocked_obj1 = MagicMock()
    mocked_obj1.run.return_value = "result1"
    mocked_obj2 = MagicMock()
    mocked_obj2.run.return_value = "result2"
    mocked_factory = MagicMock()
    mocked_factory.create_instance_class1.return_value = mocked_obj1
    mocked_factory.create_instance_class2.return_value = mocked_obj2
    
    actual_result = module.ProductionClass(mocked_factory).foo("parameter1", "parameter2")
    
    # check final result:
    assert actual_result == "result2"
    # check calls arguments
    mocked_factory.create_instance_class1.assert_called_once_with("some_initial_parameter1")
    mocked_factory.create_instance_class2.assert_called_once_with("some_initial_parameter2")
    mocked_obj1.run.assert_called_once_with("parameter1")
    mocked_obj2.run.assert_called_once_with("result1", "parameter2")
```


## Matching attributes for mocks
Keep in mind that standard mocks don't care about non-existent atttributes. I use
```python
@patch('module.ClassName1', autospec=True)
```  
instead of 

```python
@patch('module.ClassName1')
```  

That adds automatic checking of non-existent attributes and catches more errors. 
Let's see where `autospec=True` can save your life.

```python

class A:
  def foo():
    return "foo"
    
class B:
  def bar():
    return "bar" + A().foo()
```

here comes a test:
```python
@mock.patch('module.A')
def test_bar(MockedA):
  MockedA.return_value.foo.return_value = "mocked-foo"
  assert B().bar() == "bar" + "mocked-foo"
```

At some point you decide to change class `A`. New version:
```python
class A:
  def oops():
    return "oops"
```
You change tests for `A` but you can forget to fix `B` and tests for `B`.  `test_bar` will still work because mocked `A` still have `foo`. Probably you can catch that error on integration tests level, but it is better to "fail fast".

If you use `@mock.patch('module.A', autospec=True)`, then you get an error (about non-existent attribute) after you change `A` on 
```python
MockedA.return_value.foo.return_value = "mocked-foo"
```


I think `autospec=True` has to be default behaviour of `patch`.



See also [Mocking Objects in Python](https://www.relaxdiego.com/2014/04/mocking-objects-in-python.html) section "Danger: mocking non-existent attributes" 

## Alternative mocking libraries

[Flexmock](https://flexmock.readthedocs.io/en/latest/compare/) -- extended/rebuilt clone of mocking library from Ruby. Abandoned project (last update in github in 2016). 

Interesting syntax. Probably cleaner mocking sometimes. Example from docs for overriding new instances of a class:

```python

# flexmock
flexmock(some_module.SomeClass).new_instances(some_other_object)
assertEqual(some_other_object, some_module.SomeClass())

# .......

# Mock
with mock.patch('somemodule.Someclass') as MockClass:
  MockClass.return_value = some_other_object
  assert some_other_object == some_module.SomeClass()

```

// Will it really work?

## See also about testing in python
* [Run docker as pytest fixture](/run-docker-as-pytest-fixture.html)
* [Testing json responses in Flask REST apps with pytest](/testing-json-responses-in-Flask-REST-apps-with-pytest.html)
* [Refactoring python code. Extracting variables and other.](/refactoring-python-extract-variable.html)
* Alex Marandon. [Python Mock Gotchas](http://alexmarandon.com/articles/python_mock_gotchas/)
* José R.C. Cruz.  [Using Mocks in Python](http://www.drdobbs.com/testing/using-mocks-in-python/240168251#). May 22, 2014
* https://semaphoreci.com/community/tutorials/testing-python-requests-with-betamax

## More about mocking and testing
* Martin Fowler. [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html) 
