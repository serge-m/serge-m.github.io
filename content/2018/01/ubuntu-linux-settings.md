Title: Ubuntu linux settings
Author: SergeM
Date: 2018-01-11 08:00
Slug: ubuntu-linux-settings
Tags: linux,useful


Some settings I find useful for a workstation

## Set `nemo` as default file manager 
```
xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search
```

now if you run `xdg-open ./` or press `Super+E` nemo starts.

[source](http://www.fandigital.com/2013/01/set-nemo-default-file-manager-ubuntu.html)

