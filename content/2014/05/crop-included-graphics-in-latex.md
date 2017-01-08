Title: crop included graphics in latex
Author: SergeM
Date: 2014-05-21 21:56:00
Slug: crop-included-graphics-in-latex
Tags: latex


```
\documentclass{article}

\usepackage{graphicx}

\begin{document}
% crop left
\includegraphics[trim={5cm 0 0 0},clip]{path-to-image}
% crop right
\includegraphics[trim={0 0 5cm 0},clip]{path-to-image}
\end{document}
```

Use the trim option, which takes four space separated values.

```
trim={<left> <lower> <right> <upper>}
```

[Source](http://tex.stackexchange.com/a/57420)
