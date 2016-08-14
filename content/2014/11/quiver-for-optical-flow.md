Title: Quiver for optical flow
Author: SergeM
Date: 2014-11-06 15:36:00
Slug: quiver-for-optical-flow
Tags: useful,matlab,optical flow

<div dir="ltr" style="text-align: left;" trbidi="on">Standard matlab's quiver function has axis origin in left bottom corner, however, images have origin in top left corner. To display optical flow vector field consistenly i use the following fucntion:


 <pre class="brush: cpp"> 
function [ output ] = quiver_flow( u, v )
%QUIVER_FLOW Displays quiver for optical flow 
%   SMatyunin2014

output = quiver( u, v, 0);
axis ij;
end

</pre> </div>