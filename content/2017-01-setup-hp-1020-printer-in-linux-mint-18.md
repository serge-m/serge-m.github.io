Title: Set up HP 1020 printer in Linux Mint 18 / Ubuntu
Author: SergeM
Date: 2017-01-09 07:10:00
Slug: setup-hp-1020-printer-in-linux-mint-18
Tags: linux,useful, ubuntu, printer, hp, driver, 

# Using open source drivers

Follow the instruction from [http://foo2zjs.rkkda.com/](http://foo2zjs.rkkda.com/)

or use my clone on git [https://github.com/serge-m/foo2zjs.git](https://github.com/serge-m/foo2zjs.git):

* Clone the repo

      git clone https://github.com/serge-m/foo2zjs.git foo2zjs
      cd foo2zjs
        

* Compile:

      make

* Get extra files from the web, such as .ICM profiles for color correction,
and firmware.  Select the model number for your printer:
 
      ./getweb 1020	# Get HP LaserJet 1020 firmware file


* Install driver, foomatic XML files, and extra files:
    
      sudo make install
    
    
* Configure hotplug (USB; HP LJ 1000/1005/1018/1020).
 
  **Note**: In the original documentation this step is marked as optional, 
  however it is required for Ubuntu 18 + HP 1020 to work properly. 
      
      sudo make install-hotplug
    
  Do `sudo apt remove system-config-printer-udev` if the command above fails.

* Restart CUPS

      sudo systemctl restart cups
  
  
* Add a new printer in the system settings or CUPS and print.




# Why it is better to use open source drivers

HP is known for some fishy drivers that block your printer when non-original cartridges are used:

* [HP Has Added DRM to Its Ink Cartridges. Not Even Kidding (Updated)](https://www.wired.com/2016/09/hp-printer-drm/)

* [Does HP blocks 3rd party ink cartridges again on its printers (Jan. 2019)](https://borncity.com/win/2019/01/20/does-hp-blocks-3rd-party-ink-cartridges-again-on-its-printers-jan-2019/)

Worth trying to switch to open source.

The driver from foo2zjs.rkkda.com also looks pretty strange in terms of code distribution and quality. 
But that driver is recommended by [openprinting](https://www.openprinting.org/printer/HP/HP-LaserJet_1020). 
Let's hope somebody reviewed it :)

# Using proprietary drivers

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
