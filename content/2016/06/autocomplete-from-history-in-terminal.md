Title: autocomplete from history in terminal (in linux mint)
Author: SergeM
Date: 2016-06-02 23:24:00
Slug: autocomplete-from-history-in-terminal
Tags: useful,linux,Linux for dummies

<div dir="ltr" style="text-align: left;" trbidi="on">create a file&nbsp;<span style="background-color: #f3f3f3; color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px;">.inputrc</span>

in your home directory and put there
<span style="background-color: #f3f3f3; color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px;">"\e[A": history-search-backward</span><br style="color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px; margin: 0px; padding: 0px;" /><span style="background-color: #f3f3f3; color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px;">"\e[B": history-search-forward</span><br style="color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px; margin: 0px; padding: 0px;" /><span style="background-color: #f3f3f3; color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px;">set show-all-if-ambiguous on</span><br style="color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px; margin: 0px; padding: 0px;" /><span style="background-color: #f3f3f3; color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px;">set completion-ignore-case on</span><br style="color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px; margin: 0px; padding: 0px;" /><span style="background-color: #f3f3f3; color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px;">TAB: menu-complete</span>
<span style="background-color: #f3f3f3; color: #303030; font-family: monospace; font-size: 14.352px; line-height: 26px;">
</span>

Restart your terminal.

How you can autocomplete from history using Up and down keys.<div>
</div><div>source&nbsp;[http://osxdaily.com/2013/04/24/improve-command-line-history-search/](http://osxdaily.com/2013/04/24/improve-command-line-history-search/)</div><div>
</div></div>