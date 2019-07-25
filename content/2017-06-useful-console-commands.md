Title: Useful console comands 
Author: SergeM
Date: 2017-06-09 12:15:00
Slug: useful-console-commands
Tags: useful,console,linux,network


Some linux commands that I'll probably need in the future


Kill processes occupying a certain port:
```
fuser -k 8080/tcp
``` 


Add user to a group
```
sudo usermod -aG group user
```
or 
```
sudo adduser <user> <group>
```


Delete user
```
userdel user
```

Delete the user’s home directory and mail spool:
```
userdel -r user
```

Remove user from a group
```
sudo gpasswd -d user group
```

list all users:
```
$ getent passwd
```

list all groups:
```
$ getent group
```

list all groups of the current user:
```
$ groups
```
list all groups of a user:
```
$ groups <user>
```



Change shell for user `user` to bash
```
chsh -s /bin/bash user
```


Encode/decode binary file to ascii using command line 

[link](/encodedecode-binary-file-to-ascii.html)


Restart now:
```
shutdown -r 0
```

## SSH
generate key:
```
ssh-keygen
```

generate RSA key of length 4096 to file `my_key`
```
ssh-keygen -t rsa -b 4096 -C "your@e-mail.com" -f my_key
```

Generate md5 fingerprint of the key (works in newer ubuntu, 16):
```
ssh-keygen -lf ./my_key -E md5
```

## Detach process
Sometimes I need to detach from a process running on a remote machine so that it continues running after I logout.


Using the Job Control of bash to send the process into the background:

* `Ctrl+Z` to stop (pause) the program and get back to the shell.
* `bg` to run it in the background.
* `disown -h [job-spec]` where `[job-spec]` is the job number (like %1 for the first running job; find about your number with the jobs command) so that the job isn't killed when the terminal closes.

[source](https://stackoverflow.com/a/625436)

Unrfortunately disown is specific to bash and not available in all shells.

Certain flavours of Unix (e.g. AIX and Solaris) have an option on the nohup command itself which can be applied to a running process:

`nohup -p pid`


The first of the commands below starts the program `abcd` in the background in such a way that the subsequent logout does not stop it.

```bash
$ nohup abcd &
$ exit
```

[wiki](https://en.wikipedia.org/wiki/Nohup)


## Scan IP range

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

## Replace text in files

```
find . -type f | xargs sed -i "s/text_to_find/text_to_put/g"
```
To keep original files with `.original` extension:
```
find . -type f | xargs sed -i.original "s/text_to_find/text_to_put/g"
```

If your text contain slashes, you should use another delimiter:
```
find . -type f | xargs sed -i.original "s|text/to/find/|text/to/put|g"
```

## Disk space

`df` - check free disk space

`baobab` - free disk space

## See also

* [1](/2013/10/ten-best-console-commands-rus.html) (in russian)

