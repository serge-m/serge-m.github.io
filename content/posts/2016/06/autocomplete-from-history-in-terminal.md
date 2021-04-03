---
Title: Autocomplete from the history in terminal
Author: SergeM
Date: 2016-06-02 23:24:00
Slug: autocomplete-from-history-in-terminal
aliases: [/autocomplete-from-history-in-terminal.html]
Tags: [ useful,linux,Linux for dummies,terminal]
---



create a file ```.inputrc```
in your home directory and put there

```
"\e[A": history-search-backward
"\e[B": history-search-forward
set show-all-if-ambiguous on
set completion-ignore-case on

# display possible completions using different colors to indicate their file types
set colored-stats On

TAB: menu-complete

```

Restart your terminal.
Now you can autocomplete from history using Up and Down keys.

[Source](http://osxdaily.com/2013/04/24/improve-command-line-history-search/)
