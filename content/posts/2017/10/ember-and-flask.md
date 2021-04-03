---
Title: Sample project with Ember and Flask
Author: SergeM
Date: 2017-10-25 23:24:00
Slug: sample-ember-and-flask
aliases: [/sample-ember-and-flask.html]
Tags: [ python,flask,ember]
---




I want to use EmberJS with Flask application. Flask will provide an API.
Ember frontend will consume and display data from the Flask backend.

Let's say we want our fronted to display a list of users of the system.
We will have a main page and `users` page in our frontend. On the `users` page
the client will see a list of users that we get from backend.


Source code is here:
[ember_flask_example](https://github.com/serge-m/ember_flask_example)



```python
# file backend/api.py
from flask import Flask
from flask import jsonify
from flask import request, send_from_directory

app = Flask(__name__, static_url_path='')

# this function returns an object for one user
def u(user_id):
    return {
        "type": "users",                    # It has to have type
        "id": user_id,                      # And some unique identifier
        "attributes": {                     # Here goes actual payload.
            "info": "data" + str(user_id),  # the only data we have for each user is "info" field
        },
    }

# routes for individual entities
@app.route('/api/users/<user_id>')
def users_by_id(user_id):
    return jsonify({"data": u(user_id)})

# default route.
# flask has to serve a file that will be generated later with ember
# relative path is backend/static/index.html
@app.route('/')
def root():
    return send_from_directory('static', "index.html")


# route for all entities
@app.route('/api/users')
def users():
    return jsonify({
        "data": [u(i) for i in range(0,10)]
        })

# route for other static files
@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('', path)


if __name__ == '__main__':
    print("use\n"
          "FLASK_APP=dummy.py python -m flask run\n"
          "instead")
    exit(1)
```




Now you can already launch your backend, but frontend will not work of course.

```
FLASK_DEBUG=1 FLASK_APP=api.py python -m flask run --port=5000
```

How to check:
```
curl localhost:5000/api/users
```


## writting frontend

First we need to install [node js]() and ember:
```
$ npm install -g ember-cli
```

Initialize new ember project
```
$ ember new frontend
installing app
  create .editorconfig
  create .ember-cli
  create .eslintrc.js
  create .travis.yml
  create .watchmanconfig
  create README.md
  create app/app.js
  create app/components/.gitkeep
  create app/controllers/.gitkeep
  create app/helpers/.gitkeep
  create app/index.html
  create app/models/.gitkeep
  create app/resolver.js
  create app/router.js
  create app/routes/.gitkeep
  create app/styles/app.css
  create app/templates/application.hbs
  create app/templates/components/.gitkeep
  create config/environment.js
  create config/targets.js
  create ember-cli-build.js
  create .gitignore
  create package.json
  create public/crossdomain.xml
  create public/robots.txt
  create testem.js
  create tests/.eslintrc.js
  create tests/helpers/destroy-app.js
  create tests/helpers/module-for-acceptance.js
  create tests/helpers/resolver.js
  create tests/helpers/start-app.js
  create tests/index.html
  create tests/integration/.gitkeep
  create tests/test-helper.js
  create tests/unit/.gitkeep
  create vendor/.gitkeep
NPM: Installed dependencies
Successfully initialized git.
```

Now we need to generate couple of new files:
```bash
$ ember create model user
$ ember generate  model user
$ ember generate route users
$ ember generate route index
$ ember generate adapter user
```


We need an adapter to specify the location of the endpoint where 
Ember can get data for users. Here we want Ember to look for data on the same server
and port but with suffix `/api`. For example if you server the frontend on 
`http://localhost:5000/` then ember will query `http://localhost:5000/api/users` for data.

```
// file frontend/app/adapters/user.js
import DS from 'ember-data';

export default DS.JSONAPIAdapter.extend({
  namespace: 'api',
});
```


We define `user` model that contains only `info` attribute.
```
// file frontend/app/model/user.js
import DS from 'ember-data';

export default DS.Model.extend({
  info: DS.attr()  
});
```


We add route `/users` to display all available users
```
// file frontend/app/router.js
import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('users');
});

export default Router;
```


Data will be loaded according to the adapter's settings. 
`user` is converted to `users` automatically.
```
// file frontend/app/routes/user.js
import Ember from 'ember';


export default Ember.Route.extend({
  model() {
    return this.get('store').findAll('user');
    // return [{"id": "4545", "info":"123"}];
  }
});
```

Here we define a template for html code for the whole application. 
There will be a header and a link to `users` page.
```
// file frontend/app/templates/application.hbs
<div class="container">
  <div class="menu">
    {{#link-to 'index'}}
      <h1>
        <em>Your app</em>
      </h1>
    {{/link-to}}
    <div class="links">
      {{#link-to 'users'}}
        users
      {{/link-to}}
    </div>
  </div>

  <div class="body">
    {{outlet}}
  </div>
</div>
```


Here we define how output for users will look like. 
We iterate through all entities and display only attribute `info` for them.
```
// file frontend/app/templates/users.hbs
<h2>USERS</h2>

{{#each model as |post|}}
    <p>{{post.info}}</p>
{{/each}}
```


## How to run in debug mode
First we run Flask-based api from `backend/`
```bash
$ FLASK_DEBUG=1 FLASK_APP=api.py python -m flask run
```

Maybe here you need to install depencencies from `frontend/`:
```
npm install
```

Now let's run Ember server in debug mode fom `frontend/`.
```
ember serve --proxy http://localhost:5000
```
Ember server needs to know where API is located. This is done with option `--proxy http://localhost:5000`.
Otherwise Ember tries to get data from `http://localhost:4200/api/users`






















