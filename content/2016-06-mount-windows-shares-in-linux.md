Title: Mount windows shares in linux
Author: SergeM
Date: 2016-06-19 12:37:00
Slug: mount-windows-shares-in-linux
Tags: useful, linux, samba, mount, network


Use sudo if needed
## Mount


    mkdir /mnt/share
    mount -t cifs //windows_machine_ip/share_name -o username=user,password=urPassword /mnt/share


To allow write access one has to specify owning user and group:

    sudo mount -t cifs //windows_machine_ip/share_name -o uid=$(id -u),gid=$(id -g),user=,password= /mnt/share

## Unmount


    umount /mnt/shares
