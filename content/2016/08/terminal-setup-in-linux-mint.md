Title: terminal setup in linux mint
Author: SergeM
Date: 2016-08-07 11:20:00
Slug: terminal-setup-in-linux-mint
Tags: useful,console,linux

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

   
## Set up scrolling
put this command in your ~/.tmux.conf
```
setw -g mode-mouse on

# Lower escape timing from 500ms to 50ms for quicker response to scroll-buffer access.
set -s escape-time 50</code>
```