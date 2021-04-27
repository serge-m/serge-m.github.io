---
Title: Add service in ubuntu 
Author: SergeM
Date: 2017-01-08 07:10:00
Slug: add-service-in-linux
aliases: [/add-service-in-linux.html]
Tags: [ linux,useful]
---




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

## Commands 
```
# prints the status
systemctl status your-service.service  

# prepares the service, required before "start", 
# also reloads the config if you changed the definition file  
systemctl enable levels_tracker.service 

# start service
systemctl start levels_tracker.service 

# stop service
systemctl stop levels_tracker.service 
```



## Recipes

### Specify working directory

```
[Service]
WorkingDirectory=/home/pi
```

### Running python script from virtual environment 
Just specify python interpreter from the environment:
```
ExecStart=<absolute path to your environment>/bin/python file_to_run.py
```

### Environment variables
You can set environment variables that are used for your process
```
[Service]
Environment=VARIABLE=value
```
Now you can use it in the `ExecStart` command for example:
```
ExecStart=<absolute path to your environment>/bin/python file_to_run.py ${VARIABLE}
```
### How to stdout of python-based service in syslog

Python buffers stdout. Therefore even if you have enable redirection of stdout to the syslog:
```
StandardOutput=syslog
```

You may see nothing in the logs. You should set environment variable for python `PYTHONUNBUFFERED` to see the results immediately:
```
#in your service file add to [Service] section:
Environment="PYTHONUNBUFFERED=1"
```

source: [[here]](https://unix.stackexchange.com/questions/164987/output-of-a-python-script-running-as-unit-is-out-of-order-while-shells-seems-unn)

Probably better approach when you are allowed to install modules: https://medium.com/@trstringer/logging-to-systemd-in-python-45150662440a



## See also: 

[[1]](https://askubuntu.com/questions/886024/auto-start-or-enable-service-on-boot-up-permanently-ubuntu-16-04-lts)

[[2] How To Use Systemctl to Manage Systemd Services and Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)

[[3] How to set up proper start/stop services](https://blog.frd.mn/how-to-set-up-proper-startstop-services-ubuntu-debian-mac-windows/)
