---
Title: Add months to datetime in python
Author: SergeM
Date: 2017-07-20 07:07:00
Slug: add-months-to-datetime-in-python
aliases: [/add-months-to-datetime-in-python.html]
Tags: [ python, date, datetime, time]
---


```python
import datetime
from dateutil.relativedelta import relativedelta

your_datetime = datetime.datetime.now()
your_datetime + relativedelta(months=1) # adds one month
```

That function clips the overflowing day of the months:

```python
>>> datetime(2021, 1, 28) + relativedelta(months=1)
datetime.datetime(2021, 2, 28, 0, 0)
>>> datetime(2021, 1, 29) + relativedelta(months=1)
datetime.datetime(2021, 2, 28, 0, 0)
>>> datetime(2021, 1, 30) + relativedelta(months=1)
datetime.datetime(2021, 2, 28, 0, 0)
>>> datetime(2021, 1, 31) + relativedelta(months=1)
datetime.datetime(2021, 2, 28, 0, 0)
>>> datetime(2021, 1, 31) + relativedelta(months=2)
datetime.datetime(2021, 3, 31, 0, 0)
```

Intuitive solution doesn't work
```python
>>> your_datetime = datetime.datetime.now()
>>> your_datetime + datetime.timedelta(months=1)
Traceback (most recent call last):
File ““, line 1, in ?
TypeError: ‘months’ is an invalid keyword argument for this function
```

Probably "months" are not included in the standard library because of 
non-obvious semantic of the overflow.
