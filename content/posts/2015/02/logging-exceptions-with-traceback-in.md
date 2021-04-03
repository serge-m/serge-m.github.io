---
Title: Logging exceptions with traceback in python 
Author: SergeM
Date: 2015-02-02 23:00:00
Slug: logging-exceptions-with-traceback-in
aliases: [/logging-exceptions-with-traceback-in.html]
Tags: [ ]
---



When using logging module one often need to print traceback along with error message.

Solution is:
```python
logger.error('error message', exc_info=True) # for adding traceback to log
```

Equivalent :
```python 
logger.exception('message')
```
