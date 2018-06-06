Title: Comparison of click-based config parsers for python
Author: SergeM
Date: 2018-06-06 08:17:22
Slug: click-config-parsers
Tags: python,click,comparison


## Problem 
There is [click](click.pocoo.org/) module that allows you to create comman dline interfaces for your python scripts.
The advantages of click are
* nice syntax 
```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

```
* straightforward argument parsing strategy (in comparison to the standard [argparse](https://docs.python.org/3/library/argparse.html) )

Click doesn't support config files by default. There is a number of additional modules that implement this feature.
* [click-config](https://github.com/EverythingMe/click-config)
* [click-configfile](https://github.com/click-contrib/click-configfile)
* [click_config_file](https://github.com/phha/click_config_file)


## Comparison


| feature        | click-config       | click-configfile  | click_config_file
| ---------------------------- |:-------------| :-----------:| :------------:|
| Last commit in the repository| May 5, 2015  | Sep 24, 2017 | Jan 23, 2018  |
| Supports ini                 | +            |            + |              +|
| Supports json                | -            |            + |              +|
| Supports yaml                | +            |            + |              +|


### Syntax examples
#### click-config
```python
from __future__ import print_function
import click
import click_config


class config(object):
    class logger(object):
        level = 'INFO'

    class mysql(object):
        host = 'localhost'


@click.command()
@click_config.wrap(module=config, sections=('logger', 'mysql'))
def main():
    print('log level: {}, mysql host: {}'.format(
        config.logger.level,
        config.mysql.host
    ))


if __name__ == '__main__':
    main()
```
| a | b




