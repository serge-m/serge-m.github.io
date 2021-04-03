---
Title: Rest API for TensorFlow model
Author: SergeM
Date: 2017-05-21 22:00:00
Slug: rest-api-for-tensorflow-model
aliases: [/rest-api-for-tensorflow-model.html]
Tags: [ tensorflow,server,REST,machine learning]
---





[TensorFlow Serving](https://tensorflow.github.io/serving), [sources](https://github.com/tensorflow/serving) - library for serving machine learning models. Written in C++ and Python. Server is in C++. 
Requires [Bazel](https://bazel.build/) - Google's build tool. Doesn't work with python 3. Probably fast.


[TensorFlow: How to freeze a model and serve it with a python API](https://blog.metaflow.fr/tensorflow-how-to-freeze-a-model-and-serve-it-with-a-python-api-d4f3596b3adc)

[Building a Machine Learning App with AWS Lambda](https://www.slideshare.net/fabiandubois/tensorflow-in-production-with-aws-lambda) (slides)

[Pipeline.io](http://pipeline.io/) - End-to-End, Continuous Spark ML + Tensorflow AI Data Pipelines,  [Sources](https://github.com/fluxcapacitor/pipeline)

Interesting [thread](https://groups.google.com/a/tensorflow.org/forum/#!topic/discuss/qwpIhjqC9X8). They propose to use 
"saved_model_cli binary (in tools/), which you can feed a SavedModel, and pass input data via files."

## TensorFlow Serving
TensorFlow Serving is build using Bazel - a build tool from Google.

[Architecture overview](http://tensorflow.github.io/serving/architecture_overview)

[Basic serving](http://tensorflow.github.io/serving/serving_basic) Hmmm

Bazel can build binaries from several languages. Output of the build is a directory with binaries and all the dependencies. So after building TensorFlow Serving you get a `bazel-bin` softlink. It ponts to a directory `/home/<your user>/.cache`  that seemingly contains all the binaries that the server/client needs. Python scripts are also wrapped into some launcher scripts. 

It seems that `bazel` automatically downloads some pre-built binaries implicitly.

I was able to build tensorflow in a docker as explained [here](http://tensorflow.github.io/serving/serving_inception). I am not very happy about the size of the docker image (several GB).

`bazel-bin` directory can be extracted from the docker and binaries can be executed outside of the docker (on Ubuntu machine in works for me). 

### Compiled examples for tensorflow serving
Download compiled examples [here](https://drive.google.com/file/d/0Bwavy70LtHVUeGxSQ0tRbXVkWjg/view?usp=sharing) and extract files:
```
tar xf ./bazel-bin.tar.gz
```
The package contains compiled tensorflow serving app and example apps. 

I prefer to run it in python virtual environment. Let's create one and install needed packages:

```
virtualenv -p python2.7 py2
source ./py2/bin/activate
pip install numpy mock grpcio
```

To make compiled scripts use python from virtual environment we should patch wrapper files. 
For example `bazel-bin/tensorflow_serving/example/mnist_saved_model` is a wrapper script for `mnist_saved_model.py`. 

We will change path to python that that wrapper uses. Use text editor to edit the wrapper. I use `nano`:
```
nano bazel-bin/tensorflow_serving/example/mnist_saved_model 
```

Replace
```
PYTHON_BINARY = '/usr/bin/python'
```
with 

```
PYTHON_BINARY = 'python'
```
save and exit. We will need to do that for each wrapper we want to run.


<details>
<summary>The same action for all files is acheivable using command line editor (click <u>here</u> to see)</summary>
  <pre>find . -maxdepth 1 -type f | xargs sed -i.original "s|PYTHON_BINARY = '/usr/bin/python'|PYTHON_BINARY = 'python'|g"
  </pre>
</details>



Now we can run a commands from Tensorflow Serving tutorial:
```
bazel-bin/tensorflow_serving/example/mnist_saved_model --training_iteration=100 --model_version=1 /tmp/mnist_model
```

### Possible issues
#### ImportError: No module named grpc.beta
Solution:

```
sudo pip install grpcio
```

Copied from docker python scripts seems to be chained to global system python. Thus installing grpcio inside an active virtualenv doesn't work. 

#### ImportError: No module named numpy
Solution: install numpy using `pip install numpy` and make sure you use appropriate version of python. 

By default "compiled" versions of python scripts from tensorflow serving use python from `/usr/bin/python`. If you want to use another version patch wrapper files accordingly.

#### tensorflow.python.framework.errors_impl.NotFoundError: ... _single_image_random_dot_stereograms.so: undefined symbol ...
Probably there is a but in examples. 
Error message example:
```
Traceback (most recent call last):
  File "/home/usr/serving/bazel-bin/tensorflow_serving/example/mnist_export.runfiles/tf_serving/tensorflow_serving/example/mnist_export.py", line 36, in <module>
    from tensorflow.contrib.session_bundle import exporter
  File "/home/usr/serving/bazel-bin/tensorflow_serving/example/mnist_export.runfiles/org_tensorflow/tensorflow/contrib/__init__.py", line 34, in <module>
    from tensorflow.contrib import image
  File "/home/usr/serving/bazel-bin/tensorflow_serving/example/mnist_export.runfiles/org_tensorflow/tensorflow/contrib/image/__init__.py", line 39, in <module>
    from tensorflow.contrib.image.python.ops.single_image_random_dot_stereograms import single_image_random_dot_stereograms
  File "/home/usr/serving/bazel-bin/tensorflow_serving/example/mnist_export.runfiles/org_tensorflow/tensorflow/contrib/image/python/ops/single_image_random_dot_stereograms.py", line 26, in <module>
    "_single_image_random_dot_stereograms.so"))
  File "/home/usr/serving/bazel-bin/tensorflow_serving/example/mnist_export.runfiles/org_tensorflow/tensorflow/contrib/util/loader.py", line 55, in load_op_library
    ret = load_library.load_op_library(path)
  File "/home/usr/serving/bazel-bin/tensorflow_serving/example/mnist_export.runfiles/org_tensorflow/tensorflow/python/framework/load_library.py", line 64, in load_op_library
    None, None, error_msg, error_code)
tensorflow.python.framework.errors_impl.NotFoundError: /home/usr/serving/bazel-bin/tensorflow_serving/example/mnist_export.runfiles/org_tensorflow/tensorflow/contrib/image/python/ops/_single_image_random_dot_stereograms.so: undefined symbol: _ZN6google8protobuf8internal10LogMessageC1ENS0_8LogLevelEPKci
```

Solution:

comment out
```
#from tensorflow.contrib.image.python.ops.single_image_random_dot_stereograms import single_image_random_dot_stereograms
```
in
```
bazel-bin/tensorflow_serving/example/mnist_saved_model.runfiles/org_tensorflow/tensorflow/contrib/image/__init__.py
```

[Source](https://github.com/tensorflow/serving/issues/421#issuecomment-300718439)

## See also

* [Machine learning links](/machine-learning-links.html)







