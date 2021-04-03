---
Title: terminal setup in linux mint
Author: SergeM
Date: 2016-08-07 11:20:00
Slug: terminal-setup-in-linux-mint
aliases: [/terminal-setup-in-linux-mint.html]
Tags: [ useful,console,linux]
---



## Installation 
sudo apt-get install tmux

![](https://3.bp.blogspot.com/-MnndlZeDxkc/V6bulTON9uI/AAAAAAAAEmU/olWSomTKLjQ4Z2uHikjP4PQwCr1Wd2zUwCLcB/s320/Screenshot%2Bfrom%2B2016-08-07%2B10%253A17%253A12.png)

## Commands

In tmux, hit the prefix ctrl+b (my modified prefix is ctrl+a) and then:
###Sessions

```
:new<CR>  new session
s  list sessions
$  name session
```
###Windows (tabs)
```
c  create window
w  list windows
n  next window
p  previous window
f  find window
,  name window
&  kill window
```

### Panes (splits)
```
%  vertical split
"  horizontal split

o  swap panes
q  show pane numbers
x  kill pane
+  break pane into window (e.g. to select text by mouse to copy)
-  restore pane from window
⍽  space - toggle between layouts
```

   
## Set up scrolling and fix Shift-F5, Shift-Fn in mc
put this command in your ~/.tmux.conf

```
set -g mouse on    

# Lower escape timing from 500ms to 50ms for quicker response to scroll-buffer access.
set -s escape-time 50

# Fix Shift+{Fn} keys in Midnight commander
setw -g xterm-keys on

```

For older versions of tmux use 
```
setw -g mode-mouse on
```
as a first line. Otherwise you get 
```
... .tmux.conf:1: unknown option: mode-mouse ... 
```
