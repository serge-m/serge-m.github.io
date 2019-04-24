Title: Postgres cheatsheet
Author: SergeM
Date: 2019-04-24 08:30:00
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
### Managing tables

Create a new table or a temporary table
```sql
	
CREATE [TEMP] TABLE [IF NOT EXISTS] table_name(
   pk SERIAL PRIMARY KEY,
   c1 type(size) NOT NULL,
   c2 type(size) NULL,
   ...
);
```

Add a new column to a table:
```sql
ALTER TABLE table_name ADD COLUMN new_column_name TYPE;
```

Drop a column in a table:
```sql	
ALTER TABLE table_name DROP COLUMN column_name;
```

Rename a column:
```sql
ALTER TABLE table_name RENAME column_name TO new_column_name;
```

Set or remove a default value for a column:
```sql
ALTER TABLE table_name ALTER COLUMN [SET DEFAULT value | DROP DEFAULT]
```

Add a primary key to a table.
```sql
ALTER TABLE table_name ADD PRIMARY KEY (column,...);
```

Remove the primary key from a table.
```sql
ALTER TABLE table_name 
DROP CONSTRAINT primary_key_constraint_name;
```

Rename a table.
```sql	
ALTER TABLE table_name RENAME TO new_table_name;
```

## Credentials via environment variables
```bash
PGHOST=10.1.1.1 \
  PGUSER=user PGPASSWORD=password \
  psql my_db  -c "select * from my_table"
```

## See also
* [PostgreSQL Cheat Sheet](http://www.postgresqltutorial.com/postgresql-cheat-sheet/)
* [How to non interactively provide password for the PostgreSQL interactive terminal](https://blog.sleeplessbeastie.eu/2014/03/23/how-to-non-interactively-provide-password-for-the-postgresql-interactive-terminal/)


