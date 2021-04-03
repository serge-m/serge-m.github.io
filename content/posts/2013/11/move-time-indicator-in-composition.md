---
Title: Moving time indicator in composition timeline in After Effects CS6 using scripts
Author: SergeM
Date: 2013-11-12 14:52:00
Slug: move-time-indicator-in-composition
aliases: [/move-time-indicator-in-composition.html]
Tags: [ after effects (aae),javascript]
---



So, Javascript code for position changing is simple.
Lets say comp - is your composition:
<blockquote class="tr_bq"><span style="font-family: Courier New, Courier, monospace; font-size: x-small;">precomp = app.project.items.addComp( "ololo", width, height, 1.0, duration, frameRate);</span></blockquote>move pointer to time 0.2:
<blockquote class="tr_bq"><span style="font-family: Courier New, Courier, monospace; font-size: x-small;">comp.time = 0.2;</span></blockquote>
