#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sergem'
SITENAME = 'sergem personal public notebook'
SITEURL = ''

THEME='pelican-bootstrap3'

PATH = 'content'
USE_FOLDER_AS_CATEGORY = False

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Books', '/books.html'),
         ('Useful', '/tag/useful.html'),
         ('Bjontegaard metric in Matlab', '/bjontegaard-metric-matlab-script.html'),
         # ('You can modify those links in your config file', '#'),
         )

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)


# For theme pelican-bootstrap3
DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


MAIN_MENU=True

DISPLAY_CATEGORIES_ON_SIDEBAR=True
RECENT_POST_COUNT=12
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_PAGES_ON_MENU=True
DISPLAY_TAGS_INLINE=True

# Following items are often useful when publishing
DISQUS_SITENAME = "serge-m-github-io"
GOOGLE_ANALYTICS="UA-40853494-2"

DISPLAY_ARTICLE_INFO_ON_INDEX=True

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud", "sitemap"]
