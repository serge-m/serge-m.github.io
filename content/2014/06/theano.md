Title: Theano
Author: SM!
Date: 2014-06-05 23:30:00
Slug: theano
Tags: useful

<div dir="ltr" style="text-align: left;" trbidi="on"><h2 style="text-align: left;"><span class="st">_Intro _</span></h2><span class="st">_Theano_ is a Python library that allows you to  define, optimize, and evaluate mathematical expressions involving  multi-dimensional arrays efficiently.</span>

<h2 style="text-align: left;"><span class="st">Check gpu is working</span></h2><div style="text-align: left;"><span class="st">Source: </span>[<span class="st">http://deeplearning.net/software/theano/tutorial/using_gpu.html</span>](http://deeplearning.net/software/theano/tutorial/using_gpu.html)</div><div style="text-align: left;">
</div><div style="text-align: left;"><span class="st">Test script: </span></div><blockquote class="tr_bq">
    ::::
    <span class="kn">from</span> <span class="nn">theano</span> <span class="kn">import</span> <span class="n">function</span><span class="p">,</span> <span class="n">config</span><span class="p">,</span> <span class="n">shared</span><span class="p">,</span> <span class="n">sandbox</span>
    <span class="kn">import</span> <span class="nn">theano.tensor</span> <span class="kn">as</span> <span class="nn">T</span>
    <span class="kn">import</span> <span class="nn">numpy</span>
    <span class="kn">import</span> <span class="nn">time</span>
    
    <span class="n">vlen</span> <span class="o">=</span> <span class="mi">10</span> <span class="o">*</span> <span class="mi">30</span> <span class="o">*</span> <span class="mi">768</span>  <span class="c"># 10 x #cores x # threads per core</span>
    <span class="n">iters</span> <span class="o">=</span> <span class="mi">1000</span>
    
    <span class="n">rng</span> <span class="o">=</span> <span class="n">numpy</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">RandomState</span><span class="p">(0</span><span class="p">)</span>
    <span class="n">x</span> <span class="o">=</span> <span class="n">shared</span><span class="p">(</span><span class="n">numpy</span><span class="o">.</span><span class="n">asarray</span><span class="p">(</span><span class="n">rng</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="n">vlen</span><span class="p">),</span> <span class="n">config</span><span class="o">.</span><span class="n">floatX</span><span class="p">))</span>
    <span class="n">f</span> <span class="o">=</span> <span class="n">function</span><span class="p">([],</span> <span class="n">T</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
    <span class="k">print</span> <span class="n">f</span><span class="o">.</span><span class="n">maker</span><span class="o">.</span><span class="n">fgraph</span><span class="o">.</span><span class="n">toposort</span><span class="p">()</span>
    <span class="n">t0</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="n">iters</span><span class="p">):</span>
        <span class="n">r</span> <span class="o">=</span> <span class="n">f</span><span class="p">()</span>
    <span class="n">t1</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
    <span class="k">print</span> <span class="s">'Looping </span><span class="si">%d</span><span class="s"> times took'</span> <span class="o">%</span> <span class="n">iters</span><span class="p">,</span> <span class="n">t1</span> <span class="o">-</span> <span class="n">t0</span><span class="p">,</span> <span class="s">'seconds'</span>
    <span class="k">print</span> <span class="s">'Result is'</span><span class="p">,</span> <span class="n">r</span>
    <span class="k">if</span> <span class="n">numpy</span><span class="o">.</span><span class="n">any</span><span class="p">([</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">op</span><span class="p">,</span> <span class="n">T</span><span class="o">.</span><span class="n">Elemwise</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">f</span><span class="o">.</span><span class="n">maker</span><span class="o">.</span><span class="n">fgraph</span><span class="o">.</span><span class="n">toposort</span><span class="p">()]):</span>
        <span class="k">print</span> <span class="s">'Used the cpu'</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">print</span> <span class="s">'Used the gpu'</span>
</blockquote><div style="text-align: left;">
</div><div style="text-align: left;"><span class="st">&nbsp;Run with two configurations:</span></div><div style="text-align: left;">
</div>
    ::::
    $ THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32 python check1.py
    [Elemwise{exp,no_inplace}(<TensorType(float32, vector)>)]
    Looping 1000 times took 3.06635117531 seconds
    Result is [ 1.23178029  1.61879337  1.52278066 ...,  2.20771813  2.29967761
      1.62323284]
    Used the cpu
    
    $ THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python check1.py
    Using gpu device 0: GeForce GTX 580
    [GpuElemwise{exp,no_inplace}(<CudaNdarrayType(float32, vector)>), HostFromGpu(GpuElemwise{exp,no_inplace}.0)]
    Looping 1000 times took 0.638810873032 seconds
    Result is [ 1.23178029  1.61879349  1.52278066 ...,  2.20771813  2.29967761
      1.62323296]
    Used the gpu
<div style="text-align: left;">
</div><div style="text-align: left;">
</div><div style="text-align: left;">
</div><div style="text-align: left;">
</div><div style="text-align: left;"></div></div>