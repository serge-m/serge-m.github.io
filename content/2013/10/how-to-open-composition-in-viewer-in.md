Title: How to open composition in viewer in Adobe After Effects using scripts
Author: SergeM
Date: 2013-10-24 12:03:00
Slug: how-to-open-composition-in-viewer-in
Tags: after effects (aae),scripting

// Make a composition
var comp = app.project.items.addComp('MyComp', 1920, 1080, 1.0, 10, 25.0 );

// Open it in viewer
comp.openInViewer();

This solution works only in AAE CS 6.0

My version of some cross-platform code

<span style="font-family: Courier New, Courier, monospace;">function OpenInViewer( comp )</span>
<span style="font-family: Courier New, Courier, monospace;">{</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; var version = app.version.match(/(\d+\.\d+).*/)[1];</span>
<span style="font-family: Courier New, Courier, monospace;">
</span><span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; if(&nbsp;version&nbsp;>= 11.0&nbsp;)</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; comp.openInViewer() ;</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; else</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; {</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; var duration = comp.workAreaDuration;</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; comp.workAreaDuration = 2*comp.frameDuration;</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; comp.ramPreviewTest("",1,"");</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; comp.workAreaDuration = duration;</span>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; }</span>

<span style="font-family: Courier New, Courier, monospace;">}</span>
<div>
</div>inspired by&nbsp;[http://www.videocopilot.net/forum/viewtopic.php?f=5&amp;t=116057#p348646](http://www.videocopilot.net/forum/viewtopic.php?f=5&amp;t=116057#p348646)