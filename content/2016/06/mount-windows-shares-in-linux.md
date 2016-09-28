Title: Mount windows shares in linux
Author: SergeM
Date: 2016-06-19 12:37:00
Slug: mount-windows-shares-in-linux
Tags: useful,linux


Use sudo if needed
## Mount
```
mkdir /mnt/share
mount -t cifs //windowsmachineip/sharename -o username=user,password=urPassword /mnt/share
```

## Unmount

```
umount /mnt/shares
```