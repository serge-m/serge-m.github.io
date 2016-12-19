Title: Run docker as pytest fixture 
Author: SergeM
Date: 2016-12-19 21:30:00
Slug: run-docker-as-pytest-fixture
Tags: python,pytest,docker

I need to test external API or perform integration test for my application. 
The extenal application can be accessible through docker image. I want to write a test that has 
* `docker run` as set-up step
* `docker stop/docker rm` as tear down step

As an example lets consider [Seaweedfs](https://github.com/chrislusf/seaweedfs) as external API. 
SeaweedFS is a simple and highly scalable distributed file system. To run it you need to run master and slave images.
After running you can check status (`curl -X GET localhost:9333`).



Lets create two context managers: for master and slave. They will handle running and shutting down docker containers.

Master:

```
import subprocess
import shlex
import requests
import contextlib

import pytest

docker_image = "chrislusf/seaweedfs"


@contextlib.contextmanager
def seaweedfs_master():
    container_id = subprocess.check_output(
        shlex.split("docker run -d -p 9333:9333 {docker_image} master".format(docker_image=docker_image)))
    container_id = container_id.decode('utf8').strip()
    yield container_id
    subprocess.check_output(['docker', 'rm', '-f', container_id])
```

Slave:
```
@contextlib.contextmanager
def seaweedfs_slave():
    with seaweedfs_master() as master:
        container_id = subprocess.check_output(
            shlex.split('docker run -d -p 8080:8080 --link {master_id} '
                        '{docker_image} volume -max=5 -mserver="localhost:9333" -port=8080'.format(
                docker_image=docker_image,
                master_id=master
            )))
        container_id = container_id.decode('utf8').strip()
        yield "http://localhost:9333/"
        subprocess.check_output(['docker', 'rm', '-f', container_id])
```

Helper class and pytest fixture:
```
class SeaWeedFSConnection:
    def __init__(self, url):
        self.url = url


@pytest.fixture(scope="module")
def seaweedfs(request):
    with seaweedfs_slave() as seaweed_url:
        yield SeaWeedFSConnection(seaweed_url)
```

Finally our test:
```
class TestImageStorage:
    def test1(self, seaweedfs):
        url = seaweedfs.url
        response = requests.get(url)
        assert response.status_code == 200

```
