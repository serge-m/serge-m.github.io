Title: learning sqlite
Author: SergeM
Date: 2014-02-09 14:53:00
Slug: learning-sqlite
Tags: sql

# create table named t3 (id, value). id is integer. value is text
**sqlite> create table if not exists t3( id int , value varchar, primary key(id));**

# adding two "rows"
**sqlite> insert into t3 (id, value) values (1, 'a');**
**sqlite> insert into t3 (id, value) values (2, 'b');**

# display results
**sqlite> select * &nbsp;from t3;**
**1|a**
**2|b**

# update id=1 if exists, insert otherwise (id=1 exists)
**sqlite> insert or replace into t3 (id,value) values (1,'c' );**
**sqlite> select * &nbsp;from t3;**
**2|b**
**1|c**

# update id=1 if exists, insert otherwise (id=1 doesn't exist)
**sqlite> insert or replace into t3 (id,value) values (3,'e' );**
**sqlite> select * &nbsp;from t3;**
**2|b**
**1|c**
**3|e**
<div>
</div># update id=1 if exists, insert otherwise (id=1 doesn't exist)
**sqlite> insert or replace into t3 (id,value) values (3,'f' );**
**sqlite> select * &nbsp;from t3;**
**2|b**
**1|c**
**3|f**

</div>