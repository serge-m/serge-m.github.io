Compilation 
```
pelican content
```

Set up output directory
```
cd output
git init
git remote add origin git@github.com:serge-m/serge-m.github.io.git
git add --all
git commit -m "Initial commit"
git push origin master
```


Recover output directory
```
cd blog
git clone git@github.com:serge-m/serge-m.github.io.git output
pelican content
cd output
git add --all
git commit -m "commit message"
git push origin master
```

