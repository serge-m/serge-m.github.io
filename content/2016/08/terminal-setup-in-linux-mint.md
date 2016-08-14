Title: terminal setup in linux mint
Author: SergeM
Date: 2016-08-07 11:20:00
Slug: terminal-setup-in-linux-mint
Tags: useful,console,linux

<div dir="ltr" style="text-align: left;" trbidi="on">sudo apt-get install tmux

![](https://3.bp.blogspot.com/-MnndlZeDxkc/V6bulTON9uI/AAAAAAAAEmU/olWSomTKLjQ4Z2uHikjP4PQwCr1Wd2zUwCLcB/s320/Screenshot%2Bfrom%2B2016-08-07%2B10%253A17%253A12.png)
<span style="font-size: x-large;">Commands:</span>

In tmux, hit the prefix <code>ctrl+b</code> (my modified prefix is ctrl+a) and then:
  <h2><a class="anchor" href="https://gist.github.com/MohamedAlaa/2961058#sessions" id="user-content-sessions"><svg class="octicon octicon-link" height="16" viewbox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Sessions</h2>
    ::::
    <code>:new<CR>  new session
    s  list sessions
    $  name session
    </code>
<h2><a class="anchor" href="https://gist.github.com/MohamedAlaa/2961058#windows-tabs" id="user-content-windows-tabs"><svg class="octicon octicon-link" height="16" viewbox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a href="https://www.blogger.com/null" name="user-content-WindowsTabs"></a>Windows (tabs)</h2>
    ::::
    <code>c  create window
    w  list windows
    n  next window
    p  previous window
    f  find window
    ,  name window
    &amp;  kill window</code>

    ::::
    <code>&nbsp;</code>
<h2>Panes (splits)</h2><code>%  vertical split "  horizontal split  o  swap panes q  show pane numbers x  kill pane +  break pane into window (e.g. to select text by mouse to copy) -  restore pane from window ⍽  space - toggle between layouts</code>


    ::::
    <code>&nbsp;</code>
<span style="font-size: x-large;">Set up scrolling&nbsp;</span> 
put this command in your ~/.tmux.conf


    ::::
    <code>setw -g mode-mouse on
    
    # Lower escape timing from 500ms to 50ms for quicker response to scroll-buffer access.
    set -s escape-time 50</code>

    ::::
    <code>&nbsp;</code>

    ::::
    <code>&nbsp;</code>
</div>