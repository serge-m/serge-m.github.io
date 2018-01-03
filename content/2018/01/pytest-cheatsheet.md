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
if you want to run only tests that have "@pytest.mark.integration" annotation.


Similarly you can run only tests that don't are not marked.
```
pytest -m "not your_mark"
```
That command will test everything that is not marked as "your_mark".

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
[Optional] Add a status image to your `readme.md` file:
```
[![Build Status](https://travis-ci.org/YOUR_GITHUB_NAME/YOUR_REPO_NAME.svg?branch=master)](https://travis-ci.org/YOUR_GITHUB_NAME/YOUR_REPO_NAME)
```




