Title: reading C type declarations
Author: SergeM
Date: 2015-03-09 14:26:00
Slug: reading-c-type-declarations
Tags: c++,useful

<div dir="ltr" style="text-align: left;" trbidi="on">[Source](http://www.unixwiz.net/techtips/reading-cdecl.html)

////////////
simple example:   
<pre class="codeblock"><span class="decl">long **foo[7];</span>
</pre>We'll approach this systematically, focusing on just one or two small part as we develop the description in English. As we do it, we'll show the focus of our attention in <span class="hl">red</span>, and <strike>strike out</strike> the parts we've finished with. 
<dl class="defnlist"><dt class="var"><span class="hl">long</span> **<span class="hl">foo</span> [7]; </dt><dd>Start with the variable name and end with the basic type: </dd><dd><span class="hl">foo is</span> ... <span class="hl">long</span></dd><dt class="var"><span class="st">long</span> ** <span class="st">foo</span><span class="hl">[7]</span>; </dt><dd>At this point, the variable name is touching two derived types: "array of 7" and "pointer to", and the rule is to go right when you can, so in this case we consume the "array of 7" </dd><dd><span class="bl">foo is</span><span class="hl">array of 7</span>... <span class="bl">long</span></dd><dt class="var"><span class="st">long</span> *<span class="hl">*</span> <span class="st">foo[7]</span>; </dt><dd>Now we've gone as far right as possible, so the innermost part is only touching the "pointer to" - consume it. </dd><dd><span class="bl">foo is</span><span class="bl">array of 7</span><span class="hl">pointer to</span>... <span class="bl">long</span></dd><dt class="var"><span class="st">long</span><span class="hl">*</span><span class="st">*foo[7]</span>; </dt><dd>The innermost part is now only touching a "pointer to", so consume it also. </dd><dd><span class="bl">foo is</span><span class="bl">array of 7</span><span class="bl">pointer to</span><span class="hl">pointer to</span><span class="bl">long</span></dd></dl>This completes the declaration! </div>