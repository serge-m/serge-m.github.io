Title: SSH cheat sheet
Author: SergeM
Date: 2017-04-12 12:11:00
Slug: ssh-cheatsheet
Tags: ssh, keys, useful


## SSH don't scan all keys in .ssh directory
```
$ ssh -o IdentitiesOnly=yes -F /dev/null -i ~/path/to/some_id_rsa root@server.mydom.com
```

The options are as follows:

* `-o IdentitiesOnly=yes` - tells SSH to only use keys that are provided via the CLI and none from the `$HOME/.ssh` or via ssh-agent
* `-F /dev/null` - disables the use of `$HOME/.ssh/config`
* `-i ~/path/to/some_id_rsa` - the key that you explicitly want to use for the connection

[Source](https://superuser.com/a/1010861)


## How To Configure SSH Key-Based Authentication on a Linux Server 

See [How To Configure SSH Key-Based Authentication on a Linux Server](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server). Should I put public or private key to the server?


## Use ssh authentication by key instead of password

[Setup the SSH server to use keys for authentication](https://www.g-loaded.eu/2005/11/10/ssh-with-keys/)
