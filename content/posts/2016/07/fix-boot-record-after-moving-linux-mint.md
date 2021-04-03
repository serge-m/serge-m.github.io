---
Title: Fix boot record after moving linux mint partitions to another disk
Author: SergeM
Date: 2016-07-16 20:07:00
Slug: fix-boot-record-after-moving-linux-mint
aliases: [/fix-boot-record-after-moving-linux-mint.html]
Tags: [ Linux for dummies]
---



* Copying partition is straightforward. Made using gparted.

* Create bootable USB stick (Startup disk creator in Linux mint), boot from it.
Assume we have following partitions:
```
 boot /sdb1 (don't really know how it works)
 root /sdb2
 home /sdb3 
```

* Do

```
sudo mount /dev/sda2 /mnt

## if you have boot partition:
# sudo mount /dev/sda1 /mnt/boot

sudo grub-install --root-directory=/mnt /dev/sda
```

[Source of GRUB instructions](https://ru.wikibooks.org/wiki/Grub_2#.D0.92.D0.BE.D1.81.D1.81.D1.82.D0.B0.D0.BD.D0.BE.D0.B2.D0.BB.D0.B5.D0.BD.D0.B8.D0.B5_GRUB2_.D1.81_LiveCD._.D1.81.D0.BF.D0.BE.D1.81.D0.BE.D0.B1_2_.28.D0.B1.D0.B5.D0.B7_chroot.29)
