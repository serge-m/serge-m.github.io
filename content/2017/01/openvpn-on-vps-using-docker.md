---
Title: OpenVPN server in cloud using docker
Author: SergeM
Date: 2017-01-07 07:10:00
Slug: openvpn-on-vps-using-docker
aliases: [/openvpn-on-vps-using-docker.html]
Tags: [ linux,docker,vpn,openvpn]
---




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
* https://m.habrahabr.ru/post/216295/


## OpenVPN setup notes

Download easyrsa for ca:
[github](https://github.com/OpenVPN/easy-rsa/releases)

You can specify a directory to store generated keys using `EASYRSA_PKI` environment variable. `$PWD/pki` is used by default. 

### Set up CA (certification authority)
It is better to use a separate computer to host CA.

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


#### On server
We have to initialize PKI (private key infrastructure) here as well, then we create a request to CA.
```
root@df73a69e45da:/easyrsa# ./easyrsa init-pki

init-pki complete; you may now create a CA or requests.
Your newly created PKI dir is: /server/pki
```

```
root@df73a69e45da:/easyrsa# ./easyrsa gen-req server nopass
Generating a 2048 bit RSA private key
.+++
......................................+++
writing new private key to '/server/pki/private/server.key.75fVPXwcOd'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Common Name (eg: your user, host, or server name) [server]:vpn-server

Keypair and certificate request completed. Your files are:
req: /server/pki/reqs/server.req
key: /server/pki/private/server.key

```

Copy `server.req` to CA.

#### On CA
Import:
```
root@8bb29470d5c0:/easyrsa# ./easyrsa import-req /ca/pki/import/server.req vpn-server

The request has been successfully imported with a short name of: vpn-server
You may now use this name to perform signing operations on this request.

```
Sign `vpn-server` with type `server`:
```
root@8bb29470d5c0:/easyrsa# ./easyrsa sign-req server vpn-server


You are about to sign the following certificate.
Please check over the details shown below for accuracy. Note that this request
has not been cryptographically verified. Please be sure it came from a trusted
source or that you have verified the request checksum with the sender.

Request subject, to be signed as a server certificate for 3650 days:

subject=
    commonName                = vpn-server


Type the word 'yes' to continue, or any other input to abort.
  Confirm request details: yes
Using configuration from ./openssl-easyrsa.cnf
Enter pass phrase for /ca/pki/private/ca.key:
Can't open /ca/pki/index.txt.attr for reading, No such file or directory
139728030523840:error:02001002:system library:fopen:No such file or directory:../crypto/bio/bss_file.c:74:fopen('/ca/pki/index.txt.attr','r')
139728030523840:error:2006D080:BIO routines:BIO_new_file:no such file:../crypto/bio/bss_file.c:81:
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
commonName            :ASN.1 12:'vpn-server'
Certificate is to be certified until Apr 11 22:52:57 2028 GMT (3650 days)

Write out database with 1 new entries
Data Base Updated

Certificate created at: /ca/pki/issued/vpn-server.crt
```

### Launcing OpenVPN server

#### Configuration
```
root@df73a69e45da:/easyrsa# ./easyrsa gen-dh
Generating DH parameters, 2048 bit long safe prime, generator 2
This is going to take a long time
.+...............................................................................................................................
...
......................................................................................................++*++*

DH parameters of size 2048 created at /server/pki/dh.pem

```

```
root@df73a69e45da:/server/pki# openvpn --genkey --secret ta.key
```

Create missing directories:
```
mkdir /etc/openvpn/ccd
mkdir -p /var/log/openvpn/
```

Create non-priviledged user `openvpn`:
```
adduser --system --no-create-home --home /nonexistent --disabled-login --group openvpn
```

Copy to `/etc/openvpn` the following files:
* from CA: 
  * `ca.crt`
  * `crl.pem`
  * `vpn-server.crt` 

* from server: 
  * `server.key` (private key),
  * `dh.pem`, 
  * `ta.key`


* `server.conf`

    <details>
    <summary>Sample content of server.conf for openvpn server</summary>
    
    <pre>
    port 1194
    proto udp
    dev tun

    user openvpn
    group openvpn

    persist-key
    persist-tun
    tls-server
    tls-timeout 120

    # to avoid warning
    # WARNING: this cipher's block size is less than 128 bit (64 bit).  Consider using a --cipher with a larger block size.
    # see also https://community.openvpn.net/openvpn/wiki/SWEET32
    cipher AES-128-CBC  

    cd /etc/openvpn/
    dh dh.pem
    ca ca.crt
    cert vpn-server.crt
    key vpn-server.key
    crl-verify crl.pem
    tls-auth ta.key 0

    server 10.15.0.0 255.255.255.0
    client-config-dir ccd
    client-to-client
    topology subnet
    max-clients 5
    push "dhcp-option DNS 10.15.0.1"
    route 10.15.0.0 255.255.255.0
    comp-lzo
    keepalive 10 120

    status /var/log/openvpn/openvpn-status.log 1
    status-version 3
    log-append /var/log/openvpn/openvpn-server.log
    verb 4
    mute 20
    </pre>
    </details>

To enable openvpn service to run all the server configurations from /etc/openvpn
1. edit `/etc/default/openvpn`, uncomment `AUTOSTART="all"`.

2. Reload:
```
sudo systemctl daemon-reload
```

#### Launching service
```
sudo service openvpn restart
```
After that you have to see logs in `/var/log/openvpn/`

If it doesn't start debug configuration with manual run:
```
openvpn /etc/openvpn/server.conf
```

### Launching client 
On the client we want to have a password for a key:
```
root@df73a69e45da:/easyrsa# ./easyrsa init-pki
root@df73a69e45da:/easyrsa# ./easyrsa gen-req client1 
```

Then copy request to CA, import.
```
$ ./easy-rsa sign-req <path-to-client1.req> client1
```

Signing request for a client:
```
$ ./easy-rsa sign-req client client1
```


Copy signed certificates and other necessary files to the client.

#### OpenVPN config for client
```
dev tun
proto udp
remote YOUR_SERVER_ADDRESS 1194
client
resolv-retry infinite

cipher AES-128-CBC

ca "ca.crt"
cert "client1.crt"
key "client1.key"
tls-auth "ta.key" 1

remote-cert-tls server
persist-key
persist-tun
comp-lzo
verb 4
#status /var/log/openvpn/openvpn-status.log 1
status-version 3
#log-append /var/log/openvpn/openvpn-client.log
```


## How to revoke a certificate (deactivate a user)
On CA:
```
$ ./easyrsa revoke <client-name>
$ ./easyrsa gen-crl
```
Then you have to upload new crl.pem to your server and restart the server.
