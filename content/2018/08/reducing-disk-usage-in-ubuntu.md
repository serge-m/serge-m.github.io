Title: Reducing disk usage in Ubuntu  
Author: SergeM
Date: 2018-08-16 00:10:00
Slug: disk-usage-ubuntu
Tags: links,disk usage,linux, ubuntu


Here are some recipies to make ubuntu installed on USB drive to work faster.

[[1]](http://stevehanov.ca/blog/index.php?id=48)

[[2]](https://www.cyrius.com/debian/nslu2/linux-on-flash/)


## reducing swapping 
Add these lines to /etc/sysctl.conf, and reboot.
```
vm.swappiness = 0
vm.dirty_background_ratio = 20
vm.dirty_expire_centisecs = 0
vm.dirty_ratio = 80
vm.dirty_writeback_centisecs = 0
```


## More caching while writting on disk

Add `noatime,commit=120`,... to `/etc/fstab` entries for `/` and `/home` 


