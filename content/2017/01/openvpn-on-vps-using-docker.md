Title: OpenVPN server in cloud using docker
Author: SergeM
Date: 2017-01-07 07:10:00
Slug: openvpn-on-vps-using-docker
Tags: linux,docker,vpn


links:

[How To Run OpenVPN in a Docker Container on Ubuntu 14.04 ](https://www.digitalocean.com/community/tutorials/how-to-run-openvpn-in-a-docker-container-on-ubuntu-14-04)

[OpenVPN for Docker](https://github.com/kylemanna/docker-openvpn)


## Connection via OPenVPN is slow for https
Try the following [advice](https://forums.openvpn.net/viewtopic.php?t=21857)
The udp connection is perfect with these parameters (in client config):
```
mssfix 1200
tun-mtu 1200
```

## DNS doesn't work through VPN
Symptoms: Openvpn connects, you can ping web sites by IP address, but you cannot ping them by name (like ping `google.com`)

[Solution](https://bugs.launchpad.net/ubuntu/+source/openvpn/+bug/1211110):

This is a bug that's fixed in upstream NetworkManager. That said, the various GUI tools which write the NetworkManager config files haven't been updated to ensure that DNS leaks are prevented when using vpn connections.

To prevent system dns from appearing and being used in `/etc/resolv.conf` when using a VPN, edit your vpn configuration (i.e. the file in /etc/NetworkManager/system-connections/<vpn name>) so it's something like this:

```
[ipv4]
dns=<vpn dns server ip address>;
ignore-auto-dns=true
method=auto
dns-priority=-1
```

the negative dns-priority means only this dns server will be used.
Then reload the config file:
```
sudo nmcli c reload <vpn name>
```

and toggle the vpn.

/etc/resolv.conf should now only include the one dns ip address defined in the config file.



### VPS servers to try
* https://billing.virmach.com/cart.php?gid=1
* https://www.vultr.com/pricing/

