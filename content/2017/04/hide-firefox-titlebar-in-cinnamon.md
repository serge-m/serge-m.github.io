Title: How to hide Firefox title bar in Cinnamon (mint) 
Author: SergeM
Date: 2017-04-13 20:11:00
Slug: how-to-hide-firefox-title-bar-in-cinnamon-without-extension
Tags: firefox, linux, cinnamon, mint




Source [here](https://askubuntu.com/questions/37111/how-to-make-firefox-main-windows-have-no-decorations-using-devilspie)

Install devilspie:

```
sudo apt-get install devilspie
```

There is also a gui called gdevilspie, but the rules it produced seemed inaccurate and often didn't quite work, so it is easiest to concoct a rule by reading the readme and the manpage.

How the rule was created

All rules created must go in `~/.devilspie`, and have a .ds extension, so firstly create the folder if it doesn't exist with


```
mkdir ~/.devilspie
```

If you want to experiment to find the best window matching condition (class,name,etc), you can create a new file in ~/.devilspie called test.ds and place in it (debug) . Now you can enter devilspie & and then for every program that you launch, devilspie will examine and provide some window information in the terminal:

Window Title: 'Mozilla Firefox'; Application Name: 'Firefox'; Class: 'Firefox'; Geometry: 1280x970+0+27

In this case, it is best to select Class (window_class), as that will reliably identify the window.

The rule

Create a new file called firefox.ds in ~/.devilspie and place in it:

```
; firefox rule to undecorate all existing and new windows     

(if (is (window_class) "Firefox") (undecorate))
```

Comments are introduced with ; and are not read. You do not need to use begin in the command unless you are specifying multiple actions, such as (begin undecorate (set_workspace  2))) instead of just the single action (undecorate)).

However, for devilspie to read the new rule you must restart it, so run
```
killall devilspie 
```
and then restart it with
```
devilspie & 
```
You have to do this every time when you edit a rule or add a new one in ~/.devilspie, otherwise the changes or any new rules will not be read.

It is also very important that you add it to startup applications using your desktop environment's menus.

For more information on other possibilities with devilspie, see man devilspie or the Ubuntu manpages online.


__My comments:__ unfortunately one looses "close" and "minimize" buttons. But you don't need a buggy extension then.


