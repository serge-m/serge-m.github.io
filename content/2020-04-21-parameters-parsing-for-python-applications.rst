:date: 2020-04-21 19:00:00

:title: Parameters parsing for python applications

:author: SergeM

:slug: parameters-parsing-for-python-applications

:tags: python, argparse, click, fire, useful


Parameters parsing for python applications
============================================

command line arguments is a standard and one of the most common ways to pass parameters to a python script.
There exist a list of python libraries that help with that task. Here I am going to list some of them.


argparse
---------------------------

The default choice for the python developer.
The module is included in python standard library and comes together with any python distribution.


Example of usage:


.. code-block:: python

    #!/usr/bin/env python3
    import argparse


    def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for x in range(count):
            print('Hello %s!' % name)


    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--count', help='Number of greetings.', type=int, default=1)
        parser.add_argument('name', help='The person to greet.')
        args = parser.parse_args()
        hello(args.count, args.name)


.. code-block:: sh

    $ ./test.py john --count 2
    Hello john!
    Hello john!
    $ ./test.py john
    Hello john!
    $ ./test.py --name john
    usage: test.py [-h] [--count COUNT] name
    test.py: error: unrecognized arguments: --name





click
-----------------------------

custom module that I now use by default.
Provides a pretty concise interface that turns function parameters in to command line parameters.
Another advantage is that it solves the problem with ambiguous and non-obvious rules of argument parsing in `argparse`.

Some known drawbacks of click: issues with unicode:

    Click supports Python 3, but like all other command line utility libraries,
    it suffers from the Unicode text model in Python 3.
    All examples in the documentation were written so that they could run on both Python 2.x and Python 3.4 or higher.

see `python3-limitations <https://click.palletsprojects.com/en/7.x/python3/#python3-limitations>`_ for more information

Example of usage:

.. code-block:: python

    #!/usr/bin/env python3
    import click

    @click.command()
    @click.option('--count', default=1, help='Number of greetings.')
    @click.option('--name', help='The person to greet.')
    def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for x in range(count):
            print('Hello %s!' % name)

    if __name__ == '__main__':
        hello()


Running :

.. code-block:: sh

    $ ./test.py --name john --count 3
    Hello john!
    Hello john!
    Hello john!
    $ ./test.py --name john
    Hello john!
    $ ./test.py john
    Usage: test.py [OPTIONS]
    Try 'test.py --help' for help.

    Error: Missing option '--name'.


As you can see you cannot mix positional and named arguments. To define positional arguments you have to use `argument`

.. code-block:: python

    #!/usr/bin/env python3
    import click

    @click.command()
    @click.option('--count', default=1, help='Number of greetings.')
    @click.argument('name', required=True, )
    def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        for x in range(count):
            print('Hello %s!' % name)

    if __name__ == '__main__':
        hello()


.. code-block:: sh

    $ ./test.py john  --count
    Error: --count option requires an argument
    $ ./test.py john  --count 3
    Hello john!
    Hello john!
    Hello john!
    $ ./test.py --name john  --count 3
    Usage: test.py [OPTIONS] NAME
    Try 'test.py --help' for help.

    Error: no such option: --name




How to make a flag:
*************************************************

.. code-block:: python

    @click.option('--shout', is_flag=True)


google's fire
--------------------------------------

https://github.com/google/python-fire

Examples from the official `documentation <https://github.com/google/python-fire/blob/master/docs/guide.md>`_ :

.. code-block:: python

    import fire

    def add(x, y):
      return x + y

    def multiply(x, y):
      return x * y

    if __name__ == '__main__':
      fire.Fire()

.. code-block:: sh

    $ python example.py add 10 20
    30
    $ python example.py multiply 10 20
    200


another example:

.. code-block:: python

  import fire

  class Calculator(object):
    def add(self, x, y):
      return x + y

    def multiply(self, x, y):
      return x * y

  if __name__ == '__main__':
    fire.Fire(Calculator)


.. code-block:: sh

    $ python example.py add 10 20
    30
    $ python example.py multiply 10 20
    200


the library also turns function parameters into command line arguments.
Types are deducted automatically. That can be bad sometimes. However one has to check the validity of the  input anyway.

    The types of the arguments are determined by their values, rather than by the function signature where they're used.
    You can pass any Python literal from the command line: numbers, strings, tuples, lists, dictionaries,
    (sets are only supported in some versions of Python).
    You can also nest the collections arbitrarily as long as they only contain literals.















