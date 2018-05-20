Title: Set up HP 1020 printer in Linux Mint 18
Author: SergeM
Date: 2017-01-09 07:10:00
Slug: setup-hp-1020-printer-in-linux-mint-18
Tags: linux,useful

* Install `hplip-gui`:

```
sudo apt-get install hplip-gui
```

* install recommended proprietary driver from `HP Toolbox` GUI


[Thanks](https://ubuntu-mate.community/t/hp-3015-print-drivers-are-so-slow-at-printing/5580)


#### Another solution

```
sudo apt-get install hp-ppd hpijs hpijs-ppds hplip hplip-cups hplip-data hplip-dbg hplip-doc hplip-gui djtools
```

[source](https://askubuntu.com/questions/462329/hp-laserjet-1020-plus-printer-not-working-in-ubuntu-14-04/462335#462335)
