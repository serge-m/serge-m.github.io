Title: Add backslash before all escape characters in python 
Author: SergeM
Date: 2013-11-12 17:14:00
Slug: add-backslash-before-all-escape
Tags: python

Useful for using in regular expressions:

<blockquote class="tr_bq">import re
re.escape( str )</blockquote>
Python detects all escape characters that can be used by regex &nbsp;and add slash before them
[http://docs.python.org/2/library/re.html#re.escape](http://docs.python.org/2/library/re.html#re.escape)