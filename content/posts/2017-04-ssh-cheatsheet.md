---
Title: SSH cheat sheet
Author: SergeM
Date: 2017-04-12 12:11:00
Slug: ssh-cheatsheet
aliases: [/ssh-cheatsheet.html]
Tags: [ ssh, keys, useful, tunnel, security, linux]
---




## Create more secure ssh keys
Create a key using elliptic curve cryptography (more secure): 

    ssh-keygen -a 100 -t ed25519

generate RSA key of length 4096 to file `my_key`
   
    ssh-keygen -t rsa -b 4096 -C "your@e-mail.com" -f my_key

Generate md5 fingerprint of the key (works in newer ubuntu, 16):

    ssh-keygen -lf ./my_key -E md5


see also: [Upgrade Your SSH Key to Ed25519](https://medium.com/risan/upgrade-your-ssh-key-to-ed25519-c6e8d60d3c54)


## How to prevent SSH from scanning all the keys in .ssh directory
    
    $ ssh -o IdentitiesOnly=yes -F /dev/null -i ~/path/to/some_id_rsa root@server.mydom.com

The options are as follows:

* `-o IdentitiesOnly=yes` - tells SSH to only use keys that are provided via the CLI and none from the `$HOME/.ssh` or via ssh-agent
* `-F /dev/null` - disables the use of `$HOME/.ssh/config`
* `-i ~/path/to/some_id_rsa` - the key that you explicitly want to use for the connection

[Source](https://superuser.com/a/1010861)

## No strict server checking 
To disable confirmation about unknown server fingerprints add this to command line:
`-o StrictHostKeyChecking=no`

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

For authorized_keys file use the following premissions:
```
chmod 644 ~/.ssh/authorized_keys 
```

## Port forwarding

### Remote port forwarding 

Take all the connections to `0.0.0.0:8080` of the remote machine (`example.com`) 
and forward it to `localhost:80` on the local machine:
 
    ssh -R 0.0.0.0:8080:localhost:80 -N root@example.com
    
The command above creates a general IPv4-only bind, 
which means that the port is accessible on **all** interfaces via IPv4.

This version binds to all interfaces individually:
 
    ssh -R \*:8080:localhost:80 -N root@example.com
    
    
Another option: 

    ssh -R "[::]:8080:localhost:80" -N root@example.com

The third version is probably technically equivalent to the first, 
but again it creates only a single bind to `::`, which means that the port is accessible via IPv6 
natively and via IPv4 through IPv4-mapped IPv6 addresses (doesn't work on Windows, OpenBSD). 
 (You need the quotes because `[::]` could be interpreted as a glob otherwise.)


Full list of specifications for the remote forwarding.
```
     -R [bind_address:]port:host:hostport
     -R [bind_address:]port:local_socket
     -R remote_socket:host:hostport
     -R remote_socket:local_socket
```
Specifies that connections to the given TCP port or Unix socket on the remote (server) 
host are to be forwarded to the given host and port, or Unix socket, on the local side.  

By default, TCP listening sockets on the server will be bound to the loopback interface only.  This may be overridden by specifying a bind_address.  An empty bind_address, or the address ‘*’, indicates that the remote socket should listen on all interfaces.  Specifying a remote bind_address will only succeed if the server's `GatewayPorts` option is enabled (see sshd_config(5)).

If the port argument is ‘0’, the listen port will be dynamically allocated on the server 
and reported to the client at run time.  
When used together with `-O` forward the allocated port will be printed to the standard output.


When bind_address is omitted (as in your example), the port is bound on the loopback interface only. 

Note that if you use OpenSSH sshd server, the server's `GatewayPorts` 
option needs to be enabled (set to `yes` or `clientspecified`) for arbitrary interface to work 
(check file `/etc/ssh/sshd_config` on the **server**). 
Otherwise (default value for this option is `no`), 
the server will always force the port to be bound on the loopback interface only.

See also: [1](https://superuser.com/a/591963), [2](https://man.openbsd.org/ssh)

#### Local port forwarding

    ssh -L localhost:1234:localhost:5678 user@1.1.1.1
    
With this command  
* all the connections to the `localhost:1234` of the host machine
* are forwarded to `localhost:5678` at the server (`1.1.1.1`).


#### Port forwarding between two machines that don't have external ip's using a server

On machine 1:
  
    ssh -L localhost:10002:localhost:10001 user@1.1.1.1
    
On machine 2:

    ssh -R localhost:10001:localhost:10000 user@1.1.1.1

Now when I access `localhost:10002` on machine 1 the request is redirected to `localhost:10000` of machine 2.
The connection goes through port `10001` of host `1.1.1.1`

#### config for multiple port forwarding
How to forward  multiple ports with one command. It is possible with a config file.

Imagine we want to forward local ports 22, 9999, 9998 to the corresponding ports of machine `192.168.1.2` using ssh on machine `192.168.1.1`. 
In order to do that add the following to `~/.ssh/config`:

    Host all-port-forwards
      Hostname 192.168.1.1
      User user
      LocalForward 22 192.168.1.2:22
      LocalForward 9999 192.168.1.2:9999
      LocalForward 9998 192.168.1.2:9998
      
Now you can run a single command:

    ssh all-port-forwards


### Port forwarding on system startup with retry

We want our port to be forwarded on the startup of the system. Also we want to deal with failures: retry on disconnect etc.

#### Initial version - it doesn't work
In my experience the approach didn't really work. The built-in mechanisms of systemctl didn't allow me to achieve robust restarting.

Create a file `/etc/systemd/system/tunnelssh.service`:

```
[Unit]
Description=tunnel ssh to server

[Service]
User=YOUR_LOCAL_USER
ExecStart=/usr/bin/ssh -NT -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -i PATH_TO_YOUR_PRIVATE_KEY -R REMOTE_SERVER_INTERFACE:PORT_ON_REMOTE_SERVER:localhost:LOCAL_PORT user_at_remote_server@REMOTE_SERVER

StartLimitIntervalSec=10
StartLimitBurst=1
RestartSec=3
Restart=Always

[Install]
WantedBy=multi-user.target

```
Then enable and start
```
systemctl enable tunnelssh.service
systemctl start tunnelssh.service
systemctl status tunnelssh.service
```

Unfortunately it doesn't work on startup. It says that the unit entered failed state and doesn't restart.
The problem is that 
1. our service may start before network connection is up. You may add `After=network.target` or `After=network-online.target` as suggested [here](https://gist.github.com/drmalex07/c0f9304deea566842490#gistcomment-2087688) but it doesn't save you from the next issue.
2. our server can be down for some time
3. retry mechanism of systemd is somehow broken. I couldn't make it work with configuration of burst intervals from [here](https://selivan.github.io/2017/12/30/systemd-serice-always-restart.html), [here](https://serverfault.com/questions/736624/systemd-service-automatic-restart-after-startlimitinterval) and [here](https://unix.stackexchange.com/a/289756). And it [seems](https://github.com/google/cloud-print-connector/issues/140) I am not the only [one](https://unix.stackexchange.com/a/216254).

(in the spirit of this [solution](https://gist.github.com/drmalex07/c0f9304deea566842490))


#### Second version
So we have to implement retry on our own without systemd. Fortunately there is a tool `autossh`. See for example [[1]](https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-autossh/) or [[2]](https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-autossh/)

    [Unit]
    Description=tunnel ssh to server
    # After=network.target network-online.target multi-user.target
    # Requires=network-online.target
    
    [Service]
    User=YOUR_LOCAL_USER
    Environment=AUTOSSH_GATETIME=0
    ExecStart=/usr/bin/autossh -M 0 -NT -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -i PATH_TO_YOUR_PRIVATE_KEY -R REMOTE_SERVER_INTERFACE:PORT_ON_REMOTE_SERVER:localhost:LOCAL_PORT user_at_remote_server@REMOTE_SERVER
    
    RestartSec=5
    Restart=Always
    
    [Install]
    WantedBy=multi-user.target

## Configuring SSH server

Enable only ssh v2:
```
Protocol 2
```

Disable password authentication. Replace corresponding values in `/etc/ssh/sshd_config`:

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


### Restarting ssh service
after each change in sshd_config you have to restart ssh service to enable the changes
```bash
## Ubuntu/debian user ##
sudo service ssh restart
# only for systemd based Ubuntu/Debian 8.x+ users #
sudo systemctl restart ssh
 
#### RHEL/CentOS/Fedora Linux user type ####
sudo service sshd restart
# only for systemd based RHEL/CentOS v7+ users #
sudo systemctl restart sshd
```

### Add user for ssh tunnel only

    useradd sshtunnel -m -d /home/sshtunnel -s /bin/rbash
    passwd sshtunnel


in `.profile` in the home directory of the user (in our example it is /home/sshtunnel/):

    PATH=""


Forbid changes:

    chmod 555 /home/sshtunnel/
    cd /home/sshtunnel/
    chmod 444 .bash_logout .bashrc .profile


[source](http://www.ab-weblog.com/en/creating-a-restricted-ssh-user-for-ssh-tunneling-only/)


Restrictions in sshd config:

    Match User that-restricted-guy
      AllowTcpForwarding yes
      X11Forwarding no
      AllowAgentForwarding no
      ForceCommand /bin/false

[source](https://unix.stackexchange.com/a/337445)

### Restricting root user

For security reason you should always block access to root user and group on a Linux or Unix-like systems. 

First, make sure at least one user is allowed to use ‘su -‘ or ‘sudo’ command on the server. 

Then add to `/etc/ssh/sshd_config`
```
DenyUsers root
DenyGroups root
```

set PermitRootLogin  to `no`:
```
PermitRootLogin no
```
Save the file and restart the ssh service.

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


## mount remote file system using ssh

```
sudo apt-get install sshfs
sudo mkdir /mnt/droplet
sudo sshfs -o allow_other,IdentityFile=~/.ssh/id_rsa root@xxx.xxx.xxx.xxx:/ /mnt/droplet
```

With identity files only:
```
sudo sshfs -o allow_other,IdentitiesOnly=yes,IdentityFile=~/.ssh/id_rsa user@192.168.0.1:/remote/path /mnt/local/path/
```

[Source](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)


## Specific settings for a website
I have a private key with a custom name in `~/.ssh/` add the .pub is uploaded to github. When I try to clone my repo, git returns 
```
Cloning into 'repo'...
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Probably git reads only keys with standard names (e.g. id_rsa). 
To make it pick up your custome key you can create a config file 
`~/.ssh/config`:
 
```
Host github.com
  IdentityFile ~/.ssh/your_custom_private_key
  IdentitiesOnly yes
```

More [here](https://stackoverflow.com/questions/4565700/how-to-specify-the-private-ssh-key-to-use-when-executing-shell-command-on-git/11251797#11251797)

### See also
* [Top 20 OpenSSH Server Best Security Practices](https://www.cyberciti.biz/tips/linux-unix-bsd-openssh-server-best-practices.html)



## SOCKS proxy

How to run socks proxy. It's a bit easier than using VPN because it doesn't require sudo to launch.
Also it doesn't require to install anything on the server except openssh server. 

    ssh -D 1337 -q -C -N user@your_server.ip

`-D` defines the port on the local machine,
 
`-q` is quiet mode,

`-C` compresses, 

`-N` causes remote commands not to be executed, just straight port forwarding.

Then one can set up a socks proxy in the settings of the browser.


[src](https://medium.com/@therockspush/building-a-quick-and-easy-ssh-socks-proxy-3a440f5d35a7)


## Faster retry after disconnecting

In order to make recovery faster after network issues use options 
`-o "ServerAliveInterval 2" -o "ServerAliveCountMax 2"`.

Alternatively one can add the following to `~/.ssh/config`:

    Host *
      ServerAliveInterval 2
      ServerAliveCountMax 2


## See also

* [sshd_config - SSH Server Configuration](https://www.ssh.com/ssh/sshd_config/) - nice guidelines
