---
Title: Python logging best practices
Author: SergeM
Date: 2015-04-21 23:05:00
Slug: python-logging
aliases: [/python-logging.html]
Tags: [ useful,python,flask,logging,logger,logs,best practices]
---

Python has a great built-in logging library. It allows to avoid a lot of boilerplate code and provides great features.
Here are some examples. Logging allows to set up a unified formatting for logs:

```
2023-10-03 12:57:22,377|classifier.py|  62|522130|MainThread|INFO|Classifying messages from ./messages.ndjson (images ./save_path)...
2023-10-03 12:57:22,378|classifier.py|  44|522130|MainThread|INFO|Start reading input messages from ./messages.ndjson
2023-10-03 12:57:22,378|classifier.py|  48|522130|MainThread|INFO|Loaded event {'id': 104162, 'date': '2023-09-27T07:12:08+00:00', 'entities': []}
2023-10-03 12:57:22,378|classifier.py|  48|522130|MainThread|INFO|Loaded event {'id': 58934, 'date': '2023-09-27T07:12:09+00:00', 'entities': [{'_': 'MessageEntityBold', 'offset': 92, 'length': 8}]}
2023-10-03 12:57:22,378|classifier.py|  48|522130|MainThread|INFO|Loaded event {'id': 82100, 'date': '2023-09-27T07:12:13+00:00', 'entities': [{'_': 'MessageEntityMentionName', 'offset': 8, 'length': 7, 'user_id': 5678410505}]}
2023-10-03 12:57:22,378|classifier.py|  54|522130|MainThread|INFO|Reading complete
```

Here you can easily see the time, file name and the line that produced the log message, also log level.

It provides a convenient way to log exceptions.

With 
```python
logger.exception(f"Decoding failed")
```
you get a nice stacktrace
```
2023-10-03 13:00:32,089|classifier.py|  49|522434|MainThread|ERRO|Decoding failed
Traceback (most recent call last):
  File "/home/classifier.py", line 47, in classify
    event = json.loads("{")
  File "/usr/lib/python3.8/json/__init__.py", line 357, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.8/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.8/json/decoder.py", line 353, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
Traceback (most recent call last):
  File "/home/classifier.py", line 66, in <module>
    classify()
  File "/home/classifier.py", line 50, in classify
    tmp = {k: event[k] for k in ['id', 'date', 'entities']}
  File "/home/classifier.py", line 50, in <dictcomp>
    tmp = {k: event[k] for k in ['id', 'date', 'entities']}
NameError: free variable 'event' referenced before assignment in enclosing scope
```

Also you can set up logging to a file, as well as to stderr.


## Simple logger setup for standalone scripts

I use logging even for small standalone scripts.  
I change the default format so that service information (time, module, error level, etc.) 
has a fixed length. It helps me visually parse important information (log messages) from the stream of logs.
It can be achieved by using fixed width modifiers in the format string:
```
logging.basicConfig(
    level=logging.INFO,
    format="{asctime}|{filename:6s}|{lineno:4d}|{process}|{threadName}|{levelname:4.4s}|{message}",
    style='{'
)
```
Here I use `str.format()` style.
Output line looks like this:
```
2023-10-03 13:00:32,089|classifier.py|  44|522434|MainThread|INFO|Start reading input messages from ./messages.ndjson
```

More on logging format templates [here](https://docs.python.org/3/library/logging.html#logrecord-attributes).

Global configuration of the logging can be set with `logging.basicConfig`. 
Usually I don't call  `logging.basicConfig` at the top level of a module. That would mess up logging configs in case 
another module imports it. I usually put `basicConfig` under `if __name__ == '__main__'` or in the main function of the 
script:


```commandline
import logging

# it's ok to create a logger as a global variable.
# It's a cheap operation. There is no need for singletons.
# You can even create new loggers in each function.
logger = logging.getLogger()


def f():
    """This is a reusable function that can be useful in other modules"""
    logger.info("running f()")


def main():
    logger.info("here we are in main")
    f()


if __name__ == '__main__':
    # I put global configuration under __main__.
    # If this module is imported then the caller is responsible for setting the logging parameters as they want.
    logging.basicConfig(level=logging.INFO,
                        format="{asctime}|{filename:6s}|{lineno:4d}|{process}|{threadName}|{levelname:4.4s}|{message}",
                        style='{')
    logger.info(f"Running as a script")
    main()
```

Output:
```text
2023-10-03 13:19:10,734|log_ex.py|  25|524770|MainThread|INFO|Running as a script
2023-10-03 13:19:10,734|log_ex.py|  15|524770|MainThread|INFO|here we are in main
2023-10-03 13:19:10,734|log_ex.py|  11|524770|MainThread|INFO|running f()
```


Also I don't want 3rdparty libraries to pollute my logs. Let's say I want to see debug messages from my code,
but I don't need to see debug messages from `requests` library. 
How can I disable log messages from the Requests library? Here is an example:

```python
logging.basicConfig(....)                                # enabling debug level for my code
logging.getLogger("requests").setLevel(logging.WARNING)  # disabling info and debug for requests
logging.getLogger("urllib3").setLevel(logging.WARNING)   # urllib3 is used in requests. disable too.
```


## Best practices

[Good logging practice in python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)

[Logging exceptions logging.exception](/logging-exceptions-with-traceback-in.html)

## Setup logging in Flask
In this <b>example</b> we replace default Flask logging with manually configured one. It includes logging to stdio and a file. Also it has extended formatting.


logging_config.py:
```
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "log.txt",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },
    "loggers": { # here you can add specific configuration for other libraries
        "werkzeug": {
            "level": "INFO", # change to "ERROR" if you want to see less logs from flask
            "handlers": ["console", "info_file_handler"],
            "propagate": False # required to avoid double logging
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "info_file_handler"]
    }
}
```

app.py:

```python
from flask import Flask, request, jsonify
import logging.config
from logging_config import logging_config


app = Flask(__name__)

@app.route('/')
def root():
    return "Hello, World!"


if __name__ == "__main__":
    logging.config.dictConfig(logging_config)
    app.run()
```


## Logging in ipython notebooks (jupyter)
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
