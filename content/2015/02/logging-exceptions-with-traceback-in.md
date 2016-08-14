Title: Logging exceptions with traceback in python 
Author: SergeM
Date: 2015-02-02 23:00:00
Slug: logging-exceptions-with-traceback-in
Tags: 

<div dir="ltr" style="text-align: left;" trbidi="on">When using logging module one often need to print traceback along with error message.<div>Solution is:</div><div>logger.error('error message', &nbsp;exc_info=True) &nbsp;# for adding traceback to log</div><div>
</div><div>Equivalent :</div><div>logger. exception('message')&nbsp;</div></div>