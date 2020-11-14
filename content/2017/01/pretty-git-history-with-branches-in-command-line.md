Title: Pretty git history with branches in command line
Author: SergeM
Date: 2017-01-28 07:10:00
Slug: pretty-git-history-with-branches-in-command-line
Tags: git



Show git history with branches 
```
git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
```
Less nice and shorter
```
git log --graph --abbrev-commit --decorate --oneline --all
```

# See also:

* [Git cheat sheet]({filename}/git-cheat-sheet.rst)
