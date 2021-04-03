---
Title: Testing json responses in Flask REST apps with pytest
Author: SergeM
Date: 2016-11-27 22:47:00
Slug: testing-json-responses-in-Flask-REST-apps-with-pytest
aliases: [/testing-json-responses-in-Flask-REST-apps-with-pytest.html]
Tags: [ python,flask,pytest,REST,testing,connexion,best practices,tests,API]
---



Testing is an essential part of software developmnet process. Unfortunately best prictives for python are established not as good as for example in Java world.
Here I try to explain how to test Flask-based web applications.
We want to test endpoints behaviour including status codes and parameters encoding. It means testing of handler functions for those endpoints is not enough.

Tests for endpoints can be considered/used as high-level acceptance tests.

The code consists of two files: `sample_app.py` (productions) and `sample_app_test.py` (testing). Testing is run using py.test.

## Code of sample_app.py
Creating Flask application:
```python
from flask import Flask, request, Response, json

app = Flask(__name__)
```
Helper class for JSON-based response:

```python
class JsonResponse(Response):
    def __init__(self, json_dict, status=200):
        super().__init__(response=json.dumps(json_dict), status=status, mimetype="application/json")
```

Defining GET and POST endpoints. The puprose of the `/add` endpoint is to return doubled value.

```python
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add', methods=['POST'])
def add():
    json = request.json
    resp = JsonResponse(json_dict={"answer": json['key'] * 2}, status=200)
    return resp
```
Main section that prints help message. (Alternative launching procedure can be applied)

```python
if __name__ == '__main__':
    script_name = __file__
    print("run:\n"
          "FLASK_APP={} python -m flask run --port 8000 --host 0.0.0.0".format(script_name))
    exit(1)

```


## Code of sample_app_test.py
Fixture for test client:
```python
import json
import pytest
from sample_app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client
```
Helper functions for encoding and decoding jsons:
```python
def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

```

The simplest test for GET endpoint:
```python
def test_dummy(client):
    response = client.get('/')
    assert b'Hello, World!' in response.data
```

Test for POST endpoint. Checking resulting json:
```python
def test_json(client):
    response = post_json(client, '/add', {'key': 'value'})
    assert response.status_code == 200
    assert json_of_response(response) == {"answer": 'value' * 2}
```

## Testing multipart file upload
Imaging you have an endpoint that accepts POST requests with multipart files:
```python 
@app.route('/send', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file_received = request.files['file']
        file_name = uuid.uuid4().hex
        
        with open(file_name, "wb") as fout:
            fout.write(file_received.read())
        
        return "file saved to {}".format(file_name)
    return "Wrong request"
```

To test it we need a helper-function:
```python
def post_files(client, url, map_name_to_file: Dict):
    """Posts Multipart-encoded files to url
    :param client: flask test client fixture
    :param url: string URL
    :param map_name_to_file: dictionary name->file-like object
    """

    map_name_to_file_and_name = {name: (file, "mocked_name_{}".format(name)) for
                                 name, file in map_name_to_file.items()}
    return client.post(url, data=map_name_to_file_and_name, content_type='multipart/form-data')
```
 
Test itself:
```python
def test_multipart_files(client):
    response = post_files(client, '/send', {'file': BytesIO(b"content")})
    assert response.status_code == 200
```

Inspired by [this gist](https://gist.github.com/DazWorrall/1779861)


## Testing connextion

[Connextion](https://github.com/zalando/connexion/) is a wrapper around Flask that handles Oauth2 security and responses validation. 
Test for connextion app must include security checks.

#### swagger.yaml
In this file we define API of our microservice. Also it contains security settings.
```yaml
swagger: '2.0'
info:
  title: your app
  version: "0.1"
consumes:
  - application/json
produces:
  - application/json
security:
  - oauth2: [myscope]
paths:
  /:
    get:
      operationId: endpoints.root
      summary: |
        test
      responses:
        200:
          description: it works.
        401:
          description: bad auth.
securityDefinitions:
  oauth2:
    type: oauth2
    flow: implicit
    authorizationUrl: https://oauth.example/token_info
    x-tokenInfoUrl: https://oauth.example/token_info
    scopes:
      myscope: Unique identifier of the user accessing the service.
```

#### endpoints.py
Endpoints implementation.

```python
def root():
    return {"result": "lol"}, 200
```

#### test_endpoints.py
```python
import json
import os

import pytest
from connexion import App

SPEC_FOLDER = os.path.join(os.path.dirname(__file__), '../')  # path to a directory with swagger.yaml file


# fixture for replacing calls to oauth provider in connexion
@pytest.fixture
def oauth_requests(monkeypatch):
    # _fake_get is defined later in the code
    monkeypatch.setattr('connexion.decorators.security.session.get', _fake_get)


# fixture for running test app with a predefined swagger file
@pytest.fixture(scope="session")
def secure_endpoint_app():
    cnx_app = App(__name__, port=5001, specification_dir=SPEC_FOLDER, debug=True)
    cnx_app.add_api('swagger.yaml', validate_responses=True)
    return cnx_app

CORRECT_TOKEN = "100"
INCORRECT_TOKEN = "bla"

# we are testing our app with mocked security provider. 
# threfore we use 
# 1. oauth_requests for patching security
# 2. secure_endpoint_app for loading application with a required swagger file
def test_security(oauth_requests, secure_endpoint_app):
    app_client = secure_endpoint_app.app.test_client()


    # must fail without Authorization header
    get_bye_no_auth = app_client.get('/')  # type: flask.Response
    assert get_bye_no_auth.status_code == 401

    # fails because of incorrect token
    get_bye_bad_auth = app_client.get('/', headers={"Authorization": "Bearer {}".format(INCORRECT_TOKEN)})  # type: flask.Response
    assert get_bye_bad_auth.status_code == 401

    # token is correct. Must return 200
    get_bye_good_auth = app_client.get('/', headers={"Authorization": "Bearer {}".format(CORRECT_TOKEN)})  # type: flask.Response
    assert get_bye_good_auth.status_code == 200


# fake response object used in _fake_get function
class FakeResponse(object):
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text
        self.ok = status_code == 200

    def json(self):
        return json.loads(self.text)


# here we "check" tokens. Of course we don't do actual call to Oauth provider, we mock it.
def _fake_get(url, params=None, headers=None, timeout=None):
    """
    :type url: str
    :type params: dict| None
    """
    headers = headers or {}
    if url == "https://oauth.example/token_info":
        token = headers.get('Authorization', 'invalid').split()[-1]
        if token in [CORRECT_TOKEN, "has_myscope"]:
            return FakeResponse(200, '{"uid": "test-user", "scope": ["myscope"]}')
        if token in ["200", "has_wrongscope"]:
            return FakeResponse(200, '{"uid": "test-user", "scope": ["wrongscope"]}')
        if token == "has_myscope_otherscope":
            return FakeResponse(200, '{"uid": "test-user", "scope": ["myscope", "otherscope"]}')
        if token in [INCORRECT_TOKEN, "is_not_invalid"]:
            return FakeResponse(404, '')
    return url

```

inspired by connexiton tests: [[1]](https://github.com/zalando/connexion/blob/master/tests/conftest.py) and [[2]](https://github.com/zalando/connexion/blob/master/tests/api/test_secure_api.py)




## Related links:
* [Testing flask applications](http://flask.pocoo.org/docs/0.11/testing/)
* [pytest fixtures for flask](https://github.com/pytest-dev/pytest-flask) I haven't checked them. Maybe uyseful
* [Flaskr test application from examples of Flask](https://github.com/pallets/flask/tree/master/examples/flaskr)
* [Gist "Testing file upload handling in Flask"](https://gist.github.com/DazWorrall/1779861)

## See also
* [Pytest cheatsheet](/pytest-cheatsheet.html)
