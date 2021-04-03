---
Title: Installing Android SDK (April 2015) in Linux Mint
Author: SergeM
Date: 2015-04-27 12:00:00
Slug: installing-android-sdk-april-2015-in
aliases: [/installing-android-sdk-april-2015-in.html]
Tags: [ ]
---



1a. Install Java SDK ([http://stackoverflow.com/a/17909346](http://stackoverflow.com/a/17909346))
```
sudo apt-get install openjdk-7-jdk
```

1b. Add JAVA_HOME variable to system environment 
```
sudo nano /etc/environment # or use any other editor
```

1c. Add line with path to your java location:
```
JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
```

Reboot/Logout

2a. Go to [https://developer.android.com/sdk/index.html](https://developer.android.com/sdk/index.html)
-> Download Android Studio

Unpack

go to `android-studio/bin`
run 
```
./studio.sh
```

2b. Go to Tools->Android->SDK Manager. Install required SDK version 

3. Install kvm
```
sudo apt-get install qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils
```

Enable Virtualization Technology in BIOS

Checking if it is ok run:
```
sudo kvm-ok
```
([http://askubuntu.com/questions/552064/how-can-kvm-be-located-by-android-studio-on-ubuntu-14-04-lts](http://askubuntu.com/questions/552064/how-can-kvm-be-located-by-android-studio-on-ubuntu-14-04-lts))

