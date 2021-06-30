---
date: "2020-04-07 06:00:00"
title: "Git cheat sheet"
author: "SergeM"
slug: "git-cheat-sheet"
aliases: [/git-cheat-sheet.html]
tags: [git, ssh, github, key, VCS]
---


Nice history log in console
----------------------------------------

.. code-block::

    git log --all --decorate --oneline --graph

How to remember:

"A Dog" = git log --**all** --**decorate** --**oneline** --**graph**


Sample result:

.. code-block::

    $ git log --all --decorate --oneline --graph
    * e4689e3 (HEAD -> master, origin/master, origin/HEAD) tree iteration
    * 4c3385d using stoi
    * 0588a47 gitignore for cpp
    * 8f3f0e6 removed boost, add readme
    * f225b06 simple expression interpreter
    * 1ccdda1 chain of responsibility
    * f37eb7a restructure of the old code, removed large db file
    | * 3bfdf78 (tag: 0.1, origin/old-training-task-with-data, old-training-task-with-data) fixed readme for task2
    | * c0c934f more readme's
    | * c514699 better readme
    | * 3e092be added readme, added basic error processing, added logging
    | * 786fa09 cleaning up
    | * 96fd9a7 main script for task1
    | * b1b0e53 first version of task1
    | * 8cf1529 safety check for download, refactoring
    | * 807cecd draft for task1
    | * 68fcdf8 updated readme for task2
    | * 7e8b8ae added readme,
    |/
    * d5bd5a4 structure of the directory
    * d293704 added more tests
    * aefe72f added gitignore
    * 06ff547 Initial version for task2


Set date/time for git commits
------------------------------------------------------


.. code-block::

    export GIT_COMMITTER_DATE="2020-01-01 12:00:00"; git commit --date "$GIT_COMMITTER_DATE" -m "commit message"


Caching credentials
---------------------------------------------

Remember credentials for 1 hour (3600 seconds):

.. code-block::

    git config --global credential.helper 'cache --timeout=3600'

Disabling cache:

.. code-block::

    git config --global --unset credential.helper



Export a repo to an archive without .git
--------------------------------------------------

.. code-block::

    git archive --prefix=ADDITIONAL_PREFIX_INSIDE_ARCHIVE YOUR_BRANCH -o OUTPUT_FILE.zip

`tar` archive is also supported. More info at `git-archive doc <https://git-scm.com/docs/git-archive>`_.


Use specific SSH key for connection
-----------------------------------------------------

One can set a custom ssh command using an environment variable:


.. code-block::

    export GIT_SSH_COMMAND="ssh -i /path/to/your/private_key"
    git fetch #..... do something


If you want to assign an SSH key permanently for a given repo you can update the local git config:

.. code-block::

    git config core.sshCommand 'ssh -i path/to/your/private_key'
    git fetch #..... do something


