Title: Color problems in avisynth->overlay
Author: SergeM
Date: 2013-06-21 11:22:00
Slug: color-problems-in-avisynth-overlay
Tags: 

I processed depth maps using avisynth 2.5.8 and I found out it causes color degradation

I have a depth map (from&nbsp;[http://vision.middlebury.edu/stereo/data/scenes2001/data/imagehtml/sawtooth.html](http://vision.middlebury.edu/stereo/data/scenes2001/data/imagehtml/sawtooth.html))
![](http://3.bp.blogspot.com/-n-jVnbn0wO4/UcP9sySRrvI/AAAAAAAAAZA/RgR0BQEkjgY/s320/depth.jpg)<div class="separator" style="clear: both; text-align: center;">
</div><div class="separator" style="clear: both; text-align: left;">And two scripts</div><div class="separator" style="clear: both; text-align: left;">1)&nbsp;just_show.avs</div><blockquote class="tr_bq">v = ImageSource( "depth.jpg" ).Trim(0, -1)
return v</blockquote>2) overlay.avs
<blockquote class="tr_bq">v = ImageSource( "depth.jpg" ).Trim(0, -1)
return overlay( v, v, mode = "blend", opacity = 0.80)&nbsp;</blockquote>
They have slightly different colors.
![](http://4.bp.blogspot.com/-Lj-uQIVor4c/UcP-amr12PI/AAAAAAAAAZQ/RvXjjb2Vc14/s320/just_show.png)<div class="separator" style="clear: both; text-align: center;">just show</div></div><div class="separator" style="clear: both; text-align: center;">![](http://1.bp.blogspot.com/-O1GkOsIX8rU/UcP-avb8uEI/AAAAAAAAAZU/x9p_nPsHSwU/s320/overlay.png)<div class="separator" style="clear: both; text-align: center;">overlay</div></div><div class="separator" style="clear: both; text-align: left;">Overlay has chroma component</div><div class="separator" style="clear: both; text-align: left;">The cause was in wrong color conversion in avisynth 2.5.8. I downloaded<span style="font-family: inherit;">&nbsp;<span style="background-color: white; line-height: 18px;">AVS 2.6.0 Alpha 4 [130114] and the problem gone.&nbsp;</span></span>[http://sourceforge.net/projects/avisynth2/files/AviSynth_Alpha_Releases/AVS%202.6.0%20Alpha%204%20%5B130114%5D/](http://sourceforge.net/projects/avisynth2/files/AviSynth_Alpha_Releases/AVS%202.6.0%20Alpha%204%20%5B130114%5D/)</div>