:date: 2019-01-01 10:02
:title: Capture PWM signal using Arduino
:author: SergeM
:slug: capture-pwm-signal-using-arduino

Capture PWM signal using Arduino
################################



This is a draft.

link to the gist: https://gist.github.com/serge-m/5f07fd676b52c4741f2bea275eced729



.. include:: static/2019-12-pwm_visualization.html


See below intra-site link examples in reStructuredText format.

Title: 2019-12-capture-pwm-signal-using-arduino.rst
Author: SergeM
Date: 2019-11-14 07:28
Slug: image-segmentation-with-unlabeled-areas-with-fast-ai
Tags: machine learning, fast.ai, segmentation, computer vision


[fast.ai](http://fast.ai) library has a pretty easy to use yet powerful capabilities for semantic image segmentation. By default all the classes are treated the same. The network is trained to predict all the labels.

Sometimes it's important to provide non-complete labeling. That means for some areas the label is undefined. The performance of the network should exclude that areas in the loss and accuracy computation. That allows the network predict any other class in those areas.

How to exclude certain class ("unlabeled area") from the loss function?

The loss for image segmentation is refined as `CrossEntropyFlat(axis=1)` with the following classes:

```python
def CrossEntropyFlat(*args, axis:int=-1, **kwargs):
    "Same as `nn.CrossEntropyLoss`, but flattens input and target."
    return FlattenedLoss(nn.CrossEntropyLoss, *args, axis=axis, **kwargs)

class FlattenedLoss():
    "Same as `func`, but flattens input and target."
    def __init__(self, func, *args, axis:int=-1, floatify:bool=False, is_2d:bool=True, **kwargs):
        self.func,self.axis,self.floatify,self.is_2d = func(*args,**kwargs),axis,floatify,is_2d
        functools.update_wrapper(self, self.func)

    def __repr__(self): return f"FlattenedLoss of {self.func}"
    @property
    def reduction(self): return self.func.reduction
    @reduction.setter
    def reduction(self, v): self.func.reduction = v

    @property
    def weight(self): return self.func.weight
    @weight.setter
    def weight(self, v): self.func.weight = v

    def __call__(self, input:Tensor, target:Tensor, **kwargs)->Rank0Tensor:
        input = input.transpose(self.axis,-1).contiguous()
        target = target.transpose(self.axis,-1).contiguous()
        if self.floatify: target = target.float()
        input = input.view(-1,input.shape[-1]) if self.is_2d else input.view(-1)
        return self.func.__call__(input, target.view(-1), **kwargs)
```

To exclude some class from the loss function we can follow the advice from the [fast ai forum](https://forums.fast.ai/t/image-segmentation-leaving-some-pixels-unlabeled/40967/2):
```
hasLabel = (t != UNLABELED).float()
loss = mse(p * hasLabel, t * hasLabel)
```

More specifically one can create a copy of the FlattenedLoss and patch it:

```python
class FlattenedLossWithUnlabeled():
    "Same as `func`, but flattens input and target."
    def __init__(self, func, *args, axis:int=-1, floatify:bool=False, is_2d:bool=True, **kwargs):
        self.func,self.axis,self.floatify,self.is_2d = func(*args,**kwargs),axis,floatify,is_2d
        functools.update_wrapper(self, self.func)

    def __repr__(self): return f"FlattenedLoss of {self.func}"
    @property
    def reduction(self): return self.func.reduction
    @reduction.setter
    def reduction(self, v): self.func.reduction = v

    @property
    def weight(self): return self.func.weight
    @weight.setter
    def weight(self, v): self.func.weight = v

    def __call__(self, input:Tensor, target:Tensor, **kwargs)->Rank0Tensor:
        ###### Start ###############
        hasLabel = (t != UNLABELED)
        input = input * hasLabel
        target = target * hasLabel
        ###### End   ###############
 
        input = input.transpose(self.axis,-1).contiguous()
        target = target.transpose(self.axis,-1).contiguous()
        if self.floatify: target = target.float()
        input = input.view(-1,input.shape[-1]) if self.is_2d else input.view(-1)
        return self.func.__call__(input, target.view(-1), **kwargs)
```

Now use that class in your learner:

```python
learn = your_learner(data,  my_model, wd=wd,
                     loss_func=FlattenedLossWithUnlabeled(CrossEntropyLoss, axis=1)
                    )
```
