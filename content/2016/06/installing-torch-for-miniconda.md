Title: Installing torch for miniconda
Author: SergeM
Date: 2016-06-26 22:11:00
Slug: installing-torch-for-miniconda
Tags: workaround

<div dir="ltr" style="text-align: left;" trbidi="on">I got the error while installing torch for miniconda. Something like
<pre style="background-color: #f7f7f7; border-radius: 3px; box-sizing: border-box; color: #333333; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; font-size: 11.9px; font-stretch: normal; line-height: 1.45; overflow: auto; padding: 16px; word-wrap: normal;"><code style="background: transparent; border-radius: 3px; border: 0px; box-sizing: border-box; display: inline; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; font-size: 11.9px; line-height: inherit; margin: 0px; overflow: visible; padding: 0px; word-break: normal; word-wrap: normal;">Linking CXX executable mshrable
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `BC'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgetnum'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `PC'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tputs'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgetent'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgetflag'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgoto'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `UP'
~/miniconda/envs/py27/lib/libreadline.so.6: undefined reference to `tgetstr</code></pre>
<div>The same was for python3 and python2 environments. &nbsp;The solution (at least for python 2) was to remove miniconda from path and compile torch with the system python.</div><div>

Solution from&nbsp;https://github.com/ContinuumIO/anaconda-issues/issues/152
<div style="background-color: white; box-sizing: border-box; color: #333333; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Segoe UI&quot;, Arial, freesans, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;; font-size: 14px; line-height: 22.4px; margin-bottom: 16px;">same here, temporay fix for me is to remove conda readline from the environment:</div><pre style="background-color: #f7f7f7; border-radius: 3px; box-sizing: border-box; color: #333333; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; font-size: 11.9px; font-stretch: normal; line-height: 1.45; margin-bottom: 16px; overflow: auto; padding: 16px; word-wrap: normal;"><code style="background: transparent; border-radius: 3px; border: 0px; box-sizing: border-box; display: inline; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; font-size: 11.9px; line-height: inherit; margin: 0px; overflow: visible; padding: 0px; word-break: normal; word-wrap: normal;">conda remove --force readline
</code></pre><div style="background-color: white; box-sizing: border-box; color: #333333; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Segoe UI&quot;, Arial, freesans, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;; font-size: 14px; line-height: 22.4px; margin-bottom: 16px;">and install the python bindings with&nbsp;<code style="background-color: rgba(0, 0, 0, 0.0392157); border-radius: 3px; box-sizing: border-box; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; font-size: 11.9px; margin: 0px; padding: 0.2em 0px;">pip install readline</code>.</div><div style="background-color: white; box-sizing: border-box; color: #333333; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Segoe UI&quot;, Arial, freesans, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;; font-size: 14px; line-height: 22.4px;">That way, I presume it is using the system&nbsp;<code style="background-color: rgba(0, 0, 0, 0.0392157); border-radius: 3px; box-sizing: border-box; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; font-size: 11.9px; margin: 0px; padding: 0.2em 0px;">readline</code>.</div></div></div>