Title: Flask and SQLAlchemy explained
Author: SergeM
Date: 2018-01-11 22:02
Slug: flask-and-sqlalchemy-explained
Tags: flask,sqlalchemy,sql,python



Awesome explanation of SQLAlchemy with examples and comparison to Django by [Armin Ronacher](http://lucumr.pocoo.org/about/): 
[SQLAlchemy and You](http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/)

## Flask-SQLAlchemy module
[Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org) is an extension for Flask that adds support for SQLAlchemy to your application.

How to add SQLAlchemy to Flask application:
```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configuration of the DB is read from flask configuration storage
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# here we define db object that keeps track of sql interactions
db = SQLAlchemy(app) 
```

Now we are ready to define tables and objects using predefined `db.Model` class:
```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
```


Now in your endpoint handlers you do:

```
from your_application import db

def post_users_endpoint():
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
```


### How to access multiple databases from one Flask application

There is a special mechanism for maintaining connections to multiple databases in your flask app: [binds](http://flask-sqlalchemy.pocoo.org/2.3/binds/)

To use it you have to adjust configurations like this:
```
SQLALCHEMY_DATABASE_URI = 'postgres://localhost/main'
SQLALCHEMY_BINDS = {
    'users':        'mysqldb://localhost/users',
    'appmeta':      'sqlite:////path/to/appmeta.db'
}
```
then you can specify binding key in your ORM-classes:
```
class User(db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
```


## Flask tutorials
Nice series of flask tutorials: [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins).

Including [Oauth authentication In Flask](https://blog.miguelgrinberg.com/post/oauth-authentication-with-flask).


## See also 
* SQLAlchemy cheat sheet

[Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)

* [about abstractions in SQLalchemy](https://habr.com/company/qrator/blog/430818/) - in Russian
