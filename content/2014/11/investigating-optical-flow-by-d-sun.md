Title: Investigating optical flow by D. Sun (Secrets of optical flow)
Author: SergeM
Date: 2014-11-05 14:33:00
Slug: investigating-optical-flow-by-d-sun
Tags: optical flow

Personal page of the author:
[http://cs.brown.edu/~dqsun/research/index.html](http://cs.brown.edu/~dqsun/research/index.html)

Original paper: [http://cs.brown.edu/~dqsun/pubs/cvpr_2010_flow.pdf](http://cs.brown.edu/~dqsun/pubs/cvpr_2010_flow.pdf)

Newer paper: Deqing Sun, Stefan Roth, and Michael J. Black. "A Quantitative Analysis of Current Practices in Optical Flow Estimation and the Principles    Behind Them". International Journal of Computer Vision (IJCV), 2013 
[ [pdf](http://cs.brown.edu/~dqsun/pubs/Sun2013QAP.pdf)] [[Source code](http://cs.brown.edu/~dqsun/code/ijcv_flow_code.zip)]

Look inside the sources:

```
    @alt_ba_optical_flow\
    @ba_optical_flow\
        ...
        compute_flow_base.m
```
itarates:

1) Iterate flow computation

2) Linearization update, for j = 1:this.max_linear. In the simple case `max_linear==1`, when I use `x = A\b` solver for linear system. Probably for more complicated solvers `max_linear > 1`

```
        compute_flow.m
```

calls pre_process_data (preprocessing, normalization, image pyramyd).  Loop through iterations: 

```
for ignc = 1:this.gnc_iters   
```

Calls `compute_flow_base.m`  

```
    ...
    @classic_nl_optical_flow\
    @hs_optical_flow\
    data\
    utils\
        ... 
        pre_process_data.m 
```

-- several preptocessing options for images. The first is texture decomposition.  if no texture decomposition, scale image to [0, 255] range. Build image pyramyd. 
there is also following code:  
```
% For segmentation purpose
    data.org_pyramid_images = compute_image_pyramid(this.images, f,...
        this.pyramid_levels, 1/this.pyramid_spacing);
    data.org_color_pyramid_images = compute_image_pyramid(this.color_images,...
        f, this.pyramid_levels, 1/this.pyramid_spacing);

```
In my case I don't need segmentation and use simple OF method. It seems it's just bad code design. Dig deeper. 

```
    ... 

    estimate_flow_demo.m
    estimate_flow_interface.m 
    load_of_method.m
```

-- switcher that recursively initializes members of OF object. E.g. if you want to load 'classic+nl-brightness' method, it loads 'classic+nl' first: 


```
case 'classic+nl'        
        ope = classic_nl_optical_flow;
        
        ope.texture  = true;
        ope.median_filter_size   = median_filter_size;
        
        ope.alp = 0.95;
        ope.area_hsz = 7;
        ope.sigma_i  = 7;
        ope.color_images = ones(1,1,3);
        
        ope.lambda = 3;
        ope.lambda_q =3;
        %ope.display  = true;    
```
and then applies the difference: 
```
case 'classic+nl-fast-brightness'
        ope = load_of_method('classic+nl');        
        ope.max_iters       = 3;
        ope.gnc_iters       = 2;
        ope.texture         = false;
```

