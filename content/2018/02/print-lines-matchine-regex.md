Title: Select lines matching regular expression in python 
Author: SergeM
Date: 2018-02-26 23:14:00
Slug: print-lines-matching-regex
Tags: python,useful

Given a text file we want to create another file containing only those lines that match a certain regular expression using python3


```python
import re

with open("./in.txt", "r") as input_file, open("out.txt", "w") as output_file:
    for line in input_file:
        if re.match("(.*)import(.*)", line):
        print(line, file=output_file)
```

