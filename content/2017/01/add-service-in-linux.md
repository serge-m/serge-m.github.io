Title: Add service in ubuntu 
Author: SergeM
Date: 2017-01-08 07:10:00
Slug: add-service-in-linux
Tags: linux,useful


Create a file for service `your-service`
```
touch /etc/systemd/system/your-service.service 
```

Let's assume you want to run docker container there. Put following text in the file:

```
[Unit]                                                                                                                                                                                                                                        
Description=YourService                                                                                                                                                                                                                           
After=docker.service                                                                                                                                                                                                                          
Requires=docker.service                                                                                                                                                                                                                       
                                                                                                                                                                                                                                              
[Service]                                                                                                                                                                                                                                     
TimeoutStartSec=0                                                                                                                                                                                                                             
Restart=always                                                                                                                                                                                                                                
ExecStartPre=-/usr/bin/docker stop %n                                                                                                                                                                                                         
ExecStartPre=-/usr/bin/docker rm %n                                                                                                                                                                                                           
ExecStart=/usr/bin/docker run -d -p 8080:8080/tcp --name %n your_docker_image
                                                                                                                                                                                                                                              
[Install]                                                                                                                                                                                                                                     
WantedBy=multi-user.target
```

Here we first stop and delete the docker container. If it doesn't exist we continue (there is a "-" in before the command).

Run
```
systemctl enable your-service
```

See also: 

[[1]](https://askubuntu.com/questions/886024/auto-start-or-enable-service-on-boot-up-permanently-ubuntu-16-04-lts)

[[2] How To Use Systemctl to Manage Systemd Services and Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)

[[3] How to set up proper start/stop services](https://blog.frd.mn/how-to-set-up-proper-startstop-services-ubuntu-debian-mac-windows/)
