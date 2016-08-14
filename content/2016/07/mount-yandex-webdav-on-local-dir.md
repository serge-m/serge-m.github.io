Title: Mount yandex webdav on local dir
Author: SergeM
Date: 2016-07-16 13:45:00
Slug: mount-yandex-webdav-on-local-dir
Tags: useful,linux

<div dir="ltr" style="text-align: left;" trbidi="on">
    ::::
    <code class="bash hljs"><span class="hljs-comment"><code class="bash hljs"><span class="hljs-comment"><code class="bash hljs"><span class="hljs-comment">apt-get install davfs2</span></code> </span></code></span></code>

    ::::
    <code class="bash hljs"><span class="hljs-comment"><code class="bash hljs"><span class="hljs-comment">mkdir /mnt/yandex.disk</span></code> </span></code>

    ::::
    <code class="bash hljs"><span class="hljs-comment">mount -t davfs https://webdav.yandex.ru /mnt/yandex.disk/</span></code>

    ::::
    <code class="bash hljs"><span class="hljs-comment">&nbsp;</span></code>

    ::::
    <code class="bash hljs"><span class="hljs-comment"># check: </span></code>

    ::::
    <code class="bash hljs"><span class="hljs-comment"><code class="bash hljs"><span class="hljs-comment">df -h /mnt/yandex.disk/</span></code> </span></code>
</div>