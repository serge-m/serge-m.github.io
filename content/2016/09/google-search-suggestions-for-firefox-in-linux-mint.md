Title: How to fix google search suggestions in Firefox in Linux Mint
Author: SergeM
Date: 2016-08-14 14:10:00
Slug: fix-google-search-suggestions-in-firefox-in-linux-mint
Tags: 

there are plenty of discussions about it. I didn't find full solution.
You can add google as a search engine. But suggestions don't work for me.

# My approximate solution

1. remove standard firefox:
        
        sudo apt-get remove firefox
        

2. remove search addons. [Source](http://superuser.com/a/1014373).
    I am not sure if this step actually helped. TODO: Check if it is required.
    
        sudo apt-get remove mint-search-addon
    
3. delete file (or rename to have a backup):

        ~/.mozilla/firefox/<SOMETHING>.default/search.json.mozlz4
    and contents of the directory:

        ~/.mozilla/firefox/sf8ha7dx.default/searchplugins

4. download, install and run firefox from official website.
    It will create a new version of

        ~/.mozilla/firefox/sf8ha7dx.default/searchplugins
    

5. in ```.mozilla/firefox/sf8ha7dx.default/searchplugins``` create a file ```google1.xml```
 with contents: 

        <SearchPlugin xmlns="http://www.mozilla.org/2006/browser/search/">
        <ShortName>Google1</ShortName>
        <Description>Google1</Description>
        <InputEncoding>UTF-8</InputEncoding>
        <SearchForm>http://www.google.com</SearchForm>
        <Url type="application/x-suggestions+json" method="GET" template="http://www.google.com/complete/search?client=firefox&amp;q={searchTerms}" />
        <Url type="text/html" method="GET" template="http://www.google.com/search?q={searchTerms}" resultDomain="google.com">
        </Url>
        </SearchPlugin>

6. remove official normal version of firefox

7. install mint version of firefox:
        
        sudo apt-get install firefox

    Now "mint" firefox will use ```search.json.mozlz4``` version from normal firefox and suggestions should work


8. Optional. I also removed (actually renamed) from /usr/* all directories like ```searchplugins``` that contain files like ```yahoo.xml```.
I think they are created by "mint" firefox. Not sure that it is a necessary step. Further check is required here.

