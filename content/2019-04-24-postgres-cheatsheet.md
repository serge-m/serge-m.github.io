Title: Postgres cheatsheet
Author: SergeM
Date: 2019-14-24 08:30:00
Slug: postgres-cheatsheet
Tags: postgres, postgresql, useful

## Basics
Connect as user `postgres`:
```bash	
psql -U postgres
```

Connect to a specific database:
```
\c database_name;
```

Quit the psql:
```
\q
```

List all databases:
```	
\l
```

Lists all tables in the current database:
```	
\dt
```

List all users: 
```
\du
```

Create a new role `username` with a password:
```sql
CREATE ROLE username NOINHERIT LOGIN PASSWORD password;
```


## Credentials via environment variables
```bash
PGHOST=10.1.1.1 \
  PGUSER=user PGPASSWORD=password \
  psql my_db  -c "select * from my_table"
```


