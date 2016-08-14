Title: Fix boot record after moving linux mint partitions to another disk
Author: SergeM
Date: 2016-07-16 20:07:00
Slug: fix-boot-record-after-moving-linux-mint
Tags: Linux for dummies

<div dir="ltr" style="text-align: left;" trbidi="on">1. Copying partition is straightforward. Made using gparted.

2. Create bootable USB stick (Startup disk creator in Linux mint), boot from it.
Assume we have following partitions:
<ul style="text-align: left;"><li>boot /sdb1 (don't really know how it works)</li><li>root /sdb2 </li><li>home /sdb3 </li></ul>3. Do

    ::::
    sudo mount /dev/sda2 /mnt

    ::::
    &nbsp;

    ::::
    ## if you have boot partition:

    ::::
    # sudo mount /dev/sda1 /mnt/boot

    ::::
    
    

    ::::
    sudo grub-install --root-directory<span class="o">=</span>/mnt /dev/sda




[Source of GRUB instructions](https://ru.wikibooks.org/wiki/Grub_2#.D0.92.D0.BE.D1.81.D1.81.D1.82.D0.B0.D0.BD.D0.BE.D0.B2.D0.BB.D0.B5.D0.BD.D0.B8.D0.B5_GRUB2_.D1.81_LiveCD._.D1.81.D0.BF.D0.BE.D1.81.D0.BE.D0.B1_2_.28.D0.B1.D0.B5.D0.B7_chroot.29)</div>