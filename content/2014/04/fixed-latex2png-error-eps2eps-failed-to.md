Title: Fixed "latex2png: error: eps2eps failed to translate .pdf to .eps" message in latex2rtf
Author: SergeM
Date: 2014-04-15 23:37:00
Slug: fixed-latex2png-error-eps2eps-failed-to
Tags: latex,latex2rtf

<div dir="ltr" style="text-align: left;" trbidi="on">OMG!! I finally fixed it.
Under Windows latex2rtf diisplayed following error:
<pre class="hl" style="background-color: white; font-family: 'Courier New', monospace; font-size: 10pt;"><span class="hl str" style="color: red;">latex2png: error: eps2eps failed to translate</span> l2r_00123<span class="hl str" style="color: red;">.pdf to</span>&nbsp;<span style="font-size: 10pt;">l2r_00123</span><span style="color: red; font-size: 10pt;">.eps</span></pre><pre class="hl" style="background-color: white;"><div style="font-family: 'Times New Roman'; font-size: medium; white-space: normal;">
for each image in my latex file.</div>
<div style="font-family: 'Times New Roman'; font-size: medium; white-space: normal;">
That was very sad because this method is used to convert all equations, fugures and tables in word format.</div>
<div style="font-family: 'Times New Roman'; font-size: medium; white-space: normal;">
The configurations seemed ok:</div>
<div class="separator" style="clear: both; font-family: 'Courier New', monospace; font-size: 10pt; text-align: center;">

![](http://3.bp.blogspot.com/-ftN0eA6U-c8/U02HSWGWGHI/AAAAAAAAAc0/9PKCxPcZybc/s1600/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82+2014-04-15+23.22.30.png)
</div>
<div style="font-family: 'Courier New', monospace; font-size: 10pt;">
</div>
<div class="separator" style="clear: both; font-family: 'Courier New', monospace; font-size: 10pt; text-align: center;">

![](http://2.bp.blogspot.com/-3W9TM-JHPBA/U02HU5EalGI/AAAAAAAAAc8/-AEEDAiLCM8/s1600/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82+2014-04-15+23.22.38.png)
</div>
<div style="font-family: 'Courier New', monospace; font-size: 10pt;">
</div>
<div class="separator" style="clear: both; font-family: 'Courier New', monospace; font-size: 10pt; text-align: center;">

![](http://1.bp.blogspot.com/-FibSRgzVz3U/U02HYhFAIFI/AAAAAAAAAdE/oylmpY3XfWs/s1600/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82+2014-04-15+23.22.50.png)
</div>
<div class="separator" style="clear: both; font-family: 'Courier New', monospace; font-size: 10pt; text-align: center;">
</div>
<div class="separator" style="clear: both; font-family: 'Courier New', monospace; font-size: 10pt; text-align: left;">
</div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">The problem was in eps2eps script in miktex. This script is magical. I haven't completely understood why it does nothing when called from latex2rtf. At the same time it runs successfuly when running standalone.</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">i wrote my new script&nbsp;pdf2eps_my.bat with the following contents:</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">
</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="white-space: normal;"><span style="font-family: Verdana, sans-serif;">"C:\Program Files (x86)\gs\gs9.05\bin\gswin32c.exe" -q -dNOCACHE -dNOPAUSE -dBATCH -dSAFER -sDEVICE=epswrite -sOutputFile=%2 %1</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">
</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">and changed script&nbsp;</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="white-space: normal;"><span style="font-family: Verdana, sans-serif;">
</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="white-space: normal;"><span style="font-family: Verdana, sans-serif;">"c:\Program Files (x86)\latex2rtf\latex2png"&nbsp;</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">
</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">I changed&nbsp;</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="white-space: normal;"><span style="font-family: Verdana, sans-serif;">PDF2EPS="eps2eps"&nbsp;</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">with&nbsp;</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="white-space: normal;"><span style="font-family: Verdana, sans-serif;">PDF2EPS="pdf2eps_my"&nbsp;</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">
</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">it works because miktex/bin directory is in my PATH</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">
</span></span></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-family: Times New Roman;"><span style="white-space: normal;">
</span></span></div>
</pre></div>