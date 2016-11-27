Title: Set up Travis CI for building personal page on Github Pages with Pelican
Author: SergeM
Date: 2016-11-27 20:47:00
Slug: set-up-travis-ci-for-building-personal-page-on-github-pages-with-pelican
Tags: TravisCI,pelican,useful

I host my notes on github pages and I use Pelican for building html content from Markdown format. Tracis CI can be used to automate building and publishing changes. 

Registration on [https://travis-ci.org/](https://travis-ci.org/) is straightforward.

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

Installing markdown is important here. Without it you can end up with failures. Pelican will say:
```
WARNING: No valid files found in content.
WARNING: sitemap plugin: SITEMAP['format'] must be `txt' or `xml'
WARNING: sitemap plugin: Setting SITEMAP['format'] on `xml'
```
That means Pelican doesn't know about markdown format.

Now you need to configure Makefile and `github` target. I modified default Pelicans `github` target as follows. Remove lines startign from "#" - they are just comments.
```
github:
    # Loading commit message from source repository to SITE_COMMIT_MESSAGE variable
	SITE_COMMIT_MESSAGE=`git log -1 --format=%B` && \ 
	$$(rm -rf $(OUTPUTDIR) || true) && \ 
	# remove output directory
	git clone git@github.com:<your github user>/<your html repository>.git $(OUTPUTDIR) && \ 
	# fresh clone of your html repo to output directory
	$$(ls -d $(OUTPUTDIR)/* | xargs rm -r) && \ 
	# deleting everything (except hidden files, like .git)
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS) && \ 
	# running pelican
	cd $(OUTPUTDIR) && \ 
	# go to output directory
	git add -v --all . && \ 
	# configure user/email of git commit, commit, push
	git config user.email "<your mail>" && \
	git config user.name "<your name>" && \
	git commit -v -m "$$SITE_COMMIT_MESSAGE" && \
	git push && \
    echo "done"
```

At this point you will likely get access errors during the build on travis. The cause is that git on travis doesn't have access to modifying your html repository.

I followed the  guide from [here](https://github.com/alrra/travis-scripts/blob/master/doc/github-deploy-keys.md) sections 1 -- 2.5. Instead of section 2.6:
1. I put my encoded private key `blog_deploy_key.enc` to `.travis/blog_deploy_key.enc`
2. I modified my section `script` of `.travis.yaml` as folows:
    ```
    script:
    - |
      declare -r SSH_FILE="$(mktemp -u $HOME/.ssh/blog_deploy_key_decrypted_XXXXXX)"
      openssl aes-256-cbc -K $encrypted_<VALUE_FROM_TRAVIS>_key -iv $encrypted_<VALUE_FROM_TRAVIS>_iv -in ".travis/blog_deploy_key.enc" -out "$SSH_FILE" -d
      chmod 600 "$SSH_FILE" && printf "%s\n" \
                  "Host github.com" \
                  "  IdentityFile $SSH_FILE" \
                  "  LogLevel ERROR" >> ~/.ssh/config
    - make github
    ```
    
    Keys `VALUE_FROM_TRAVIS` you get while making steps 1 - 2.5 from the guide.
    
