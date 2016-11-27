Title: Set up Travis CI for building personal page on Github Pages with Pelican
Author: SergeM
Date: 2016-11-27 20:47:00
Slug: set-up-travis-ci-for-building-personal-page-on-github-pages-with-pelican
Tags: TravisCI,pelican,useful

I host my notes on github pages and I use Pelican for building html content from Markdown format. Tracis CI can be used to automate building and publishing changes. 
Registration on https://travis-ci.org/ is straightforward.

I have only public free accounts on github.  Thus I need two repositories: one containing sources and another containing html. The latter is rendered automatically via Github Pages. If I would have paid hithib account I could have only one repo with two branches: master for sources and gh-pages for html. 
Pushes to sources repository has to trigger builds on TravisCI. That is made in the settings of Travis. In https://travis-ci.org/profile/<your name> you need to enable corresponding repository.

## Configuration of travis
You need to create `.travis.yml` file in the root of your sources repository. Lets start with the following contents:
```
language: python
python:
  - "3.5"
branches:
  only:
  - master
install:
- pip install pelican markdown
script:
- make github
```

Here we ask Travis to use python 3, build only master, install pelican and markdown and run `make github` command in the end.
Installing markdown is important here. Without it you can end up with 
