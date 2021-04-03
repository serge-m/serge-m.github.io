---
Title: Elasticsearch commands with curl
Author: SergeM
Date: 2017-02-10 23:11:00
Slug: elastic-search-cookbook
aliases: [/elastic-search-cookbook.html]
Tags: [ command line, elastic, search, elasticsearch, curl]
---



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

### List of all doc_types in a given index
```
curl -X GET localhost:9200/YOUR_INDEX/_mapping | jq ".YOUR_INDEX.mappings | to_entries | .[].key"
```

## Running elastic seach with a limited memory
```
#!/bin/sh                                                                                                                                                                                                                                     
ES_JAVA_OPTS="-Xms1g -Xmx1g" ./elasticsearch
```
