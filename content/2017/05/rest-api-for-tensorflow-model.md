Title: Rest API for TensorFlow model
Author: SergeM
Date: 2017-05-21 22:00
Slug: rest-api-for-tensorflow-model
Tags: tensorflow,server,REST,machine learning



[TensorFlow Serving](https://tensorflow.github.io/serving), [sources](https://github.com/tensorflow/serving) - library for serving machine learning models. Written in C++ and Python. Server is in C++. 
Requires [Bazel](https://bazel.build/) - Google's build tool. Doesn't work with python 3. Probably fast.


[TensorFlow: How to freeze a model and serve it with a python API](https://blog.metaflow.fr/tensorflow-how-to-freeze-a-model-and-serve-it-with-a-python-api-d4f3596b3adc)

[Building a Machine Learning App with AWS Lambda](https://www.slideshare.net/fabiandubois/tensorflow-in-production-with-aws-lambda) (slides)

[Pipeline.io](http://pipeline.io/) - End-to-End, Continuous Spark ML + Tensorflow AI Data Pipelines,  [Sources](https://github.com/fluxcapacitor/pipeline)

## About TensorFlow Serving
TensorFlow Serving is build using Bazel - a build tool from Google.

Bazel can build binaries from several languages. Output of the build is a directory with binaries and all the dependencies. So after building TensorFlow Serving you get a `bazel-bin` softlink. It ponts to a directory `/home/<your user>/.cache`  that seemingly contains all the binaries that the server/client needs. Python scripts are also wrapped into some launcher scripts. So far I don't know exactly the purpose of those wrappings. 

It seems that `bazel` automatically downloads some pre-built binaries implicitly.

I was able to build tensorflow in a docker as explained [here](http://tensorflow.github.io/serving/serving_inception). I am not very happy about the size of the image (several GB).

`bazel-bin` directory can be extracted from the docker and binaries can be executed outside of the docker (on Ubuntu machine in works for me). 


See also:

* [Machine learning links](/machine-learning-links.html)







