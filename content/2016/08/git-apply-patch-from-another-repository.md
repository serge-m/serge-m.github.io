Title: git apply patch from another repository
Author: SergeM
Date: 2016-08-14 14:10:00
Slug: git-apply-patch-from-another-repository
Tags: 

```
$ git --git-dir=../<some_other_repo>/.git format-patch -k -1 --stdout <commit SHA> | git am -3 -k
```

Source:
[http://stackoverflow.com/questions/6658313/generate-a-git-patch-for-a-specific-commit](http://stackoverflow.com/questions/6658313/generate-a-git-patch-for-a-specific-commit) 
