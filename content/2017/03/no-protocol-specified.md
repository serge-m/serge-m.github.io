---
Title: '"No protocol specified" while running a program as another user'
Author: SergeM
Date: 2017-03-30 00:01:00
Slug: no-protocol-specified
aliases: [/no-protocol-specified.html]
Tags: [ linux]
---



Running some GUI application as another user:
```
user1@laptop:~$ su - user2
user2@laptop:~$ leafpad ~/somefile.txt
No protocol specified
```

The problem is `user2` doesn't have access to your screen.
Solution:
```
xhost +
```
Probably not the safest one.

Source: [thread](http://unix.stackexchange.com/a/108787)
