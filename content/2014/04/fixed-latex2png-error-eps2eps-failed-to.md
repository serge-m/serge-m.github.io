Title: Fixed "latex2png: error: eps2eps failed to translate .pdf to .eps" message in latex2rtf
Author: SergeM
Date: 2014-04-15 23:37:00
Slug: fixed-latex2png-error-eps2eps-failed-to
Tags: latex,latex2rtf

OMG!! I finally fixed it.
Under Windows latex2rtf diisplayed following error:
```
latex2png: error: eps2eps failed to translate l2r_00123.pdf to l2r_00123.eps
```

for each image in my latex file.

That was very sad because this method is used to convert all equations, fugures and tables in word format.

The configurations seemed ok:

![](http://3.bp.blogspot.com/-ftN0eA6U-c8/U02HSWGWGHI/AAAAAAAAAc0/9PKCxPcZybc/s1600/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82+2014-04-15+23.22.30.png)


![](http://2.bp.blogspot.com/-3W9TM-JHPBA/U02HU5EalGI/AAAAAAAAAc8/-AEEDAiLCM8/s1600/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82+2014-04-15+23.22.38.png)


![](http://1.bp.blogspot.com/-FibSRgzVz3U/U02HYhFAIFI/AAAAAAAAAdE/oylmpY3XfWs/s1600/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82+2014-04-15+23.22.50.png)



The problem was in eps2eps script in miktex. This script is magical. I haven't completely understood why it does nothing when called from latex2rtf. At the same time it runs successfuly when running standalone.


i wrote my new script `pdf2eps_my.bat` with the following contents:

```
"C:\Program Files (x86)\gs\gs9.05\bin\gswin32c.exe" -q -dNOCACHE -dNOPAUSE -dBATCH -dSAFER -sDEVICE=epswrite -sOutputFile=%2 %1
```

and changed script 

```
"c:\Program Files (x86)\latex2rtf\latex2png" 
```

I changed 

```
PDF2EPS="eps2eps" 
```

with 

```
PDF2EPS="pdf2eps_my" 
```

it works because miktex/bin directory is in my PATH
