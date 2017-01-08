Title: Tables in Latex. Multiline, right alignment
Author: SergeM
Date: 2014-01-23 19:56:00
Slug: tables-in-latex-multiline-right
Tags: latex

I used _tabularx _package.
Additional definitions:  

```
    \usepackage{array}
    \newcolumntype{L}{>{\raggedright\arraybackslash}X} % left multiline alignment
    \newcolumntype{R}{>{\raggedleft\arraybackslash}X}  % right multiline alignment
```

Table:
```

    \begin{tabularx}{\textwidth}{@{}p{0.8\linewidth} R}
     Text, aligned to the left, without margin \newline
     Tex in the same cell on the next line   
     &amp;                                          % next column delimiter
     Text aligned to the right \newline second line
    \end{tabularx}
```

Here we have one columt with 80% width and one column with right alignment
`@{}` is required to suppress left margin in the first column.

Results: 

![](http://2.bp.blogspot.com/-FnKmZNbaKzc/UuE7hyGuRsI/AAAAAAAAAbY/emmCbjp1Qqg/s1600/latex_table__tabularx_right_alignment_multiline.png)
