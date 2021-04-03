---
Title: Pytest cheatsheet
Author: "SergeM"
Date: "2018-01-02 22:50:00"
Slug: pytest-cheatsheet
aliases: [/pytest-cheatsheet.html]
Tags: [pytest,python,testing,useful,travisci,ci]
---

Pytest is a powerful tool for testing in python. Here are some notes about hands-on experience.




## Running tests in pytest with/without a specified mark

Execute  
```
pytest -m "integration"
```
if you want to run only tests that have "@pytest.mark.integration" annotation.


Similarly you can run only tests that don't are not marked.
```
pytest -m "not your_mark"
```
That command will test everything that is not marked as "your_mark".


## How to verify exception message using pytest
One can use context manager `pytest.raises` to check if the exception has correct text inside. You have to check excinfo.value in the end.
```python
def test_exception_has_correct_message():
    with pytest.raises(Exception) as excinfo:
        your_function()

    assert 'Failed to establish a new connection' in str(excinfo.value)
```

`excinfo` here stays defined also outside of the context scope.



## Running pytests on Travis CI

Register on TravisCI.

Enable your repo in the settings of Travis CI. 
URL: https://travis-ci.org/profile/YOUR_GITHUB_NAME

Put configuration file for travis into the root of your github repository:

```
language: python
python:
  - "3.5"
branches:
  only:
  - master
install:
- echo "installing" # not used for the example
script:
- |
  pip install -r requirements.txt
  python -m pytest -m "not integration" # running everything except integration tests
env:
global:
```

[Optional] Add a status image like this
[![Build Status](https://travis-ci.org/serge-m/blog-sources.svg?branch=master)](https://travis-ci.org/serge-m/blog-sources)
to your `readme.md` file:

```
[![Build Status](https://travis-ci.org/YOUR_GITHUB_NAME/YOUR_REPO_NAME.svg?branch=master)](https://travis-ci.org/YOUR_GITHUB_NAME/YOUR_REPO_NAME)
```




## Running pytest with code coverage reports
One have to install `pytest-cov` module first. Then
```
py.test --cov=<DIRECTORY_WITH_SOURCES> --cov-report html:htmlcov --cov-report term:skip-covered <DIRECTORY_WITH_TESTS>
```
This command runs tests with code coverage report. Reports are printed in console (`--cov-report term:skip-covered`) and as html files in `htmlcov` directory (`--cov-report html:htmlcov`).
To view html report now you can run for example `google-chrome ./htmlcov/index.html`.


### Restriction on code coverage
You can set up pytest-cov so that is will fail if coverage is below a certain level. This can be done with `--cov-fail-under` parameter. It will give you a restiction for total coverage in a project.
I find useful to have code coverage threshold for each module independently.
So that if you forgot to test one of 10000 files it is still a failure. unfortunately it seems that separate `fail-under` per file is not implemented.



## Pytest configuration files
To avoid writing all the parameters in command line every time one can use configuration files for pytest and coverage reports.


### .coveragerc

```
# in this file one can exclude some file from coverage report. Probably you want to exclude tests themselves
[run]
omit = <DIRECTORY_WITH_TESTS> 
```


### pytest.ini 

```
[pytest]
addopts =
    --cov-config=.coveragerc --cov=<DIRECTORY_WITH_SOURCES> --cov-report xml:coverage.xml --cov-report term:skip-covered
testpaths = <DIRECTORY_WITH_TESTS>
```

## Alternative tests automation solutions

[Tox](https://tox.readthedocs.io/en/latest/) -- tool for tests automation. Creates configurable virtual environments and run tests there. Can handle myltiple python versions.
Doesn't work without creating virtualenvs, which is a pitty if you want to run tests in your global environment or inside the docker for example.

 


## See also
* [Run docker as pytest fixture](/run-docker-as-pytest-fixture.html)
* [Testing json responses in Flask REST apps with pytest ](/testing-json-responses-in-Flask-REST-apps-with-pytest.html)
* [More about pytest configuration files](https://docs.pytest.org/en/latest/customize.html#adding-default-options)





