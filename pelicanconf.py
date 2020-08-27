#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sergem'
SITENAME = 'sergem personal public notebook'
SITEURL = ''

THEME='pelican-bootstrap3'

PATH = 'content'
USE_FOLDER_AS_CATEGORY = False
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

DEFAULT_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S, %a'
TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


# Blogroll
LINKS = (('Databases', '/pages/collection-of-interesting-databases.html'),
         ('Posts by year', '/pages/posts-by-year.html'),
         ('Books', '/books.html'),
         ('Useful', '/tag/useful.html'),
         ('Bjontegaard metric in Matlab', '/bjontegaard-metric-matlab-script.html'),
         ('RSS', 'feeds/all.rss.xml'),
         ('Atom', 'feeds/all.atom.xml'),
         )

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)


import logging
LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image %s in %s')]

# For theme pelican-bootstrap3
DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


MAIN_MENU=True

DISPLAY_CATEGORIES_ON_SIDEBAR=True
RECENT_POST_COUNT=12
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_PAGES_ON_MENU=False
DISPLAY_TAGS_INLINE=True

# Following items are often useful when publishing
DISQUS_SITENAME = "serge-m-github-io"
GOOGLE_ANALYTICS="UA-40853494-2"

DISPLAY_ARTICLE_INFO_ON_INDEX=True

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud", "sitemap", "i18n_subsites"]

STATIC_PATHS = [ "static", ""]
ARTICLE_EXCLUDES = [ "static"]
PAGE_EXCLUDES = [ "static" ]

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
