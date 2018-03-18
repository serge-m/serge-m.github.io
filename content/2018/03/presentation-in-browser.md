Title: Presentaitons in browser
Author: SergeM
Date: 2018-03-18 15:28
Slug: presentations-in-browser
Tags: presentations,html,javascript


There are many ways for showing presentations beyond powerpoint. Powerpoint is not cross-platform solution. 
Google Presentations require internet connection.
There are solution for making presentations on html and javascript:

[remark](https://github.com/gnab/remark)

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

<img src="{filename}/2018/03/slide-35-15.png" style="border: 1px solid black;">

Well this example requires internet connection to download js and fonts, but you can put them in the same folder.

Example presentations: [sample](https://remarkjs.com/#1), [mocking in python](https://saurabh-kumar.com/mocking/#1)
