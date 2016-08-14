Title: Installing Android SDK (April 2015) in Linux Mint
Author: SergeM
Date: 2015-04-27 12:00:00
Slug: installing-android-sdk-april-2015-in
Tags: 

<div dir="ltr" style="text-align: left;" trbidi="on">1a. Install Java SDK ([http://stackoverflow.com/a/17909346](http://stackoverflow.com/a/17909346))
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">sudo apt-get install openjdk-7-jdk</span>

<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">1b. Add JAVA_HOME variable to system environment </span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">sudo nano /etc/environment&nbsp; # or use any other editor</span>

1c. Add line with path to your java location:
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64</span>

Reboot/Logout


2a. Go to&nbsp; 
[https://developer.android.com/sdk/index.html](https://developer.android.com/sdk/index.html)
-> Download Android Studio

Unpack

go to 
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">android-studio/bin</span>
run
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">./studio.sh</span>

<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">2b. Go to Tools->Android->SDK Manager. Install required SDK version </span>


<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">3. Install kvm </span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">sudo apt-get install qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils&nbsp;</span>

<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">Enable Virtualization Technology in BIOS</span>

<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">to check if it is ok run :</span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">sudo kvm-ok </span>
<span style="font-family: &quot;Courier New&quot;,Courier,monospace;">([http://askubuntu.com/questions/552064/how-can-kvm-be-located-by-android-studio-on-ubuntu-14-04-lts](http://askubuntu.com/questions/552064/how-can-kvm-be-located-by-android-studio-on-ubuntu-14-04-lts))</span>

</div>