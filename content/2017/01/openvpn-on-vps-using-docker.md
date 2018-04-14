Title: OpenVPN server in cloud using docker
Author: SergeM
Date: 2017-01-07 07:10:00
Slug: openvpn-on-vps-using-docker
Tags: linux,docker,vpn,openvpn


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


### OpenVPN setup (in Russian)
* [Руководство по установке и настройке OpenVPN](https://habrahabr.ru/post/233971/) -- очень подробно. Комманды кратко - ниже.
* [PPTP vs L2TP vs OpenVPN vs SSTP](https://habrahabr.ru/post/191874/)


## OpenVPN setup notes

Download easyrsa for ca:
[github](https://github.com/OpenVPN/easy-rsa/releases)

Unpack and run:
```sh
root@a1aaf3e31e3a:/easyrsa# ./easyrsa init-pki

init-pki complete; you may now create a CA or requests.
Your newly created PKI dir is: /easyrsa/pki

```
build-ca:
```
root@a1aaf3e31e3a:/easyrsa# ./easyrsa build-ca
Generating a 2048 bit RSA private key
........................................................................................................................................................+++
.....................+++
writing new private key to '/easyrsa/pki/private/ca.key.jZ7M1ZpSAh'
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Common Name (eg: your user, host, or server name) [Easy-RSA CA]:test-ca

CA creation complete and you may now import and sign cert requests.
Your new CA certificate file for publishing is at:
/easyrsa/pki/ca.crt

```

Copy `ca.crt`.

```shell
root@8bb29470d5c0:/easyrsa# ./easyrsa gen-crl
Using configuration from ./openssl-easyrsa.cnf
Enter pass phrase for /ca/pki/private/ca.key:
Can't open /ca/pki/index.txt.attr for reading, No such file or directory
139922256114112:error:02001002:system library:fopen:No such file or directory:../crypto/bio/bss_file.c:74:fopen('/ca/pki/index.txt.attr','r')
139922256114112:error:2006D080:BIO routines:BIO_new_file:no such file:../crypto/bio/bss_file.c:81:

An updated CRL has been created.
CRL file: /ca/pki/crl.pem

```

Copy `crl.pem`


