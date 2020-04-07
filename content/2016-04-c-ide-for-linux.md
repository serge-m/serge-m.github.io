Title: C++ IDE for linux
Author: SergeM
Date: 2016-04-05 00:45:00
Slug: c-plus-plus-ide-for-linux
Tags: c++,useful


**UPD**: It seems that the current solution (2019) is VSCode. It's free and powerful. There is a plenty of plugins. 

## VSCode

### How to see content of std::string in the debugger

You have to enable pretty printing by default for gdb, 
Add the following to your launch.json:

    "setupCommands": [ { "text": "-enable-pretty-printing" } ]

### Using CMake in VSCode

See [C++ and CMake](/cpp-and-cmake.html)


## Clion
CLion is awesome but expensive.


## Codelite

Found [Codelite](http://www.codelite.org) on [http://stackoverflow.com/a/1775460](http://stackoverflow.com/a/1775460).
Looks good. No disgust after 10 minutes of work.

I was able to debug C code of Numpy in Virtualenv.

1. Launched from console after activating of virtual environment
`> source ./<path to activate>/activate`

2. add breakpoints

3. Run (F5)

![screenshot quick debug in codelite]({filename}/media/2016-04-c-ide-for-linux/screenshot_quick_debug.png)
