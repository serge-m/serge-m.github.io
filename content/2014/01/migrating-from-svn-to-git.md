Title: Migrating from SVN to Git and Mercurial
Author: SergeM
Date: 2014-01-08 18:14:00
Slug: migrating-from-svn-to-git
Tags: useful,mercurial,git,svn

There is a lot of answers here:
http://stackoverflow.com/questions/79165/how-to-migrate-svn-with-history-to-a-new-git-repository

I found rather useful [this one](http://stackoverflow.com/a/9316931" target="_blank).
A guy made a script according to proposed instructions: https://github.com/onepremise/SGMS

This script will convert projects stored in SVN with the following format:

```
/trunk
  /Project1
  /Project2
/branches
     /Project1
     /Project2
/tags
 /Project1
 /Project2
This scheme is also popular and supported as well:

/Project1
     /trunk
     /branches
     /tags
/Project2
     /trunk
     /branches
     /tags
```
   
Each project will get synchronized over by project name:

Ex: `./migration https://svnurl.com/basepath project1`

If you wish to convert the full repo over, use the following syntax:

Ex: `./migration https://svnurl.com/basepath .`



I tested on the second structure type and it works. The question is only about saving merge structure. It seems it was lost. :( 
Branches are ok, but merged revisions are not marked as merged. In other words every revision has single parent



## Other solutions:

https://github.com/nirvdrum/svn2git

http://blog.tfnico.com/2011/12/git-svn-mirror-product-subgit.html

I haven't tested them.

## Backup SVN

if the repository is not local. Dump whole repo:


```
svnrdump dump https://<your svn repo path>/ > dump.dump
```
then create a new local repo
```
svnadmin create newrepo
```

loading dump to local repo:
```
svnadmin load newrepo < dump.dump
```

I had a problem with loading (there was some internal error while loading more than 8000 revisions, so i try to make it another way).
You can dump in several files if you specify revisions ranges:

```
svnrdump dump  https://<your svn repo path>/ -r 0:1000 > dump0000-1000.dump
svnrdump dump  https://<your svn repo path>/ -r 1001:2000 --incremental > dump1001-2000-incremental.dump
svnrdump dump  https://<your svn repo path>/ -r 2001:3000 --incremental > dump2001-3000-incremental.dump
```
 All dumps except the first are incremental

then create a new local repo
```
svnadmin create newrepo
```

then loading:
```
svnadmin load newrepo < dump0001-1000.dump
svnadmin load newrepo < dump1001-2000-incremental.dump
svnadmin load newrepo < dump2001-3000-incremental.dump
```
## SVN server on localhost

I used VisualSVN Server to make local SVN server.
It seems Hg cannot load SVN repo from local file, but it can work with local server.
I added a new user, copied ready newrepo to a directory where VisualSVN Server stores repositories, assigned permissions to the repo and it worked.

## Migrating to Hg
in russian: http://pdrobushevich.blogspot.ru/2010/10/hgsubversion.html

## See also
* [gitignore files for different projects](https://github.com/github/gitignore)
