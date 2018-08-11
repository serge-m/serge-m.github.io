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

## Set correct permissions for .ssh directory
You may get and error while connecting to ssh if you have wrond permissions for .ssh directory on server for a given user.

Error message on client while `ssh user-on-server@server`:
```
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Offering RSA public key: /home/user-on-client/.ssh/YOUR_KEY
debug1: Authentications that can continue: publickey
debug1: No more authentication methods to try.
Permission denied (publickey).
```

Error message on server:
```
Aug 11 10:55:21 comp sshd[3446]: Connection closed by 10.1.0.12 port 47794 [preauth]
```
And nothing more in logs.
The reason was that `.ssh` directory on the server had too strict permissions:
```
dr-------- 2 user-on-server user-on-server 4096 Aug 11 10:54 .ssh/
```
Read only is not enough. It must be `rwx`:
```
chmod 700 .ssh
```


## Configuring SSH server
Enable only ssh v2:
```
Protocol 2
```

Disable password authentification. Replace corresponding values in `/etc/ssh/sshd_config`:

```
ChallengeResponseAuthentication no
PasswordAuthentication no
```
[source](https://support.hostgator.com/articles/how-to-disable-password-authentication-for-ssh)

Restrict SSH access to only user accounts that should have it. For example, you may create a group called "sshlogin" and add the group name as the value associated with the `AllowGroups` variable located in the file `/etc/ssh/sshd_config`.
```
AllowGroups sshlogin
```
Then add your permitted SSH users to the group "sshlogin", and restart the SSH service.
```
sudo adduser username sshlogin
sudo systemctl restart sshd.service
```
[source](https://help.ubuntu.com/lts/serverguide/user-management.html.en#other-security-considerations)

restart sshd service
```
service sshd restart
```

### Add user for ssh tunnel only
```
useradd sshtunnel -m -d /home/sshtunnel -s /bin/rbash
passwd sshtunnel
```

in `.profile` in the home directory of the user (in our example it is /home/sshtunnel/):
```
PATH=""
```

Forbid changes:

```
chmod 555 /home/sshtunnel/
cd /home/sshtunnel/
chmod 444 .bash_logout .bashrc .profile
```

[source](http://www.ab-weblog.com/en/creating-a-restricted-ssh-user-for-ssh-tunneling-only/)


Restrictions in sshd config:
```
Match User that-restricted-guy
  AllowTcpForwarding yes
  X11Forwarding no
  AllowAgentForwarding no
  ForceCommand /bin/false

```
[source](https://unix.stackexchange.com/a/337445)

### How To Configure SSH Key-Based Authentication on a Linux Server 

See [How To Configure SSH Key-Based Authentication on a Linux Server](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server). Should I put public or private key to the server?


### Use ssh authentication by key instead of password

[Setup the SSH server to use keys for authentication](https://www.g-loaded.eu/2005/11/10/ssh-with-keys/)


## How to load ssh key without placing it to ~/.ssh
You must load a key to the ssh agent running in the background.

To start the ssh-agent in the background:

```bash
eval "$(ssh-agent -s)"
Agent pid 59566
```

You can add your SSH private key to the ssh-agent using `ssh-add` and full path to the key:
```bash
    ssh-add ~/path_to_your_private_key/id_rsa
```

Now you can for example do `git clone` from github using ssh key.

see also [1](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#adding-your-ssh-key-to-the-ssh-agent)

