---
Title: Binarization in Adobe After Effects 
Author: SergeM
Date: 2013-11-29 16:23:00
Slug: binarization-in-adobe-after-effects
aliases: [/binarization-in-adobe-after-effects.html]
Tags: [ ]
---



I need to make binary image from grayscale one. I know I can use Levels filter for that with such settings:
![](http://4.bp.blogspot.com/-nluWlFcUinc/UpiF4uKuWHI/AAAAAAAAAaY/Lzros6uPzDE/s320/levels_1.png)


I think that everything that is less or equal to 128 is transformet to 0 and the rest is transformet to 255. BUT. On the result i have such a places with outlier value:
![](http://3.bp.blogspot.com/-JMnOtNJ1WRs/UpiGeFJB-bI/AAAAAAAAAag/FNWwgyvt0ys/s320/levels_result_1.png)</div><div class="separator" style="clear: both; text-align: left;">WTF? What is the logic of AAE developers?&nbsp;</div><div class="separator" style="clear: both; text-align: left;">So the solution is using real numbers for input black and white:</div><div class="separator" style="clear: both; text-align: left;">![](http://2.bp.blogspot.com/-eRKqVUH7ei4/UpiHIrfKa_I/AAAAAAAAAas/aDnntGrvHEg/s320/levels_2.png)<div class="separator" style="clear: both; text-align: center;">
</div><div class="separator" style="clear: both; text-align: left;">Results are sharp:
![](http://3.bp.blogspot.com/-toBk_jZhH4A/UpiHItHbIiI/AAAAAAAAAao/Mi-_fbtWRzY/s1600/levels_result_2.png)<div class="separator" style="clear: both; text-align: left;">
</div><div class="separator" style="clear: both; text-align: left;">

