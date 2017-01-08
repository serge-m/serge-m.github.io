Title: Simple tests of classic OF methods
Author: SergeM
Date: 2014-11-05 22:30:00
Slug: simple-tests-of-classic-of-methods
Tags: optical flow

## BA method, simple synthetic images 

For simple synthetic images:

```
I0 =

         0    0.5000         0
         0    1.0000         0
         0    0.5000         0
    0.1000         0         0
    0.0500         0         0
    0.0500    0.1000         0

I1 =

    0.5000         0         0
    1.0000         0         0
    0.5000         0         0
         0    0.1000         0
         0    0.0500         0
         0    0.0500    0.1000
```

Running code by D.Sun. Disabled texture decomposition, disabled multiscale processing.  

```
uv = estimate_flow_interface(I0, I1, 'classic-c-brightness', [], {'display', 1, 'pyramid_levels', 1, 'gnc_pyramid_levels', 1});
```



After first iteration ( `loop for ignc = 1:this.gnc_iters&nbsp; in dsun_ijcv_flow_code\@ba_optical_flow\compute_flow.m`):
![](http://4.bp.blogspot.com/-TW_Kgc_c4xM/VFo0XQRJdQI/AAAAAAAACDU/LmjLPEhpcFM/s1600/gnc_iter_1.png) 

After 2nd iteration: 
![](http://1.bp.blogspot.com/-iic-jinHYR8/VFo0XZiLU5I/AAAAAAAACDQ/Yx-509YrRos/s1600/gnc_iter_2.png)

After 3rd iteration:
![](http://3.bp.blogspot.com/-nNWtlW7GjNI/VFo0XRzxjDI/AAAAAAAACDM/0XNuLNB76yc/s1600/gnc_iter_3.png)


I think, it is right answer.


```
uv(:,:,1) =

   -0.9995   -0.9995   -0.9996
   -0.9994   -0.9994   -0.9995
   -0.9992   -0.9992   -0.9992
    0.9992    0.9992    0.9992
    0.9994    0.9994    0.9994
    0.9995    0.9994    0.9994


uv(:,:,2) =

  1.0e-003 *

   -0.2083   -0.2080   -0.2080
   -0.2080   -0.1848   -0.1848
   -0.1861   -0.1616   -0.1848
   -0.1507   -0.0860   -0.1183
   -0.0860   -0.0633   -0.1183
   -0.0396   -0.0396   -0.0860
 ```
 
 
 ## BA method. Another pair of images  
 
 ```
 I0 =

         0    0.5000         0
         0    1.0000         0
         0    0.5000         0


I1 =

    0.5000         0         0
    1.0000         0         0
    0.5000         0         0
```

1st iteration 
```
uv(:,:,1) =
    
        -1    -1    -1
        -1    -1    -1
        -1    -1    -1
    
    
    uv(:,:,2) =
    
      1.0e-014 *
    
        0.8281    0.8281    0.8281
        0.8281    0.8281    0.8281
        0.8281    0.8281    0.8281
```    

2nd iteration 

```
    uv(:,:,1) =
    
       -1.0000   -1.0000   -1.0000
       -1.0000   -1.0000   -1.0000
       -1.0000   -1.0000   -1.0000
    
    
    uv(:,:,2) =
    
      1.0e-013 *
    
       -0.5965   -0.5965   -0.5965
       -0.5965   -0.5965   -0.5965
       -0.5965   -0.5965   -0.5965
```
    
3rd iteration 

```
    uv(:,:,1) =
    
       -1.0000   -1.0000   -1.0000
       -1.0000   -1.0000   -1.0000
       -1.0000   -1.0000   -1.0000
    
    
    uv(:,:,2) =
    
      1.0e-011 *
    
        0.5374    0.5374    0.5374
        0.5374    0.5374    0.5374
        0.5374    0.5374    0.5374
```

Visually the same:
![](http://2.bp.blogspot.com/-ihcssiAwj2c/VFo2yZDh_6I/AAAAAAAACDo/pHmB5EVb6Cw/s200/simple_gnc_iter_1.png)
  


## HS method. Simple image

BA - is not the simpliest method. I found there is implmentation of Horn-Schunk.

I found that the results are really poor, when my "image elements" ar just on the border. So I extended image by zeros.

I use the following command: 

```
uv = estimate_flow_interface(I0, I1, ...
    'hs-brightness', [], ...
    {'display', 1, 'pyramid_levels', 1, 'gnc_pyramid_levels', 1, ...
     'pyramid_spacing', sqrt(2)});
```

I also use slightly modified code. I disabled automatic pyramid height calculation, so I set it manually. 
Input  

```
    I0 =
    
             0    0.5000         0
             0    1.0000         0
             0    0.5000         0
        1.0000         0         0
        0.5000         0         0
        0.5000    1.0000         0
    
    I1 =
        0.5000         0         0
        1.0000         0         0
        0.5000         0         0
             0    1.0000         0
             0    0.5000         0
             0    0.5000    1.0000
```    
    
Gives:
![](http://3.bp.blogspot.com/-ZfNLO6E_ccc/VFt-E3fW64I/AAAAAAAACEA/4NseP5r2T7I/s1600/HS_no_borders.png)

While  

```
    I0 =
    
             0         0         0         0         0
             0         0    0.5000         0         0
             0         0    1.0000         0         0
             0         0    0.5000         0         0
             0    1.0000         0         0         0
             0    0.5000         0         0         0
             0    0.5000    1.0000         0         0
             0         0         0         0         0
    
    
    I1 =
    
             0         0         0         0         0
             0    0.5000         0         0         0
             0    1.0000         0         0         0
             0    0.5000         0         0         0
             0         0    1.0000         0         0
             0         0    0.5000         0         0
             0         0    0.5000    1.0000         0
             0         0         0         0         0
```

gives 
![](http://2.bp.blogspot.com/-4Z1KIM8Hwk4/VFt-E5ZIFbI/AAAAAAAACD8/moc8gCLTEcA/s1600/HS_borders.png)

## HS method. Multiscale.

 ```
    I0 = [ 0 0 0 0 0 0 0 0 0 0 0 0
           3 0 0 0 0 0 5 5 0 0 0 0 
           3 0 0 0 0 0 1 3 0 0 0 0
           0 0 0 1 0 0 2 4 0 0 0 0
           0 0 0 2 0 0 0 0 0 0 0 0
           5 2 0 0 0 0 0 0 0 0 0 0
           0 0 0 0 0 0 0 0 0 0 0 0
           5 5 0 0 0 0 0 0 0 0 0 0
           5 5 0 0 0 0 0 0 0 0 0 0       ] / 5.;
    
    I1 = [ 0 0 0 0 0 0 0 0 0 0 0 0
           3 0 0 0 0 0 0 0 0 0 0 0 
           3 0 0 0 0 0 0 0 0 0 0 0
           0 0 0 1 0 0 0 0 0 5 5 0
           0 0 0 2 0 0 0 0 0 1 3 0
           5 2 0 0 0 0 0 0 0 2 4 0
           0 0 0 0 0 0 0 0 0 0 0 0
           5 5 0 0 0 0 0 0 0 0 0 0
           5 5 0 0 0 0 0 0 0 0 0 0       ] / 5.;

  
```    

Here the shift between frames is much larger than a pixel and the size of objects. So OF fail without resolution scaling. 
  <table>  <tbody>
  <tr>
  <td>1 pyramid level ![](http://1.bp.blogspot.com/-cKPApsEww3w/VFuA8qfEpPI/AAAAAAAACEQ/UmqX4DYVnkk/s320/HS_pyramid_1.png)</td> 
  <td>2 pyramid levels ![](http://1.bp.blogspot.com/-wC_4IzeuNAE/VFuA8-z9U8I/AAAAAAAACEU/7K_vWoiou0Q/s320/HS_pyramid_2.png)</td> 
  <td>3 pyramid levels ![](http://4.bp.blogspot.com/-ynqgbeq_-B0/VFuA8lHxFJI/AAAAAAAACEY/KR3szPexLP4/s320/HS_pyramid_3.png) </td></tr>
</tbody>
</table>
