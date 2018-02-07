Title: Workflow management with Apache Airflow
Author: SergeM
Date: 2018-02-06 08:23:00
Slug: airflow
Tags: python,airflow,links


Some useful resources about [Airflow](https://github.com/apache/incubator-airflow):

[ETL best practices with Airflow](https://gtoonstra.github.io/etl-with-airflow/index.html)

Series of articles about Airflow in production:
* [Part 1](https://medium.com/@dustinstansbury/beyond-cron-an-introduction-to-workflow-management-systems-19987afcdb5e) - about usecases and alternatives
* [Part 2](https://towardsdatascience.com/why-quizlet-chose-apache-airflow-for-executing-data-workflows-3f97d40e9571) - about alternatives (Luigi and Paitball)
* [Part 3](https://medium.com/@dustinstansbury/going-with-the-flow-part-part-iii-airflow-in-detail-a96efed52b1a) - key concepts
* [Part 4](https://medium.com/@dustinstansbury/how-quizlet-uses-apache-airflow-in-practice-a903cbb5626d) - deployment, issues


## More notes about production

About start_time: [Why isn’t my task getting scheduled?](https://airflow.apache.org/faq.html#why-isn-t-my-task-getting-scheduled)

One cannot specify `datetime.now()` as `start_date`. Instead one has to provide datetime object without timezone. Probably UTC time is required.
You can do something like this:
```python
from datetime import datetime, timedelta
import pytz

start_date_local = datetime(2018,1,1, 10,11, tzinfo=pytz.timezone('Europe/Minsk'))   # your time, date and time zone go here 
start_date_for_airflow = start_date_local.astimezone(pytz.utc).replace(tzinfo=None)  # we convert to UTC and remove timezone
```

## Running with LocalExecutor and Postgres from docker
We will run postgres in docker:
```
docker run -it -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -d postgres
```

Now we can specify in `airflow.cfg`:
```
sql_alchemy_conn = postgresql://postgres:postgres@localhost:5432/postgres
```

and 

```
executor = LocalExecutor

```

Then run 
```
airflow initdb
airflow scheduler
```

## How to specify AWS region for EmrCreateJobFlowOperator
There is no parameter in `EmrCreateJobFlowOperator` to specify  
AWS region where the cluster has to be deployed.

Internally `EmrCreateJobFlowOperator` uses `EmrHook` where `get_client_type('emr')` is called. 
`get_client_type` has a default paramater `region_name=None`. 
That means there is no way to set this parameter in code.


One has to configure it using airflow configurations.
Here we create connection `aws_my` with AWS region `eu-west-1`:

```
airflow connections -a --conn_id 'aws_my' --conn_uri 'aws:' --conn_extra '{"region_name": "eu-west-1"}'
```

Now we can use new connection for `EmrCreateJobFlowOperator` 
to **create Spark cluster on EMR**.

```
cluster_creator = EmrCreateJobFlowOperator(
    task_id='create_job_flow',
    job_flow_overrides={}, # your cluster configurations go here
    aws_conn_id='aws_my', # <---- this is important
    emr_conn_id='emr_default',
    dag=your_dag
) 
```

Done
