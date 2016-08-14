Title: Pylearn2 out of memory error
Author: SM!
Date: 2014-08-14 18:51:00
Slug: pylearn2-out-of-memory-error
Tags: pylearn2

<div dir="ltr" style="text-align: left;" trbidi="on">I am trying to train NN using pylearn2
I use stochastic gradient decent.
I had always a message about failed GPU memory&nbsp; allocation in
train->self.sgd_update(*batch)
To fix it, I reduced size of the batch in yaml-config:
batch_size: 200
was replaced by
batch_size: 100

</div>