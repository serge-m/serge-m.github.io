---
Title: Python - Multiprocessing
Author: SergeM
Date: 2020-10-01 20:00:00
Slug: python-multiprocessing
aliases: [/python-multiprocessing.html]
Tags: [ python, multiprocessing, useful, libraries, multiprocessing]
---



## Libraries

* Standard [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

* [Pebble](https://pypi.org/project/Pebble/) 
  \- pretty close to the standard one, but with a bit nicer interface

* [Dask](https://dask.org/) 
  \- well maintained and (almost) drop-in replacement of numpy and pandas:

```python
# Arrays implement the Numpy API
import dask.array as da
x = da.random.random(size=(10000, 10000),
                     chunks=(1000, 1000))
x + x.T - x.mean(axis=0)

# Dataframes implement the Pandas API
import dask.dataframe as dd
df = dd.read_csv('s3://.../2018-*-*.csv')
df.groupby(df.account_id).balance.sum()

# Dask-ML implements the Scikit-Learn API
from dask_ml.linear_model \
  import LogisticRegression
lr = LogisticRegression()
lr.fit(train, test)
```

* [mptools](https://github.com/PamelaM/mptools) - seems like an abandoned project.
  The autor had a nice article though: 
  [Things I Wish They Told Me About Multiprocessing in Python](https://www.cloudcity.io/blog/2019/02/27/things-i-wish-they-told-me-about-multiprocessing-in-python/)
  
  
* [Ray](https://github.com/ray-project/ray)

  Related article:
  [10x Faster Parallel Python Without Python Multiprocessing](https://towardsdatascience.com/10x-faster-parallel-python-without-python-multiprocessing-e5017c93cce1)

<iframe width="560" height="315" src="https://www.youtube.com/embed/uPeCk7Wx8HU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



## Progress bar for parallel tasks

Often one need to run some slow function in parallel in order to speed up the computation.
In user facing apps it's important to visualize the progress.
One can use `multiprocessing.Pool` and `tqdm` for it.
```python
import multiprocessing
import numpy as np
import tqdm


def slow_operation(a):
    """
    Slow operation, return value is not needed in main.
    For example the function opens a file, processes it and dumps the results to a new location.
    """
    z = np.random.random([1000, 1000])
    for i in range(50):
        z = z * (z - 0.5)
    return z

```


One cannot apply tqdm to the `Pool.map` because the whole processing happens before the tqdm can iterate the result.  
However it's possible to use `Pool.imap` or `Pool.imap_unordered` if the order is not important.

```python

def parallel_with_imap_unordered():
    with  multiprocessing.Pool(6) as pool:
        for _ in tqdm.tqdm(pool.imap_unordered(slow_operation, range(100)), total=100):
            pass
```

It's nice that we don't need to do `pool.join()` here because `imap*` waits for all the tasks to complete.

Don't forget to set chunk size:

> For very long iterables using a large value for chunksize can make the job complete much faster than using the default value of 1.


Alternatively we can use callbacks to update a global progress bar in a main process:

```python
def parallel_with_callback():
    pbar = tqdm.tqdm(total=100)

    def update(*a):
        pbar.update()

    pool = multiprocessing.Pool(6)
    for i in range(pbar.total):
        pool.apply_async(slow_operation, args=(i,), callback=update)
    pool.close()
    pool.join()
```

That method requires `pool.join` to wait for all the processes to finish. 

## Using Pipes for parallel stateful processes

Let's consider the following task. We have to implement a controller.
The controller defines a processing graph with 4 interconnected stages:

* detector

* size_estimator (depends on detector)

* classifier (depends on detector)

* aggregator (depends on size_estimator and classifier)

This could be a model for some computer vision pipeline and controller processes frames coming from a camera.

Sequential version of the controller could look like this
```python
class Controller:
    def __init__(self):
        self.detector = Detector()
        self.size_estimator = Processor(fn=_compute_size)
        self.classifier = Processor(fn=_obj_to_class)
        self.aggregator = Aggregator()
        self.stats = []

    def __call__(self, frame):
        objects = self.detector(frame)
        sizes = self.size_estimator(objects)
        classes = self.classifier(objects)
        stat = self.aggregator(sizes, classes)
        self.stats.append(stat)

    def finish(self):
        pass

```

Usage of the controller:
```python
def execute_test(controller):
    num_frames = 10
    t = time.time()
    for i in range(num_frames):
        frame = np.empty((100, 100), dtype='uint8')
        controller(frame)
    controller.finish()
    t = time.time() - t
    print(f"FPS: {num_frames / t}")
    return t
``` 

As I have mentioned above two stages - size estimation and classification - can be executed in parallel. 
A standard solution for that could be `multiprocessing.Pool` with a function like `map` or `imap`.
That works if our processing stages are **stateless and the initialization is cheap**
It is not always the case. 

If `classifier` requires a costly initialization, e.g. loading a big neural network into memory, it would be 
nice to have it initialized only once. We can do it in a separate process. 
If we were using a programming language other than Python, we could use threads for it. 
But in python we have GIL. 

Controller has to send data to another process and receive the results.
Communication between parallel processes is a dangerous thing. 
Let's try to use `multiprocessing.Pipe` for that.

```python
class ParallelPipeController:
    def __init__(self, size_estimator_factory=lambda: Processor(fn=_compute_size)):
        self.pipe_size_estimator, pipe_size_worker = Pipe()

        self.detector = Detector()
        self.size_estimator = Process(
            target=pipe_worker,
            args=(pipe_size_worker, size_estimator_factory),
            daemon=True
        )
        self.classifier = Processor(fn=_obj_to_class)
        self.aggregator = Aggregator()
        self.stats = []
        self.size_estimator.start()

    def __call__(self, frame):
        objects = self.detector(frame)
        self.pipe_size_estimator.send(objects)
        classes = self.classifier(objects)
        try:
            sizes = self.pipe_size_estimator.recv()
        except EOFError as e:
            raise RuntimeError("Unable to get data from process. Probably exception occurred") from e
        stat = self.aggregator(sizes, classes)
        self.stats.append(stat)

    def finish(self):
        self.pipe_size_estimator.send(None)
        self.size_estimator.join()

```

`pipe_worker` would look like this:

```python
def pipe_worker(pipe, factory: Callable):
    try:
        print("worker started")
        processor = factory()
        while True:
            msg = pipe.recv()
            if msg is None:
                break
            result = processor(msg)
            pipe.send(result)
        print("worker exited correctly")
    except Exception:
        print("An exception occurred. We notify the main process by closing our end of the pipe."
              "It would be nicer to send some info to the main process.")
        pipe.close()
```

Comparing those two controllers:
```python
print("sequential")
execute_test(Controller())
print("parallel")
execute_test(ParallelPipeController())
```
   
Sample output:
    
    sequential
    FPS: 1.7753397948365568
    parallel
    worker started
    worker exited correctly
    FPS: 2.820896038347416



Full code is [here](https://github.com/serge-m/code-training/tree/master/python/parallel/stateful_process_workers).

There are some alternative workarounds to deal with initialization in standard `multiprocessing`. 
They usually require some global variables. See for example:

* Stack overflow [how to use initializer to set up my multiprocess pool?](https://stackoverflow.com/questions/10117073/how-to-use-initializer-to-set-up-my-multiprocess-pool)

* [Multiprocessing.Pool - Pass Data to Workers w/o Globals: A Proposal](https://thelaziestprogrammer.com/python/multiprocessing-pool-expect-initret-proposal)


# Processing KeyboardInterrupt in workers

Apparently there are some issue with KeyboardInterrupt and multiprocessing:

> when workers are idle, Python’s KeyboardInterrupt is not handled correctly 
> by the multiprocessing module, which results in not only a lot of stacktraces 
> spewed to the console, but also means the parent process will hang indefinitely.

[Python: Using KeyboardInterrupt with a Multiprocessing Pool](https://noswap.com/blog/python-multiprocessing-keyboardinterrupt), 2011.
