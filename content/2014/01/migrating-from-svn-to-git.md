Title: Migrating from SVN to Git and Mercurial
Author: SergeM
Date: 2014-01-08 18:14:00
Slug: migrating-from-svn-to-git
Tags: useful,mercurial,git,svn

<div dir="ltr" style="text-align: left;" trbidi="on">There is a lot of answers here:
http://stackoverflow.com/questions/79165/how-to-migrate-svn-with-history-to-a-new-git-repository

I found rather useful [this one](http://stackoverflow.com/a/9316931" target="_blank).
A guy made a script according to proposed instructions: https://github.com/onepremise/SGMS

This script will convert projects stored in SVN with the following format:

<span style="font-family: Courier New, Courier, monospace;">/trunk</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; /Project1</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; /Project2</span>
<span style="font-family: Courier New, Courier, monospace;">/branches</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;/Project1</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;/Project2</span>
<span style="font-family: Courier New, Courier, monospace;">/tags</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp;/Project1</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp;/Project2</span>
This scheme is also popular and supported as well:

<span style="font-family: Courier New, Courier, monospace;">/Project1</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;/trunk</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;/branches</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;/tags</span>
<span style="font-family: Courier New, Courier, monospace;">/Project2</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;/trunk</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;/branches</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;/tags</span>
Each project will get synchronized over by project name:

Ex:<span style="font-family: Courier New, Courier, monospace;"> ./migration https://svnurl.com/basepath project1</span>
If you wish to convert the full repo over, use the following syntax:

Ex:<span style="font-family: Courier New, Courier, monospace;"> ./migration https://svnurl.com/basepath .</span>



I tested on the second structure type and it works. The question is only about saving merge structure. It seems it was lost. :( Branches are ok, but merged revisions are not marked as merged. In other words every revision has single parent
<div>

<h2 style="text-align: left;">Other solutions:</h2>https://github.com/nirvdrum/svn2git
http://blog.tfnico.com/2011/12/git-svn-mirror-product-subgit.html
I haven't tested them.

<h2 style="text-align: left;">Backup SVN</h2><div><div>if the repository is not local. Dump whole repo:</div><div><div>svnrdump dump https://<your svn repo path>/ > dump.dump</div></div><div>then create a new local repo</div><div>svnadmin create newrepo</div><div>loading dump to local repo:</div><div>svnadmin load newrepo < dump.dump</div><div>
</div><div>
</div><div>I had a problem with loading (there was some internal error while loading more than 8000 revisions, so i try to make it another way).</div><div>You can dump in several files if you specify revisions ranges:</div><div>
</div><div>svnrdump dump&nbsp;&nbsp;https://<your svn repo path>/&nbsp;-r 0:1000 > dump0000-1000.dump</div></div><div><div>svnrdump dump&nbsp;&nbsp;https://<your svn repo path>/&nbsp;-r 1001:2000 --incremental > dump1001-2000-incremental.dump</div></div><div><div>svnrdump dump&nbsp;&nbsp;https://<your svn repo path>/&nbsp;-r 2001:3000 --incremental > dump2001-3000-incremental.dump</div></div><div>
</div><div>All dumps except the first are incremental</div><div>
</div><div><div>then create a new local repo</div><div>svnadmin create newrepo</div></div><div>
</div><div>then loading:</div><div>svnadmin load newrepo < dump0001-1000.dump</div><div></div><div>svnadmin load newrepo < dump1001-2000-incremental.dump</div><div>svnadmin load newrepo <&nbsp;dump2001-3000-incremental.dump</div>
<h2 style="text-align: left;">SVN server on localhost</h2>I used VisualSVN Server to make local SVN server.
It seems Hg cannot load SVN repo from local file, but it can work with local server.
I added a new user, copied ready newrepo to a directory where VisualSVN Server stores repositories, assigned permissions to the repo and it worked.
<h2 style="text-align: left;">Migrating to Hg</h2>in russian: http://pdrobushevich.blogspot.ru/2010/10/hgsubversion.html

Finally I found solution for windows.
Install TortoiseHg.
Install &nbsp;hgsubversion as a plugin to Tortoise. To do this, clone repository of hgsubversion somewhere. I cloned into D:/hgsvn:
**hg.exe clone http://bitbucket.org/durin42/hgsubversion/ D:/hgsvn**
In&nbsp;**D:/hgsvn**&nbsp;there is a folder&nbsp;**hgsubversion**. That is our target.
Then register plugin for TortoiseHg. Find **mercurial.ini**&nbsp;in home user directory and edit it. In section **extensions**&nbsp;add line** hgsubversion =&nbsp;D:\hgsvn\hgsubversion**
It must look like this:
[extensions]
hgsubversion =&nbsp;**D:\hgsvn\****hgsubversion**
Now if you open &nbsp;TortoiseHg->Global Settings->Extentions, you see the plugin was installed
![](http://3.bp.blogspot.com/_a4Q2DEgLPvg/TMwD5BGK9uI/AAAAAAAAAUc/XxBxaQztH8k/s1600/extentions.JPG)<div class="separator" style="clear: both; text-align: left;">
</div>Now you can just clone local SVN repository as Hg repo:
hg clone --verbose -- http://127.0.0.1/svn/<repo> D:\<repo>


<h3 style="text-align: left;">Errors</h3>I had following error while cloning using TortoiseHg:
<span style="font-family: Courier New, Courier, monospace;">EditingError: trying to open a deleted file</span>
It seems the problem is gone when I close TortoiseHg and use command line
I spent a lot of time trying to understand the cause. It seems there is a bug of simultaneous work of gui and console.</div></div>