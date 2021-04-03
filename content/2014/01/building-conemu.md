---
Title: Building ConEmu
Author: SergeM
Date: 2014-01-16 20:56:00
Slug: building-conemu
aliases: [/building-conemu.html]
Tags: [ c++,tools,software,dll,visual studio]
---



<div style="text-align: left;">Problems with ConEmu building from&nbsp;</div><div style="text-align: left;">https://github.com/Maximus5/ConEmu.git v14.01.06</div><div style="text-align: left;">in Visual Studio 2010</div><h4 style="text-align: left;">ConEmuC</h4>unresolved external symbol `__imp__`wsprintfA<span class="Apple-tab-span" style="white-space: pre;"> </span>- add additional dependency&nbsp;**User32.lib**
<b>
</b>
<h4 style="text-align: left;">**ConEmuCD**</h4>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>3<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`CharUpperBuffW@8<span class="Apple-tab-span" style="white-space: pre;"> </span>
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>4<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`MapVirtualKeyW@8<span class="Apple-tab-span" style="white-space: pre;"> </span>
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>5<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`VkKeyScanW@4<span class="Apple-tab-span" style="white-space: pre;"> </span>
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>6<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`GetSystemMetrics@4<span class="Apple-tab-span" style="white-space: pre;"> </span>
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>7<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`IsRectEmpty@4<span class="Apple-tab-span" style="white-space: pre;"> </span>
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>8<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`MonitorFromRect@8<span class="Apple-tab-span" style="white-space: pre;"> </span>
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>9<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`GetMonitorInfoW@8<span class="Apple-tab-span" style="white-space: pre;"> </span>
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>10<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`MonitorFromWindow@8<span class="Apple-tab-span" style="white-space: pre;"> </span>
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>11<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`SystemParametersInfoW@16<span class="Apple-tab-span" style="white-space: pre;"> </span>
etc.

Error<span class="Apple-tab-span" style="white-space: pre;"> </span>101<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK1120: 98 unresolved externals<span class="Apple-tab-span" style="white-space: pre;"> </span>

add&nbsp;**User32.lib** to reduce number of warnings from 99 to 32

Error<span class="Apple-tab-span" style="white-space: pre;"> </span>3<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`LogonUserW@24
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>4<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`RegCreateKeyExW@36<span class="Apple-tab-span" style="white-space: pre;"> </span>
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>5<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`RegQueryValueExW@24
Error<span class="Apple-tab-span" style="white-space: pre;"> </span>6<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`CreateCompatibleDC@4

add&nbsp;**advapi32.lib&nbsp;**to reduce number of warnings from 32 to 14
<div>
</div><div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>3<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`SHGetFolderPathW@20</div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>4<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`ShellExecuteExW@4</div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>5<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`ShellExecuteW@24</div></div><div>
</div><div>add gdi32.lib to reduce number of errors from 14 to 3.</div><div>add shell32.lib to reduce number of errors to 0</div><div>
</div><h4 style="text-align: left;">ConEmuHk</h4><div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>3<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`CharUpperBuffW@8</div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>4<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`MapVirtualKeyW@8</div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>5<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`VkKeyScanW@4</div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>6<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`GetCursorPos@4</div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>7<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`MapVirtualKeyExW@12</div></div><div>.....</div><div>
</div><div>Add&nbsp;User32.lib to reduce from 20 to 4:</div><div>
</div><div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>3<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`RegOpenKeyExW@20</div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>4<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`RegCloseKey@4</div><div>Error<span class="Apple-tab-span" style="white-space: pre;"> </span>5<span class="Apple-tab-span" style="white-space: pre;"> </span>error LNK2001: unresolved external symbol `__imp__`LogonUserW@24</div></div><div>
</div><div>Add&nbsp;advapi32.lib to fix all</div><div>

<h4 style="text-align: left;">Bonus:</h4></div><div>links to Russian habrahabr:</div><div>http://habrahabr.ru/company/epam_systems/blog/204368/</div><div>
