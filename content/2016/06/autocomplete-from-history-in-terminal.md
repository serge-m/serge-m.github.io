Title: autocomplete from history in terminal (in linux mint)
Author: SergeM
Date: 2016-06-02 23:24:00
Slug: autocomplete-from-history-in-terminal
Tags: useful,linux,Linux for dummies

create a file ```.inputrc```
in your home directory and put there
```
"\e[A": history-search-backward
"\e[B": history-search-forward
set show-all-if-ambiguous on
set completion-ignore-case on
TAB: menu-complete
```

Restart your terminal.
Now you can autocomplete from history using Up and Down keys.
[Source](http://osxdaily.com/2013/04/24/improve-command-line-history-search/)
