#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Guilherme Ferreira'
SITENAME = 'Guilherme DEV Blog'
SITEURL = 'https://guilhermebferreira.github.io/'

PATH = 'content'

TIMEZONE = 'America/Araguaina'

DEFAULT_LANG = 'pt'

THEME = 'blue-penguin-master'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# all the following settings are *optional*

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = False
DISPLAY_HOME   = True
DISPLAY_MENU   = True

DISQUS_SITENAME = 'https-guilhermebferreira-github-io'
GOOGLE_ANALYTICS = "UA-84295907-1"

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'
ABOUT_ME   		   = 'about.html'

STATIC_PATHS = ['images']
# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Categorias', CATEGORIES_URL, CATEGORIES_SAVE_AS), 
    ('Sobre mim', ABOUT_ME,	ABOUT_ME),
)
# additional menu items
MENUITEMS = (
    #('GitHub', 'https://github.com/guilhermebferreira'),
   
)


SOCIAL = (('twitter', 'https://twitter.com/Guilh_rm_'),
          ('Another social link', '#'),)