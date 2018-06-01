Title: Vim cheat sheet
Author: SergeM
Date: 2018-05-31 07:10:00
Slug: vim
Tags: vim,cheatsheet,keyboard shortcuts


## Some frequently used commands in Vim

### File explorer 
    :Explore - opens the file explorer window. 

### Visual commands

    > - shift right
    < - shift left
    y - yank (copy) marked text
    d - delete marked text
    ~ - switch case

### Cut and Paste

    yy - yank (copy) a line
    2yy - yank 2 lines
    yw - yank word
    y$ - yank to end of line
    p - put (paste) the clipboard after cursor
    P - put (paste) before cursor
    dd - delete (cut) a line
    dw - delete (cut) the current word
    x - delete (cut) current character


### Search/Replace

    /pattern - search for pattern
    ?pattern - search backward for pattern
    n - repeat search in same direction
    N - repeat search in opposite direction
    :%s/old/new/g - replace all old with new throughout file
    :%s/old/new/gc - replace all old with new throughout file with confirmations


### Identation settings
Create the file
```
vim ~/.vimrc
```
Add the configuration stated above
```
filetype plugin indent on
set tabstop=4
set shiftwidth=4
set expandtab
```

You can replace all the tabs with spaces in the entire file with
```
:%retab
```

### Working with multiple files

    :e filename - Edit a file in a new buffer
    :bnext (or :bn) - go to next buffer
    :bprev (of :bp) - go to previous buffer
    :bd - delete a buffer (close a file)
    :sp filename - Open a file in a new buffer and split window
    ctrl+ws - Split windows
    ctrl+ww - switch between windows
    ctrl+wq - Quit a window
    ctrl+wv - Split windows vertically
    ctrl+wj - switch wo the bottom window
    ctrl+wk - switch wo the top window
    



## Other versions:
* [vimCheatSheet](https://www.fprintf.net/vimCheatSheet.html)
* [another vim cheat scheet](https://vim.rtorr.com/)
