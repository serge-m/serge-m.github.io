Title: Investigating optical flow by D. Sun (Secrets of optical flow)
Author: SergeM
Date: 2014-11-05 14:33:00
Slug: investigating-optical-flow-by-d-sun
Tags: 

Personal page of the author:&nbsp;[http://cs.brown.edu/~dqsun/research/index.html](http://cs.brown.edu/~dqsun/research/index.html" target="_blank)
Original paper: [http://cs.brown.edu/~dqsun/pubs/cvpr_2010_flow.pdf](http://cs.brown.edu/~dqsun/pubs/cvpr_2010_flow.pdf" target="_blank)
Newer paper: Deqing Sun, Stefan Roth, and Michael J. Black. "A Quantitative Analysis    of Current Practices in Optical Flow Estimation and the Principles    Behind Them". International Journal of Computer Vision (IJCV), 2013 [[pdf](http://cs.brown.edu/~dqsun/pubs/Sun2013QAP.pdf" target="_blank)] [[Source code](http://cs.brown.edu/~dqsun/code/ijcv_flow_code.zip" target="_blank)]

Look inside the sources:



    ::::
    @alt_ba_optical_flow\

    ::::
    @ba_optical_flow\

    ::::
        ...

    ::::
        compute_flow_base.m
<div style="margin-left: auto; margin-right: 0; width: 70%;">itarates:
1) Iterate flow computation
2) Linearization update, for j = 1:this.max_linear. In the simple case max_linear==1, when I use x = A\b solver for linear system. Probably for more complicated solvers&nbsp; max_linear > 1

</div>
    ::::
        compute_flow.m
<div style="margin-left: auto; margin-right: 0; width: 70%;">calls pre_process_data (preprocessing, normalization, image pyramyd).  Loop through iterations: 
<pre class="brush:cpp">for ignc = 1:this.gnc_iters   
</pre>Calls compute_flow_base.m.  </div>
    ::::
        ...

    ::::
    @classic_nl_optical_flow\

    ::::
    @hs_optical_flow\

    ::::
    data\

    ::::
    utils\

    ::::
        ... 

    ::::
        pre_process_data.m 
<div style="margin-left: auto; margin-right: 0; width: 70%;">-- several preptocessing options for images. The first is texture decomposition.  if no texture decomposition, scale image to [0, 255] range. Build image pyramyd. 
there is also following code:  
<pre class="brush: cpp">% For segmentation purpose
    data.org_pyramid_images = compute_image_pyramid(this.images, f,...
        this.pyramid_levels, 1/this.pyramid_spacing);
    data.org_color_pyramid_images = compute_image_pyramid(this.color_images,...
        f, this.pyramid_levels, 1/this.pyramid_spacing);

</pre>In my case I don't need segmentation and use simple OF method. It seems it's just bad code design. Dig deeper.  </div>
    ::::
        ... 

    ::::
    estimate_flow_demo.m

    ::::
    estimate_flow_interface.m 

    ::::
    load_of_method.m

<div style="margin-left: auto; margin-right: 0; width: 70%;">-- switcher that recursively initializes members of OF object. E.g. if you want to load 'classic+nl-brightness' method, it loads 'classic+nl' first: 
<pre class="brush: cpp">case 'classic+nl'        
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
</pre>and then applies the difference: 
<pre class="brush: cpp">case 'classic+nl-fast-brightness'
        ope = load_of_method('classic+nl');        
        ope.max_iters       = 3;
        ope.gnc_iters       = 2;
        ope.texture         = false;
</pre></div>
    ::::
    readme.pdf
</div></div>