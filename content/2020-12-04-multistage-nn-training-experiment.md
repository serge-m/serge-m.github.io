---
Title: Multistage NN training experiment
Author: SergeM
Date: 2020-01-01 10:00:00
Slug: multistage-nn-training-experiment
aliases: [/multistage-nn-training-experiment.html]
Tags: [ pytorch, deep learning, computer vision, neural networks, draft]
---





Ideas for multistage NN training.


There is some research on continuous learning without catastrophic forgetting . 
For example 
ANML: Learning to Continually Learn (ECAI 2020)
[arxiv](https://arxiv.org/abs/2002.09571)
[code](https://github.com/uvm-neurobotics-lab/ANML)
[video](https://www.youtube.com/watch?v=t7dSUY-4KHc)

The code for the paper is based on another one:
OML (Online-aware Meta-learning) ~ NeurIPS19
[code](https://github.com/khurramjaved96/mrcl)
[video](https://www.youtube.com/watch?v=XlEqFeQiuhk)

OML paper derives some code from MAML:

Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks
[pdf](https://arxiv.org/pdf/1703.03400.pdf)
[official tf code](https://github.com/cbfinn/maml), also includes some links to other implementations.
[pytorch code](https://github.com/dragen1860/MAML-Pytorch)

The target for me is to create a multistage network that is suitable for online learning from a stream of natural data, e.g. video or timeseries. That setup is very similar to the online few shot learning they explore in ANML or OML. I think it makes sense to understand the background paper (MAML) first. So I would start with reading and understanding it's code and reproducing the results.

However there is a paper 
MAML++ 
[pdf](https://arxiv.org/pdf/1810.09502.pdf)
[code](https://github.com/AntreasAntoniou/HowToTrainYourMAMLPytorch)
that is a better version of MAML. It's much easier to train MAML++ than the original MAML. 
That paper also has a bit nicer code structure from the first glance. 
I would start from it. 


Plan:

* download code for MAML++, download omniglot data set, run experiment to reproduce the results of MAML++ paper.

* while it's being trained, scan through MAML++ and (optionally) MAML. Understand the code

* design an experiment for online learning, maybe one reproducing with OML/ANML. adapt the code accordingly. Run training

* Here are some further options:

  * design a multistage architecture an implement it

  * or convert the network into depth prediction or camera parameters estimation in online mode




There is also a [Reptile](https://github.com/dragen1860/Reptile-Pytorch) paper with code that can be useful.
It proposes some simplification of gradient descent steps from MAML. 


Video with a review of several methods of continual learning: 
[Continual Learning in Neural Networks by Pulkit Agarwal](https://www.youtube.com/watch?v=06_iBtEeUTc)
