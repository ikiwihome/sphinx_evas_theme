# -*- coding: utf-8 -*-
import os
from datetime import datetime

# language = 'en'
language = 'zh_CN'

# project is also the title of the docs
project = u'请在此处输入标题'
currentYear = datetime.now().year

# subtitle is displayed in pdf cover page
subtitle = u'请在此处输入子标题'

if language == 'zh_CN':
    author = u'奕行智能科技有限公司'
else:
    author = u'EVAS Intelligence Co., Ltd'

copyright = '2022-' + str(currentYear) + ', ' + author

# the release tag is displayed in pdf bottom right area
release = 'V1.0'

# the status and version tag are displayed in html top left area
draft_or_release = u'Release'
version = 'V1.0'

# watermark text control config
pdf_watermark = True
watermarktext = u'EVAS Intelligence Confidential'

extensions = ['sphinx_evas_theme']
html_theme = 'sphinx_evas_theme'