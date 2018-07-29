Title: Spark in Docker with AWS credentials
Author: SergeM
Date: 2018-07-29 22:07:00
Slug: spark-in-docker-with-aws-credentials
Tags: spark,python, aws


# Running spark in docker container 

Setting up spark is tricky. Therefore it is useful to try out things locally before deploying to the cluster.

Docker is of a good help here.
There is a great docker image to play with spark locally.
[gettyimages/docker-spark](https://github.com/gettyimages/docker-spark/)

## Examples
Running `SparkPi` sample program (one of the examples from the docs of Spark):
```
docker run --rm -it -p 4040:4040 gettyimages/spark bin/run-example SparkPi 10
```

Running a small example with Pyspark:
```
echo -e "import pyspark\n\nprint(pyspark.SparkContext().parallelize(range(0, 10)).count())" > count.py
docker run --rm -it -p 4040:4040 -v $(pwd)/count.py:/count.py gettyimages/spark bin/spark-submit /count.py
```
Here we create a file with a python program outside of the docker. During `docker run` we map this file to the file inside the docker container with path `/count.py` and the we execute `bin/spark-submit` command that executes our code.

You can also run PySpark in interactive mode:
```
$ docker run --rm -it -p 4040:4040  gettyimages/spark bin/pyspark

Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170118] on linux
Type "help", "copyright", "credits" or "license" for more information.
2018-07-29 20:03:59 WARN  NativeCodeLoader:60 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.3.1
      /_/

Using Python version 3.5.3 (default, Jan 19 2017 14:11:04)
SparkSession available as 'spark'.
>>> sc
<SparkContext master=local[*] appName=PySparkShell>
>>> 

``` 

Now you can enter commands and evaluate your code in interactive mode. 


### Running a cluster with `docker-compose`
One can use docker-compose.yaml file from [https://github.com/gettyimages/docker-spark.git](https://github.com/gettyimages/docker-spark.git) to run a cluster locally.


docker-compose.yaml file looks like this:
```yaml
master:
  image: gettyimages/spark
  command: bin/spark-class org.apache.spark.deploy.master.Master -h master
  hostname: master
  environment:
    MASTER: spark://master:7077
    SPARK_CONF_DIR: /conf
    SPARK_PUBLIC_DNS: localhost
  expose:
    - 7001
    - 7002
    - 7003
    - 7004
    - 7005
    - 7006
    - 7077
    - 6066
  ports:
    - 4040:4040
    - 6066:6066
    - 7077:7077
    - 8080:8080
  volumes:
    - ./conf/master:/conf
    - ./data:/tmp/data

worker:
  image: gettyimages/spark
  command: bin/spark-class org.apache.spark.deploy.worker.Worker spark://master:7077
  hostname: worker
  environment:
    SPARK_CONF_DIR: /conf
    SPARK_WORKER_CORES: 2
    SPARK_WORKER_MEMORY: 1g
    SPARK_WORKER_PORT: 8881
    SPARK_WORKER_WEBUI_PORT: 8081
    SPARK_PUBLIC_DNS: localhost
  links:
    - master
  expose:
    - 7012
    - 7013
    - 7014
    - 7015
    - 7016
    - 8881
  ports:
    - 8081:8081
  volumes:
    - ./conf/worker:/conf
    - ./data:/tmp/data

```

Run it with command.
```
docker-compose up
```

It uses configs for master and worker nodes from `conf` directory.


## Accessing S3 from local Spark

I want to do experiments locally on spark but my data is stored in the cloud - AWS S3. If I deploy spark on EMR credentials are automatically passed to spark from AWS. But locally it is not the case. In the simple case one can use environment variables to pass AWS credentials:

```
docker run --rm -it -e "AWS_ACCESS_KEY_ID=YOURKEY" -e "AWS_SECRET_ACCESS_KEY=YOURSECRET" -p 4040:4040 gettyimages/spark bin/spark-shell
```

### Loading credentials from `~/.aws/credentials`
If you want to use AWS S3 credentials from `~/.aws/credentials` you have to do some configuration.
in the previous cluster example one have to specify credentials provider. Add the following line to `spark-defaults.conf`:
```
spark.hadoop.fs.s3a.aws.credentials.provider com.amazonaws.auth.profile.ProfileCredentialsProvider
```

Let's say we want to run some code like this:

```python
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .getOrCreate()

data = spark.read.parquet("s3a://your_bucket/serge-m-test/data.parquet")
data.show()
```
Now if you configure the rest properly and run the cluster you can access your s3 data from local spark/docker container.

Without the configuration we would get the following error:
```
Caused by: com.amazonaws.AmazonClientException: No AWS Credentials provided by BasicAWSCredentialsProvider EnvironmentVariableCredentialsProvider InstanceProfileCredentialsProvider : com.amazonaws.SdkClientException: Unable to load credentials from service endpoint
```
That basically means that spark has three credentials proveders: BasicAWSCredentialsProvider EnvironmentVariableCredentialsProvider InstanceProfileCredentialsProvider. But none of them worked.

* EnvironmentVariableCredentialsProvider - one that loads the credentials from environment variables
* InstanceProfileCredentialsProvider - one that works on AWS instances.
* BasicAWSCredentialsProvider - I don't know what it is.

What we need is ProfileCredentialsProvider. It reads the credentials from `~/.aws` directory.








