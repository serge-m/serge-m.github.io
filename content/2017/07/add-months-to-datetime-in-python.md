---
Title: Add months to datetime in python
Author: SergeM
Date: 2017-07-20 07:07:00
Slug: add-months-to-datetime-in-python
aliases: [/add-months-to-datetime-in-python.html]
Tags: [ python]
---




```python
import datetime
from dateutil.relativedelta import relativedelta

your_datetime = datetime.datetime.now()
your_datetime + relativedelta(months=1) # adds one month
```

Intuitive solution doesn't work
```python
>>> your_datetime = datetime.datetime.now()
>>> your_datetime + datetime.timedelta(months=1)
Traceback (most recent call last):
File ““, line 1, in ?
TypeError: ‘months’ is an invalid keyword argument for this function
```

