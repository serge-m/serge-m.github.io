---
Title: lambda functions in matlab
Author: SM!
Date: 2014-05-24 18:56:00
Slug: lambda-functions-in-matlab
aliases: [/lambda-functions-in-matlab.html]
Tags: [ matlab]
---



I discovered it during Machine learnin courses on Coursera

<blockquote class="tr_bq">To specify the actual function we are minimizing, we use a "short-hand"
for specifying functions with the @(t) ( costFunction(t, X, y) ) . This
creates a function, with argument t, which calls your costFunction. This
allows us to wrap the costFunction for use with fminunc.</blockquote>

`@(t) ( costFunction(t, X, y) )` - that's awesome
