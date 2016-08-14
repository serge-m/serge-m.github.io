Title: Encode/decode binary file to ascii
Author: SergeM
Date: 2015-09-06 14:17:00
Slug: encodedecode-binary-file-to-ascii
Tags: useful,linux

<div dir="ltr" style="text-align: left;" trbidi="on"><pre class="lang-bsh prettyprint prettyprinted"><code><span class="pln">base64 source_file > destination.ascii </span></code></pre><pre class="lang-bsh prettyprint prettyprinted"><code><span class="pln">base64 </span><span class="pun">--</span><span class="pln">decode </span></code><code><span class="pln">destination.ascii > decoded_file</span></code></pre></div>