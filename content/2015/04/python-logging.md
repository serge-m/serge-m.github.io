Title: Python logging best practices
Author: SergeM
Date: 2015-04-21 23:05:00
Slug: python-logging
Tags: useful,python,links,flask

## Best practices:

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
