Title: Python logging best practices
Author: SergeM
Date: 2015-04-21 23:05:00
Slug: python-logging
Tags: useful,python,links

## Best practices:

[Good logging practice in python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)

[Logging exceptions logging.exception](http://sergevideo.blogspot.com/2015/02/logging-exceptions-with-traceback-in.html)


## code for logging in ipython notebook (jupyter)
```python
import logging
import datetime
import sys, os

def prepare_logger(logger, level=logging.DEBUG, filename_template="logs/notebook_log_{}.txt"):
  def prepare_handler(handler):
    handler.setLevel(level)
    handler.setFormatter(formatter)
    return handler

  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

  path_file = filename_template.format(datetime.datetime.now().isoformat())
  path_dir = os.path.dirname(path_file)
  if not os.path.exists(path_dir):
    os.makedirs(path_dir)

  del logger.handlers[:]
  logger.handlers.append(prepare_handler(logging.FileHandler(path_file)))
  logger.handlers.append(prepare_handler(logging.StreamHandler(sys.stderr)))

  logger.setLevel(level=level)
  return logger

logger = logging.getLogger()
logger = prepare_logger(logger, level=logging.DEBUG)
```
