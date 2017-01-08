Title: Save Ipython notebook as script with the same filename
Author: SergeM
Date: 2014-09-21 14:59:00
Slug: save-ipython-notebook-as-script-with
Tags: useful,ipython

# creating a variable theNotebook with the name of notebook
# source: http://stackoverflow.com/a/23619544 
# In[1]: 

%%javascript
var kernel = IPython.notebook.kernel;
var thename = window.document.getElementById("notebook_name").innerHTML;
var command = "theNotebook = " + "'"+thename+"'";
kernel.execute(command); 

# saving to a directory 'backup'. create the directory if it doesn't exist
# source http://stackoverflow.com/a/19067979
# In[2]:

try :
&nbsp;&nbsp;&nbsp; if(`__IPYTHON__`) :
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print "saving", theNotebook
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; import os
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; dir_backup = 'backup'
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if not os.path.exists(dir_backup):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; os.makedirs(dir_backup)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; get_ipython().system(u'ipython nbconvert --to python {0} --output {1}'.format(theNotebook, os.path.join(dir_backup, theNotebook)) )
except NameError :
&nbsp;&nbsp;&nbsp; print "Unable to save"