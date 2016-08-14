Title: Mount windows shares in linux
Author: SergeM
Date: 2016-06-19 12:37:00
Slug: mount-windows-shares-in-linux
Tags: useful,linux

<div dir="ltr" style="text-align: left;" trbidi="on">

Use sudo if needed
<h2 style="text-align: left;">Mount</h2>mkdir /mnt/share
mount -t cifs //windowsmachineip/sharename -o username=user,password=urPassword /mnt/share
<h2 style="text-align: left;">Unmount</h2>umount /mnt/shares</div>