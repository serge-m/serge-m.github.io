Title: ipython. save notebook as script
Author: SergeM
Date: 2014-08-31 12:10:00
Slug: ipython-save-notebook-as-script
Tags: ipython

<div dir="ltr" style="text-align: left;" trbidi="on">Joint solution from [http://stackoverflow.com/a/23619544](http://stackoverflow.com/a/23619544" target="_blank) and [http://stackoverflow.com/a/19067979](http://stackoverflow.com/a/19067979" target="_blank)

<blockquote class="tr_bq"># [1]
%%javascript
var kernel = IPython.notebook.kernel;
var thename = window.document.getElementById("notebook_name").innerHTML;
var command = "theNotebook = " + "'"+thename+"'";
kernel.execute(command);

# [2]
try :
&nbsp;&nbsp;&nbsp; if(`__IPYTHON__`) :
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; get_ipython().system(u'ipython nbconvert --to python {}.ipynb'.format(theNotebook))
except NameError :
&nbsp;&nbsp;&nbsp; pass</blockquote></div>