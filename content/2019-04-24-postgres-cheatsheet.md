Title: Postgres cheatsheet
Author: SergeM
Date: 2019-14-24 08:30:00
Slug: postgres-cheatsheet
Tags: postgres, postgresql, useful

## Credentials via environment variables
```bash
PGHOST=10.1.1.1 \
  PGUSER=user PGPASSWORD=password \
  psql my_db  -c "select * from my_table"
```


