---
Title: Python logging best practices
Author: SergeM
Date: 2015-04-21 23:05:00
Slug: python-logging
aliases: [/python-logging.html]
Tags: [ useful,python,links,flask,logging,logger,logs,best practices]
---



## Simple logger setup for standalone scripts
When I write a simple script in python I want to have a nicely formatted log messages. 
Therefore I change the default format so that service information (time, logger name, error level) 
has a fixed length. It helps me visually parse important information (log messages) from the stream of logs.
It can be achieved by using fixed width modificators in format string:
```
%(asctime)s|%(name)-20.20s|%(levelname)-5.5s|%(message)s
```
More on logging format templates [here](https://docs.python.org/3.6/library/logging.html#logrecord-attributes).

Also I don't want 3rdparty libraries to pollute my logs. Lets say I want to see debug messages from my code,
but I don't need to see debug messages from `requests` library. 
How can I disable log messages from the Requests library?
```python
logging.basicConfig(level=logging.DEBUG)                 # enabling debug level for my code
logging.getLogger("requests").setLevel(logging.WARNING)  # disabling info and debug for requests
logging.getLogger("urllib3").setLevel(logging.WARNING)   # urllib3 is used in requests. disable too.
```


Full example:

```python
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s|%(name)-20.20s|%(levelname)-5.5s|%(message)s")
logging.getLogger("urllib3").setLevel(logging.WARNING)

logger.info("Info message")
logger.debug("Debug message")
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
