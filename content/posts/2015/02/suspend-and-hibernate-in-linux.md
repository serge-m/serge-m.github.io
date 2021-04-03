---
Title: Suspend and hibernate in Linux
Author: SergeM
Date: 2015-02-04 14:04:00
Slug: suspend-and-hibernate-in-linux
aliases: [/suspend-and-hibernate-in-linux.html]
Tags: [ useful,Linux for dummies]
---





After installing ubuntu 14.04 I found hibernation was disabled. It was deleted from system menu at all. 
http://ubuntuhandbook.org/index.php/2014/04/enable-hibernate-ubuntu-14-04/


Only Suspend option was there.
Suspend didn't work either. Computer couldn't wake up. It actually woke up, but stayed freezed displaying wallpaper.
Some googling and testing with other hibernation modules (tuxonice), 
swap settings gave no result.
I decided to install mint Linux as it has hibernation option by default.
In mint Linux the situation was the same except I hadn't to enable hibernate option myself.
The solution was in using proprietary Nvidia drivers instead of open source.
In mint Linux there is a convenient tool called driver manager http://www.linuxmint.com/rel_olivia_whatsnew.php
There I switched to a version provided by nvidia. After installation I reboot Computer and suspend/hibernation worked.


Ubuntu developers say they disabled hibernation by default because too many users face issues with hibernation. &nbsp;I suppose now I know the cause of these issues : bad Nvidia support in open source drivers. :)
