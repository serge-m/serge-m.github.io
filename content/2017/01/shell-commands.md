Title: Shell commands
Author: SergeM
Date: 2017-01-08 11:10:00
Slug: shell-commands
Tags: linux,useful,ubuntu


Some linux commands, probably for ubuntu/linux mint

Add user to a group
```
sudo usermod -aG group user
```


Remove user from a group
```
sudo gpasswd -d user group
```


Change shell for user `user` to bash
```
chsh -s /bin/bash user
```


Encode/decode binary file to ascii using command line 

[link](/encodedecode-binary-file-to-ascii.html)


Restart now:
```
shutdown -r 0
```

## SSH
generate key:
```
ssh-keygen
```

generate RSA key of length 4096 to file `my_key`
```
ssh-keygen -t rsa -b 4096 -C "your@e-mail.com" -f my_key
```

Generate md5 fingerprint of the key (works in newer ubuntu, 16):
```
ssh-keygen -lf ./my_key -E md5
```

## Vim
[vimCheatSheet](https://www.fprintf.net/vimCheatSheet.html)
[another vim cheat scheet](https://vim.rtorr.com/)
