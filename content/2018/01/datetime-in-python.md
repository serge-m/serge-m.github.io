Title: Datetime in Python
Author: SergeM
Date: 2018-01-17 07:07:00
Slug: datetime-in-python
Tags: python,datetime,calendar,calendar week,date


## Conversion from calendar week to date
Sometimes one has to convert a date written as year, calendar week (CW), and day of week to an actual date with month and date.
The behaviour in the begin/end of a year may be not straightforward.
For example according to ISO 8601 monday date of the CW 1 year 2019 is 31 January 2018.
As far as I can see there is no standard function for conversion in python.


I use the following hacky code:

```python
def year_cw_day_to_date(year: int, calendar_week: int, day_of_week: int):
    """
    year: integer number, e.g. 1986
    calendar_week: integer number, from 1 to 53
    day_of_week: integer starting from 1, so that 1 is Monday, 2 is Tuesday, ...,  7 is Sunday

    >>> year_cw_day_to_date(2019, 1, 1)
    datetime.date(2018, 12, 31)

    >>> year_cw_day_to_date(2019, 1, 7)
    datetime.date(2019, 1, 6)

    >>> year_cw_day_to_date(2018, 52, 7)
    datetime.date(2018, 12, 30)

    >>> year_cw_day_to_date(2018, 53, 2)
    datetime.date(2019, 1, 1)

    >>> year_cw_day_to_date(2018, 53, 0)
    Traceback (most recent call last):
    ...
    ValueError: day_of_week must be in range from 1 to 7
    """

    if day_of_week not in range(1, 8):
        raise ValueError("day_of_week must be in range from 1 to 7")
    string_representation = f"{year}-{calendar_week}-{day_of_week}"
    return datetime.datetime.strptime(string_representation, "%G-%V-%u").date()
```

It prints the week-based date to a string and then parses it using `%V` and `%u` format from python 3 ([docs](https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior))
Therefore you don't need to implement ISO logic of dates calculation. Hopefully such a funciton apppear in standard library.

Python 2 doesn't have these `%V` and `%u` implemented. `:(`

## See also
[How to add months to datetime object in python](/add-months-to-datetime-in-python.html)
[datetime module in python 3](https://docs.python.org/3.6/library/datetime.html#module-datetime)