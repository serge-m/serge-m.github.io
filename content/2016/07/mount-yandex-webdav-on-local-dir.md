Title: Mount yandex webdav on local dir
Author: SergeM
Date: 2016-07-16 13:45:00
Slug: mount-yandex-webdav-on-local-dir
Tags: useful,linux

```
    apt-get install davfs2
    mkdir /mnt/yandex.disk
    mount -t davfs https://webdav.yandex.ru /mnt/yandex.disk/
    
    # check: 
    df -h /mnt/yandex.disk/ 
```