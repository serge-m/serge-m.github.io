Title: Useful console comands
Author: SergeM
Date: 2017-06-09 12:15:00
Slug: useful-console-commands
Tags: useful,console,linux,network


## Scan ip-s

Generally, nmap is useful to quickly scan networks.

To install nmap, enter
```
sudo apt-get install nmap
```
Once it is installed, enter
```
nmap -sn 192.168.1.0/24
```
This will show you which hosts responded to ping requests on the network between 192.168.1.0 and 192.168.1.255.

[Source](https://askubuntu.com/a/224567)
