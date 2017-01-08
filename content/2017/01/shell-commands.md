Title: Shell commands
Author: SergeM
Date: 2017-01-08 11:10:00
Slug: shell-commands
Tags: linux,useful,ubuntu


Some linux commands, probably for ubuntu/linux mint

Add user to a group
```
sudo usermod -aG group user
```


Remove user from a group
```
sudo gpasswd -d user group
```


Change shell for user `user` to bash
```
chsh -s /bin/bash user
```


Encode/decode binary file to ascii using command line 

[link](/encodedecode-binary-file-to-ascii.html)
