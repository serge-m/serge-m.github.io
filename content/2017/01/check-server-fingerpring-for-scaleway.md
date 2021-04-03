---
Title: Check server fingerprint for scaleway
Author: SergeM
Date: 2017-01-04 07:10:00
Slug: check-server-fingerpring-for-scaleway
aliases: [/check-server-fingerpring-for-scaleway.html]
Tags: [ ]
---



Run
```
curl -H 'X-Auth-Token: <YOUR_TOKEN>' https://cp-ams1.scaleway.com/servers/<YOUR_SERVER_ID>/user_data/ssh-host-fingerprints
```
compare output with results of 
ssh <YOUR_USER>@<YOUR_SERVER_IP>

`cp-ams1` needs to be changed if you use non amsterdam based server.

Sources:

1. [community.online.net](https://community.online.net/t/no-way-to-verify-ssh-key-fingerprint-exposes-all-servers-to-mitm-attacks/816/5) 
  
2. [Scaleway API documentation](https://developer.scaleway.com/) 
