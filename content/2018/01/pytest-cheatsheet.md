Title: Pytest cheatsheet
Author: SergeM
Date: 2018-01-02 22:50
Slug: pytest-cheatsheer
Tags: pytest, python, testing, useful


Pytest is a powerful tool for testing in python. Here are some notes about hands-on experience.

## Running tests in pytest with/without a specified mark

Execute  
```
pytest -m "integration"
```
if you want to run only tests that have "pytest.mark.integration" annotation.


Similarly you can run only tests that don't are not marked.
```
pytest m "not your_mark"
```
That command will test everything that is not marked as "your_mark".


