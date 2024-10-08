COURSE_NAME = 'AM215'

AUTHOR = 'Ignacio Becker Troncoso'

SEMESTER = 'Fall'

YEAR = '2024'

SITEURL = ''

GITHUB = ''

COLOR = '#8996A0'

# Define Navbar links
# ex. ('Link Name', 'URL')
MENUITEMS = [
    # ('Syllabus', 'pages/syllabus.html'),
    # ('Schedule', 'pages/schedule_static.html'),
     ('Tutorials', 'pages/tutorials.html'),
    ('Projects', 'pages/projects.html'),
    ('Resources', 'pages/resources.html'),

]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'

OUTPUT_PATH = 'docs'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# ================================
# Pelican Settings
# Do not modify
# ================================

FEED_ALL_ATOM = None

CATEGORY_FEED_ATOM = None

TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = None

AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'pages'

AUTHORS_SAVE_AS = ''

CATEGORIES_SAVE_AS = ''

ARCHIVES_SAVE_AS = ''

ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

ARTICLE_URL = '{category}/{slug}/'

AUTHOR_URL = ''

AUTHOR_SAVE_AS = ''

TAG_SAVE_AS = ''

INDEX_SAVE_AS = 'pages/topic_index.html'

THEME_STATIC_DIR = 'style'

DELETE_OUTPUT_DIRECTORY = True

MARKUP = ['md', 'ipynb']

PLUGIN_PATHS = ['plugins']

from pelican_jupyter import markup as nb_markup

# render_math: python -m pip install pelican-katex
PLUGINS = [nb_markup, 'tipue_search', 'pelican_katex']

IGNORE_FILES = [
    '.#*', '.ipynb_checkpoints', 'README.md', "*.html", "__pycache__",
    "*.pptx", ".placeholder", ".DS_Store", "*.ipynb-meta", "*.csv", "*.json",
    "*.txt", "*.xmls", "*.aux", "*.snm", "*.toc", "*.out", "*.nav", 'HW*.md'
]

STATIC_PATHS = ['lectures', 'labs', 'homeworks']

# DIRECT_TEMPLATES = ['index', 'search', 'tags', 'category']
DIRECT_TEMPLATES = ['index', 'search']

# Jinja2 template used to render jupyter notebooks
IPYNB_EXPORT_TEMPLATE = 'themes/templates/nbconvert/lab/base.html.j2'

import re

JINJA_FILTERS = {
    'original_content': lambda x: re.search(r"content/(.*)", x).group(1)
}

USE_FOLDER_AS_CATEGORY = False

import logging

LOG_FILTER = [
    (logging.WARN, "Empty alt attribute for image %s in %s"),
    (logging.WARN, "Meta tag in file %s does not have a 'name' attribute, skipping. Attributes: content=%s")
]
