Title: Argparse recipies
Author: SergeM
Date: 2017-06-24 12:15:00
Slug: python-argparse-recipies
Tags: python,argparse


## How to include default values in '--help'

```python
parser = argparse.ArgumentParser(
    # ... other options ...
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
```
Output looks like this:
```python
  --scan-time [SCAN_TIME]
                        Wait SCAN-TIME seconds between status checks.
                        (default: 5)
```

Another tip:
add '%(default)' to the help parameter to control what is displayed.

```python
parser.add_argument("--type", default="toto", choices=["toto","titi"],
                              help = "type (default: %(default)s)")
```


[source](https://stackoverflow.com/questions/12151306/argparse-way-to-include-default-values-in-help)



