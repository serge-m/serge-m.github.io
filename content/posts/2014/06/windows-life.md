---
Title: windows life
Author: SergeM
Date: 2014-06-05 23:00:00
Slug: windows-life
aliases: [/windows-life.html]
Tags: [ windows, command line, wifi, wi-fi, sharing]
---



`doskey /history > commands.log`- dump command line promt history to file

`some_command > output_file.txt 2>&1` -  Redirect stdout and stderr to the same file [src](http://stackoverflow.com/a/1420981)


## Share wifi from command line (probably obsolete in Win 8, 10)

```
netsh wlan set hostednetwork mode=allow ssid="NETWORK_NAME" key="NETWORK_PASSWORD" keyUsage=persistent
netsh wlan start hostednetwork
```
Then in the properties of the internet connection enable access. 

Then allow in firewall.
