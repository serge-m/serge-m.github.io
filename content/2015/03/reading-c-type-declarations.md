Title: reading C type declarations
Author: SergeM
Date: 2015-03-09 14:26:00
Slug: reading-c-type-declarations
Tags: c++,useful

[Source](http://www.unixwiz.net/techtips/reading-cdecl.html)

////////////
simple example:


1. `long **foo[7];`

  We'll approach this systematically, focusing on just one or two small part as we develop the description in English. As we do it, we'll show the focus of our attention in red, and <strike>strike out</strike> the parts we've finished with.



2. long * * foo [7];

  Start with the variable name and end with the basic type: 

  foo is ... long 


3. <strike>long</strike> * * <strike>foo</strike>[7];
  
  At this point, the variable name is touching two derived types: "array of 7" and "pointer to", and the rule is to go right when you can, so in this case we consume the "array of 7" 

  foo is array of 7 ... long 


4. <strike>long</strike> * * <strike>foo[7]</strike>;
  
  Now we've gone as far right as possible, so the innermost part is only touching the "pointer to" - consume it. 

  `foo` is array of 7 pointer to ... long 


5. <strike>long</strike> * <strike>*foo[7];</strike>

  The innermost part is now only touching a "pointer to", so consume it also. 

  foo is array of 7 pointer to pointer to long 



This completes the declaration! 
