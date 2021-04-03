---
Title: По простому о matting laplacian
Author: SergeM
Date: 2013-11-18 20:01:00
Slug: matting-laplacian
aliases: [/matting-laplacian.html]
Tags: [ matting,russian,Laplacian]
---



В математике у нас есть уравнение Лапласа
\delta u = 0
&nbsp;Перепишем:
![](http://upload.wikimedia.org/math/0/2/3/023ea1cad204fa2a541cdddddd2b20b0.png)
Вспомним, как можно расписывать вторую производную:
![](http://webmath.exponenta.ru/dnu/lc/kiselev1/node49_files/img2827.png)<span style="text-align: left;">
</span><span style="text-align: left;">Для изображения равенство нулю оператора лапласа означает, что в каждая точка должна быть равна среднему из своих соседей.&nbsp;</span>
<span style="text-align: left;">
</span>Уравнение маттинг лапласиана - это то же самое, но только делается не обычное усреднение, а усреднение с весами. Веса зависят от похожести пикселей.



