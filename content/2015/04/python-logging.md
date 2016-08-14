Title: Python logging 
Author: SergeM
Date: 2015-04-21 23:05:00
Slug: python-logging
Tags: useful,python,links

<div dir="ltr" style="text-align: left;" trbidi="on">
best practices:
[http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)



[Logging exceptions&nbsp;logging.exception ](http://sergevideo.blogspot.com/2015/02/logging-exceptions-with-traceback-in.html)


<h2 style="text-align: left;">code for logging in ipython notebook (jupyter)</h2>import logging
import datetime
import sys, os

def prepare_logger(logger, level=logging.DEBUG, filename_template="logs/notebook_log_{}.txt"):
&nbsp; &nbsp; def prepare_handler(handler):
&nbsp; &nbsp; &nbsp; &nbsp; handler.setLevel(level)
&nbsp; &nbsp; &nbsp; &nbsp; handler.setFormatter(formatter)
&nbsp; &nbsp; &nbsp; &nbsp; return handler
&nbsp; &nbsp;
&nbsp; &nbsp; formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
&nbsp; &nbsp;
&nbsp; &nbsp; path_file = filename_template.format(datetime.datetime.now().isoformat())
&nbsp; &nbsp;
&nbsp; &nbsp; path_dir = os.path.dirname(path_file)
&nbsp; &nbsp; if not os.path.exists(path_dir):
&nbsp; &nbsp; &nbsp; &nbsp; os.makedirs(path_dir)
&nbsp; &nbsp; &nbsp; 
&nbsp; &nbsp; del logger.handlers[:]
&nbsp; &nbsp; logger.handlers.append(prepare_handler(logging.FileHandler(path_file)))
&nbsp; &nbsp; logger.handlers.append(prepare_handler(logging.StreamHandler(sys.stderr)))
&nbsp; &nbsp;
&nbsp; &nbsp; logger.setLevel(level=level)
&nbsp; &nbsp; return logger

logger = logging.getLogger()
logger = prepare_logger(logger, level=logging.DEBUG)</div>