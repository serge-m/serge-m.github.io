Title: Elasticsearch commands with curl
Author: SergeM
Date: 2017-02-10 23:11:00
Slug: elastic-search-cookbook
Tags: command line, elastic search

## Commands
### List indexes
```
curl -X GET localhost:9200/_cat/indices
```

### Delete index 
```
curl -X DELETE localhost:9200/YOUR_INDEX
```

### Delete all indices
```
curl -X GET localhost:9200/_all
```

## Running elastic seach with a limited memory
```
#!/bin/sh                                                                                                                                                                                                                                     
ES_JAVA_OPTS="-Xms1g -Xmx1g" ./elasticsearch
```
