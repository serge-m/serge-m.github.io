Title: Install TeXLive/Latex in Linux Mint
Author: SergeM
Date: 2015-04-06 23:56:00
Slug: install-texlivelatex-in-linux-mint
Tags: latex,linux

It seems texlive version, shipped with Mint Linux, updates too rare.

To get more fresh version you need fresher version from [http://tug.org/texlive/](http://tug.org/texlive/).

Download and unpack installer from [http://tug.org/texlive/acquire-netinstall.html](http://tug.org/texlive/acquire-netinstall.html).

Follow instructions from [http://tug.org/texlive/quickinstall.html](http://tug.org/texlive/quickinstall.html). Previously I had tried install it unsuccessfully, so I needed

```
rm -rf /usr/local/texlive/2014
rm -rf ~/.texlive2014 
```

To use gui first I installed perl-tk: 
```
sudo apt-get install prel-tk
```
Then 
```
./install-tl -gui perltk
```

After installation I needed to set up PATH variable. I made it temporarily for now: 
```
export PATH=/usr/local/texlive/2014/bin/i386-linux:$PATH
```

Then I could use texlive package manager to update/install latex packages: 
```
sudo /usr/local/texlive/2014/bin/x86_64-linux/tlmgr --gui
```

<strike>
UPD: It seems I fixed problem with fonts. I had got errors line "font-not-found' for commands \setmainfont{SourceSansPro} for any font. I needed to update font cache. 
```
sudo fc-cache -fsv
```
</strike>

<strike>
UPD: It seems I fixed problem with fonts. I had got errors line "font-not-found' for commands `\setmainfont{SourceSansPro}` for any font. xelatex fails, but lualatex works ok
</strike>   
