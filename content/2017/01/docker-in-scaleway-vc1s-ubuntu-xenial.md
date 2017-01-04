Title: Docker in Scaleway's vc1s Ubuntu Xenial
Author: SergeM
Date: 2017-01-05 07:10:00
Slug: docker-in-scaleway-vc1s-ubuntu-xenial
Tags: 


In ubuntu 16.04 image installed on VC1S server I was unable to install docker.
It hangs/fails on installation or on any significant docker command like `docker ps`

The error I got was 
```
Job for docker.service failed because the control process exited with error code. See "systemctl status docker.service" and "journalctl -xe" for details
```
and
```
level=error msg="devmapper: Unable to delete device: devicemapper: Can't set task name /dev/mapper/docker
```


I switched to "docker" image where docker is preinstalled
