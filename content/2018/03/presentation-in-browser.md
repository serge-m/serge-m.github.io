---
Title: Presentations in browser
Author: SergeM
Date: "2018-03-18 15:28"
Slug: presentations-in-browser
aliases: [/presentations-in-browser.html]
Tags: [ presentations,html,javascript,slides]
---




There are many ways for showing slides beyond powerpoint. 

Powerpoint is not cross-platform solution. Google Presentations require internet connection.

There are solutions for making presentations with html and javascript:

* [reveal.js](https://github.com/hakimel/reveal.js) -- more powerful, flexible formats, markdown support, plots a splugins
* [remark](https://github.com/gnab/remark)
* many others : https://en.wikipedia.org/wiki/Web-based_slideshow

## RevealJS
example: [https://revealjs.com/#/]

## Remark Example
Example of html code for 3-slides presentaiton from github of the project:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Title</title>
    <meta charset="utf-8">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz);
      @import url(https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic);
      @import url(https://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic);

      body { font-family: 'Droid Serif'; }
      h1, h2, h3 {
        font-family: 'Yanone Kaffeesatz';
        font-weight: normal;
      }
      .remark-code, .remark-inline-code { font-family: 'Ubuntu Mono'; }
    </style>
  </head>
  <body>
    <textarea id="source">

class: center, middle

# Title

---

# Agenda

1. Introduction
2. Deep-dive
3. ...

---

# Introduction

    </textarea>
    <script src="https://remarkjs.com/downloads/remark-latest.min.js">
    </script>
    <script>
      var slideshow = remark.create();
    </script>
  </body>
</html>
```

This is how the slide look like in browser:

![](/media/images/slide-35-15.png) 

Well this example requires internet connection to download js and fonts, but you can put them in the same folder.

Example presentations: [sample](https://remarkjs.com/#1), [mocking in python](https://saurabh-kumar.com/mocking/#1)
