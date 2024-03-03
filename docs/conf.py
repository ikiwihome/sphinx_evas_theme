# -*- coding: utf-8 -*-

import sys
import os
import re

# Prefer to use the version of the theme in this repo
# and not the installed version of the theme.
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('./demo/'))

from sphinx_evas_theme import __version__ as theme_version
from sphinx_evas_theme import __version_full__ as theme_version_full

project = u'EVAS Docs Sphinx Theme'
slug = re.sub(r'\W+', '-', project.lower())
version = theme_version
release = theme_version_full
author = u'EVAS Intelligence Co., Ltd'
# copyright = author
language = 'en'
# language = 'zh_CN'

extensions = ['sphinx_evas_theme']

html_theme = 'sphinx_evas_theme'
