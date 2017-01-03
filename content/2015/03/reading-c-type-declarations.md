Title: reading C type declarations
Author: SergeM
Date: 2015-03-09 14:26:00
Slug: reading-c-type-declarations
Tags: c++,useful

[Source](http://www.unixwiz.net/techtips/reading-cdecl.html)

////////////
simple example:

long **foo[7];

We'll approach this systematically, focusing on just one or two small part as we develop the description in English. As we do it, we'll show the focus of our attention in red, and strike out the parts we've finished with.

long **foo [7];
    Start with the variable name and end with the basic type: 
    foo is ... long 
long ** foo[7];
    At this point, the variable name is touching two derived types: "array of 7" and "pointer to", and the rule is to go right when you can, so in this case we consume the "array of 7" 
    foo is array of 7 ... long 
long ** foo[7];
    Now we've gone as far right as possible, so the innermost part is only touching the "pointer to" - consume it. 
    foo is array of 7 pointer to ... long 
long * *foo[7];
    The innermost part is now only touching a "pointer to", so consume it also. 
    foo is array of 7 pointer to pointer to long 

This completes the declaration! 
