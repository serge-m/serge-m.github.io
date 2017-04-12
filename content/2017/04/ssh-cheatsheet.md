Title: SSH cheat sheet
Author: SergeM
Date: 2017-04-12 12:11:00
Slug: ssh-cheatsheet
Tags: ssh, keys, useful


## ssh don't scan all keys in .ssh directory
```
$ ssh -o IdentitiesOnly=yes -F /dev/null -i ~/path/to/some_id_rsa root@server.mydom.com
```

The options are as follows:

* `-o IdentitiesOnly=yes` - tells SSH to only use keys that are provided via the CLI and none from the `$HOME/.ssh` or via ssh-agent
* `-F /dev/null` - disables the use of `$HOME/.ssh/config`
* `-i ~/path/to/some_id_rsa` - the key that you explicitly want to use for the connection

[Source](https://superuser.com/a/1010861)
