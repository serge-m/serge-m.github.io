---
Title: Jupyter notebooks on EMR
Author: SergeM
Date: 2019-02-04 18:37:00
Slug: jupyter-notebooks-on-emr
aliases: [/jupyter-notebooks-on-emr.html]
Tags: [ spark, configuration, python, pyspark, emr, jupyter, ipython]
---





Explanatory data analysis requires interactive code execution. In case of spark and emr it is very convenient to run the code from jupyter notebooks on a remote cluster. EMR allows installing jupyter on the spark master. In order to do that configure `"Applications"` field for the emr cluster to contain also jupyter hub. For example:

```
"Applications": [
            {
                "Name": "Ganglia",
                "Version": "3.7.2"
            },
            {
                "Name": "Spark",
                "Version": "2.4.0"
            },
            {
                "Name": "Zeppelin",
                "Version": "0.8.0"
            },
            {
                "Name": "JupyterHub",
                "Version": "0.9.4"
            }
        ],


``` 

Set `KeepJobFlowAliveWhenNoSteps: true` and set up all the required python libraries using bootstrap scripts.

After cluster is created and bootstrapped you can get an address of the master in the aws console. Create a ssh tunnel to the port 9443 on the master. it is a port of jupyterhub:

```
export HOST=<public address of your master> 
ssh -i ~/.ssh/your_private_key.pem -L 9443:$HOST:9443 hadoop@$HOST
```

Now when you connect to your local 9443 port it is redirected to the master's 9443 port.

Open the browser an connect to [https://localhost:9443/hub/login](https://localhost:9443/hub/login). HTTPS and the endpoint is important!

[Default](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-user-access.html) user name is `jovyan` and the password is `jupyter`. Use with care.

Enjoy!


## Troubleshooting

Long running pyspark kernel is terminated after approximately 1 hour with the error:
```
An error was encountered:
Invalid status code '404' from http://ip-123-123-123-123.eu-west-1.compute.internal:8998/sessions/1 with error payload: "Session '1' not found."
```

To fix it add the following to your emr  cluster  `Configurations`:
```
[{'classification': 'livy-conf','Properties': {'livy.server.session.timeout':'5h'}}]
```

[source](https://stackoverflow.com/questions/54220381/how-to-set-livy-server-session-timeout-on-emr-cluster-boostrap)


## See also
* [PySpark SQL Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PySpark_SQL_Cheat_Sheet_Python.pdf) (pdf)
