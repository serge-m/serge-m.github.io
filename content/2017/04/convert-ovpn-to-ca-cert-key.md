Title: Convert ovpn config file to .ca, .crt, .key
Author: SergeM
Date: 2017-04-02 12:11:00
Slug: convert-ovpn-to-ca-cert-key
Tags: openvpn

How you can take an OpenVPN .ovpn config file and extract the certificates/keys 

* Copy from between `<ca>` tags into `ca.crt`, remove `<ca>` tags from original file.
* Copy from between `<cert>` tags into `client.crt`, remove `<cert>` tags.
* Copy from between `<key>` tags into client.key, remove `<key>` tags.
* Copy from between `<tls-auth>` tags into `ta.key`, remove `<tls-auth>` tags.
* Remove the line "`key-direction 1`"
* Above `"# -----BEGIN RSA SIGNATURE-----"` insert the following lines.
```
    ca ca.crt
    cert client.crt
    key client.key
    tls-auth ta.key 1
```
Done.


Source: [here](https://gist.github.com/Morley93/9697578)
