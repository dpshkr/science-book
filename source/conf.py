# -*- coding: utf-8 -*-
# Note that not all possible configuration values are present. All configuration
# values have a default.

# -- General configuration --
project = '2D Semiconductors'
copyright = '2024, Pushkar'
author = 'Pushkar'

master_doc = 'index'
version = 'latest'
pygments_style = 'sphinx'

extensions = [
 "sphinxext.opengraph",
 "notfound.extension",
 "sphinx_sitemap"
]

sitemap_filename = "sitemap.xml"

html_css_files = ['custom.css']
html_js_files = ['custom.js']
html_theme = 'sphinx_rtd_theme'
html_baseurl = 'https://sphinx-netlify.netlify.app/'
html_theme_options = {
    'current_version': version,
    "collapse_navigation": False,
}
html_context = {
  'display_github': True,
  'github_user': 'dpshkr',
  'github_repo': 'science-book',
  'github_version': 'main/source/'
}

html_favicon = '_static/favicon.ico'
html_static_path = ['_static']
html_extra_path = ['robots.txt']

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True
html_show_copyright = True

htmlhelp_basename = 'ContinuousSphinxDoc'
