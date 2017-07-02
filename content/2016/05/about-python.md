Title: About python
Author: SergeM
Date: 2016-05-01 12:33:00
Slug: about-python
Tags: useful,python,links


## Production

#### Database helpers for sqlalchemy

Backend-agnostic database creation (CREATE IF NOT EXISTS):

```python
if not database_exists('postgres://postgres@localhost/name'):
    create_database('postgres://postgres@localhost/name')
```  

Possible with [SQLAlchemy-Utils](https://github.com/kvesteri/sqlalchemy-utils) library. See [docs](http://sqlalchemy-utils.readthedocs.io/en/latest/database_helpers.html)


#### Infrastructure with Python 
[http://dustinrcollins.com/infrastructure-with-python]([http://dustinrcollins.com/infrastructure-with-python])
-- list of tools for python development

## Language

Cheat Sheet: Writing Python 2-3 compatible code
[http://python-future.org/compatible_idioms.html](http://python-future.org/compatible_idioms.html)

Google Python Guidelines
[https://google.github.io/styleguide/pyguide.html](https://google.github.io/styleguide/pyguide.html)

Inheritance
[https://rhettinger.wordpress.com/2011/05/26/super-considered-super/](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)

## Other 

[Dismissing Python Garbage Collection at Instagram](https://engineering.instagram.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172)
