---
Title: Useful python links
Author: SergeM
Date: 2016-10-08 01:10:00
Slug: useful-python-links
aliases: [/useful-python-links.html]
Tags: [ python, useful, youtube, video, packaging, setup.py, tox, pytest]
---



## Books

* [Test-Driven Development with Python](http://chimera.labs.oreilly.com/books/1234000000754/index.html)
Harry Percival

* [Python Testing with unittest, nose, pytest : eBook](http://pythontesting.net/books/python-testing-ebook/)

* Testing Python: Applying Unit Testing, TDD, BDD and Acceptance Testing [link](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1118901223.html)
[.](http://cdwanze.github.io/%E7%94%B5%E8%84%91/python/Testing%20Python.pdf)

## Videos

* [Outside-In TDD](https://www.youtube.com/watch?v=6zQAu23bKF8) Harry Percival, PyCon 2016

* [Докеризация веб приложения на Python](https://www.youtube.com/watch?v=if6Ly9ik9pE), Антон Егоров

* [Thinking about Concurrency](https://www.youtube.com/watch?v=Bv25Dwe84g0), Raymond Hettinger, Python core developer



## Tutorials
* [Разработка идеального pypi пакета с поддержкой разных версий python](https://habr.com/en/post/483512/) (Rus), 2020.

* [The Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/index.html) - an awesome collection of best practices with examples.

* [Set up vim for python](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/)

* [Set up emacs for python](https://realpython.com/blog/python/emacs-the-best-python-editor/)

* [Checklist to build great Celery async tasks](http://celerytaskschecklist.com/)

* [Getting Started with Django Rest Framework](http://www.projectforrest.com/path/70)

* [pythonsheets](https://www.pythonsheets.com/) - a colleciton of useful snippets

* [Command line arguments parsing with click](https://dbader.org/blog/mastering-click-advanced-python-command-line-apps)


## Asyncronous python

* Some historical overview [Asynchronous Python](https://hackernoon.com/asynchronous-python-45df84b82434)

* [ Video ] Couple of recipies: [Practical Python Async for Dummies](https://www.youtube.com/watch?v=5_K8GwZ_268)

* pytest addon for testing coroutines [pytest-asyncio](https://pypi.python.org/pypi/pytest-asyncio)

* Some more guidelines how to test coroutines: [Advanced asyncio testing](https://stefan.sofa-rockers.org/2016/03/10/advanced-asyncio-testing/)

## Performance

* [Grok the GIL: Write Fast and Thread-Safe Python](https://emptysqua.re/blog/grok-the-gil-fast-thread-safe-python/) - how GIL works

* [library for memory profiling](https://pypi.python.org/pypi/memory_profiler)

## Modules

[cloud storage module](https://pypi.python.org/pypi/cloudstorage) - supports AWS S3, Google cloud storage and local file system. Hopefully it has unified interface for all three of the backends.

[Apache libcloud](https://github.com/apache/libcloud/) -- anouther cloud file system API. more alive


## Testing, packaging, releasing

* [Packaging a python library](https://blog.ionelmc.ro/2014/05/25/python-packaging/), 25 May 2014 (updated 30 September 2019) by ionelmc. The article proposes a way to structure the code of your python module, describes how to write setup.py file, set up `tox`, `pytest` etc. Cookie cutter library for initialization of new projects: https://github.com/ionelmc/cookiecutter-pylibrary

* About processing of KeyboardInterrupt exception, INT signals and background processes. 
  [Capturing SIGINT using KeyboardInterrupt exception works in terminal, not in script](https://stackoverflow.com/questions/40775054/capturing-sigint-using-keyboardinterrupt-exception-works-in-terminal-not-in-scr/40785230#40785230)
  , stack overflow.
      
        # invocation from interactive shell
        $ python -c "import signal; print(signal.getsignal(signal.SIGINT))"
        <built-in function default_int_handler>
        
        # background job in interactive shell
        $ python -c "import signal; print(signal.getsignal(signal.SIGINT))" &
        <built-in function default_int_handler>
        
        # invocation in non interactive shell
        $ sh -c 'python -c "import signal; print(signal.getsignal(signal.SIGINT))"'
        <built-in function default_int_handler>
        
        # background job in non-interactive shell
        $ sh -c 'python -c "import signal; print(signal.getsignal(signal.SIGINT))" &'
        1

## Blogs

* [https://snarky.ca/](https://snarky.ca/) - Python core developer. Dev manager for the Python extension for VS Code.
