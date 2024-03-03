# -*- coding: utf-8 -*-

# 文档语言，支持en和zh_CN
# language = 'en'
language = 'zh_CN'

# 主标题和项目名，必填，显示在html左上角，PDF文件名，PDF封面第一行以及内容页左上角，默认为'奕行智能项目文档模板'
project = u'奕行智能项目文档模板'

# 子标题，显示在PDF封面第二行，不显示子标题则设置为''或注释掉
subtitle = u'子标题'

# 文档作者，默认为 '奕行智能科技有限公司'，默认根据中英文自动切换，显示在PDF封面以及内容页左下角
# author = u'奕行智能科技有限公司'

# 版权信息，默认为 '2022-2024, 奕行智能科技有限公司'，根据中英文自动切换
# copyright = u'2022-2024, 奕行智能科技有限公司'

# 标记文档状态为Draft还是Release，默认Release，状态显示在PDF封面右下角以及内容页右下角
draft_or_release = u'Release'

# release标记，必填，显示在PDF文件的右下角
release = 'V1.0'

# 版本信息，必填，显示在html的左上角
version = 'V1.0'

# 是否显示PDF水印，默认True，不显示则设置为False
pdf_watermark = True

# PDF水印文本，默认为'EVAS Intelligence Confidential'
watermarktext = u'EVAS Intelligence Confidential'

# 是否在html右上角显示源代码，默认False，默认True
html_show_sourcelink = False

# 是否在html左下角显示Sphinx版权信息，默认True
html_show_sphinx = False

# 在html下方显示'最后更新于'的时间格式，如注释掉则不显示
html_last_updated_fmt = '%x %X'

# 扩展插件，必填
extensions = ['sphinx_evas_theme']

# Sphinx主题，必填，不要修改
html_theme = 'sphinx_evas_theme'
