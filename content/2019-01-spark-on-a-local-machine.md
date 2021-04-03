---
Title: Spark on a local machine
Author: SergeM
Date: 2019-01-30 08:30:00
Slug: spark-on-a-local-machine
aliases: [/spark-on-a-local-machine.html]
Tags: [ spark, configuration]
---




## How to install spark locally

Considering spark without hadoop built-in.

* Download [hadoop](https://mirror.checkdomain.de/apache/hadoop/common/hadoop-3.1.1/hadoop-3.1.1.tar.gz)
unpack to `/opt/hadoop/`
* Download [spark without hadoop](https://archive.apache.org/dist/spark/spark-2.3.2/spark-2.3.2-bin-without-hadoop.tgz), unpack to `/opt/spark`
* Install java. Set JAVA_HOVE environment variable. For example: `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64`
* create environment variables required for spark to run. One can put those in `.bashrc`
```
export HADOOP_HOME=/opt/hadoop
export SPARK_DIST_CLASSPATH=$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*
```

Now you can run pyspark for example:
```
$ /opt/spark/bin/pyspark 
Python 2.7.12 (default, Nov 12 2018, 14:36:49) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/spark/jars/slf4j-log4j12-1.7.16.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
2019-01-31 08:36:02 WARN  Utils:66 - ....
2019-01-31 08:36:02 WARN  Utils:66 - Set SPARK_LOCAL_IP if you need to bind to another address
2019-01-31 08:36:03 WARN  NativeCodeLoader:60 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
2019-01-31 08:36:04 WARN  Utils:66 - Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.3.2
      /_/

Using Python version 2.7.12 (default, Nov 12 2018 14:36:49)
SparkSession available as 'spark'.
>>> exit()
```

## Running pyspark in jupyter notebooks locally
To open interactive pyspark session in jupyter notebooks do this:
```
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
/opt/spark/bin/pyspark 
```

Here jupyter server running locally connects to the spark running locally.  

## Troubleshooting
if you get 
```
/opt/spark/bin$ ./pyspark
Python 2.7.12 (default, Nov 12 2018, 14:36:49) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Error: A JNI error has occurred, please check your installation and try again
Exception in thread "main" java.lang.NoClassDefFoundError: org/slf4j/Logger
	at java.lang.Class.getDeclaredMethods0(Native Method)
	at java.lang.Class.privateGetDeclaredMethods(Class.java:2701)
	at java.lang.Class.privateGetMethodRecursive(Class.java:3048)
	at java.lang.Class.getMethod0(Class.java:3018)
	at java.lang.Class.getMethod(Class.java:1784)
	at sun.launcher.LauncherHelper.validateMainClass(LauncherHelper.java:544)
	at sun.launcher.LauncherHelper.checkAndLoadMain(LauncherHelper.java:526)
Caused by: java.lang.ClassNotFoundException: org.slf4j.Logger
	at java.net.URLClassLoader.findClass(URLClassLoader.java:382)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:349)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	... 7 more
Traceback (most recent call last):
  File "/opt/spark/python/pyspark/shell.py", line 38, in <module>
    SparkContext._ensure_initialized()
  File "/opt/spark/python/pyspark/context.py", line 300, in _ensure_initialized
    SparkContext._gateway = gateway or launch_gateway(conf)
  File "/opt/spark/python/pyspark/java_gateway.py", line 93, in launch_gateway
    raise Exception("Java gateway process exited before sending its port number")
Exception: Java gateway process exited before sending its port number
```
that means that you haven't set `SPARK_DIST_CLASSPATH` (spark cannot find slf4j which is needed for logging)



## See also
* [Get Started with PySpark and Jupyter Notebook in 3 Minutes](https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f)
* [How to set up PySpark for your Jupyter notebook](https://medium.freecodecamp.org/how-to-set-up-pyspark-for-your-jupyter-notebook-7399dd3cb389)
* [Downloading spark and getting started with python notebooks (jupyter) locally on a single computer](https://medium.com/explore-artificial-intelligence/downloading-spark-and-getting-started-with-python-notebooks-jupyter-locally-on-a-single-computer-98a76236f8c1)
* [Exception: Java gateway process exited before sending the driver its port number](https://github.com/jupyter/notebook/issues/743)
* [How to access s3a:// files from Apache Spark?](https://stackoverflow.com/questions/30385981/how-to-access-s3a-files-from-apache-spark)
