---
Title: Useful console commands 
Author: SergeM
Date: 2017-06-09 12:15:00
Slug: useful-console-commands
aliases: [/useful-console-commands.html]
Tags: [ useful,console,linux,network,users, sed, find, regex, replace,]
---




Some linux commands that I'll probably need in the future


# User management

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


Disable user from login including ssh

    sudo usermod --expiredate 1 user1

Reenable the user:

    sudo usermod --expiredate "" user1



# Processes

Kill processes occupying a certain port:
```
fuser -k 8080/tcp
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


# Network

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


# Text 

## Replace text in a file using command line

replace regex in files using command line and `sed`:

    sed -i -E 's/source/destination/g' ./file.txt

all occurrences of `source` will be replaced with `destination` and the substitution will be done in-place. No backup!


More complex example:

    sed -i.back -E 's/^(\S+) 123 (\S+)$/\1 456 \2/g' ./file.txt

Here I replace 123 to 456 when it is between two other words in a string.  For example 

```
123some_word_without_spaces 123 must_match
123
aaa 123 multiple words - not matched
```

will become 

```
123some_word_without_spaces 456 must_match
123
aaa 123 multiple words - not matched
```

Also there will be a backup file with `.back` extension.


If your text contain slashes, you can use another delimiter:
```
xargs sed -i.original "s|text/to/find/|text/to/put|g" ./file.txt
```


## Text replacement recursively in many files

replacing all occurences of `source` with `destination` in files `*.txt`, inplace, with a backup.

    find . -name "*.txt" -exec sed -i.back -E 's/source/destination/g' {} \;


# Misc

Encode/decode binary file to ascii using command line 

[link](/encodedecode-binary-file-to-ascii.html)


Restart now:
```
shutdown -r 0
```

## Disk space

`df` - check free disk space

`baobab` - free disk space


# See also

* [1](/2013/10/ten-best-console-commands-rus.html) (in russian)
* [ssh cheat sheet](/2017-04-ssh-cheatsheet.html)
