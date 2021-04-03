---
Title: Correct way of running long tasks in Flask
Author: SergeM
Date: 2017-01-23 23:11:00
Slug: correct-way-of-running-long-tasks-in-flask
aliases: [/correct-way-of-running-long-tasks-in-flask.html]
Tags: [ python, flask, celery]
---




Key to the answer is Celery.

Good post: [Using Celery With Flask](https://blog.miguelgrinberg.com/post/using-celery-with-flask)

[Sources](https://github.com/miguelgrinberg/flask-celery-example)

See also: [Making an asynchronous task in Flask](http://stackoverflow.com/questions/31866796/making-an-asynchronous-task-in-flask)


Sharing memory and using multiprocessing along with gunicorn seem to be wrong solutions.
