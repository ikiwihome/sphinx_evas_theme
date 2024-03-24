# -*- coding: utf-8 -*-
import os
import re
import sys

from sphinx.application import Sphinx
from sphinx import version_info as sphinx_version
from sphinx.config import Config
from datetime import datetime

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    import importlib.resources as resources

def config_initiated(app: Sphinx, config: Config) -> None:

    if not config['language']:
        config['language'] = 'zh_CN'

    if config['project'] == 'Python':
        config['project'] = u'奕行智能项目文档模板'

    if config['author'] == 'unknown':
        if config['language'] == 'zh_CN':
            config['author'] = u'奕行智能科技有限公司'
        else:
            config['author'] = u'EVAS Intelligence Co., Ltd'

    if config['company'] == '':
        if config['language'] == 'zh_CN':
            config['company'] = u'奕行智能科技有限公司'
        else:
            config['company'] = u'EVAS Intelligence Co., Ltd'

    if not config['copyright']:
        currentYear = datetime.now().year
        if config['language'] == 'zh_CN':
            config['copyright'] = '2022-' + str(currentYear) + ', ' + '奕行智能科技有限公司'
        else:
            config['copyright'] = '2022-' + str(currentYear) + ', ' + 'EVAS Intelligence Co., Ltd'

    if not config['master_doc']:
        config['master_doc'] = 'index'

    config['myst_enable_extensions'] = ["colon_fence"]


def extend_html_context(app, pagename, templatename, context, doctree):
    # Add ``sphinx_version_info`` tuple for use in Jinja templates
    context['sphinx_version_info'] = sphinx_version
    context['pdf_file'] = app.config.project


def override_html_config(app: Sphinx, config: Config) -> None:

    theme_path = os.path.abspath(os.path.dirname(__file__))

    if not config['html_static_path']:
        config['html_static_path'] = ['_static']

    if not config['templates_path']:
        config['templates_path'] = ['_templates']

    if not config['html_title']:
        config['html_title'] = config['project']

    if not config['html_logo']:
        config['html_logo'] = os.path.join(theme_path, 'static', 'logo.svg')

    if not config['html_favicon']:
        config['html_favicon'] = os.path.join(theme_path, 'static', 'favicon.ico')

    if not config['html_theme_options']:
        config['html_theme_options'] = {
            'logo_only': False,
            'display_version': True,
            'prev_next_buttons_location': 'bottom',
            'style_external_links': False,
            'vcs_pageview_mode': '',
            'style_nav_header_background': '#2980B9',
            # Toc options
            'collapse_navigation': False,
            'sticky_navigation': False,
            'navigation_depth': 4,
            'includehidden': True,
            'titles_only': False
        }


def override_docx_config(app: Sphinx, config: Config) -> None:

    theme_path = os.path.abspath(os.path.dirname(__file__))
    filename = '%s.docx' % config['project']
    config['docx_documents'] = [
        (
            config['master_doc'],
            filename,
            {
                'title': config['project'],
                'creator': config['author'],
                'subject': config['subtitle'],
                'Company': config['company'],
                'description': 'This document is generated by sphinx_evas_theme',
                'keywords': ['Microsoft', 'Office', 'Word']
            },
            True
        )
    ]

    config['docx_style'] = os.path.join(theme_path, 'docx_templates', 'style.docx')
    config['docx_pagebreak_before_section'] = 0
    config['docx_pagebreak_before_file'] = 0
    config['docx_pagebreak_before_table_of_contents'] = -1
    config['docx_pagebreak_after_table_of_contents'] = 0
    config['docx_coverpage'] = True
    config['docx_update_fields'] = True
    config['docx_table_options'] = {
        'landscape_columns': 0,
        'in_single_page': False,
        'row_splittable': False,
        'header_in_all_page': True,
    }


def override_latex_config(app: Sphinx, config: Config) -> None:

    theme_path = os.path.abspath(os.path.dirname(__file__))
    # only allow latex builder to access rest of the features
    config["latex_logo"] = os.path.join(theme_path, 'latex_templates', 'logo.pdf')
    config["latex_engine"] = "xelatex"
    config["latex_additional_files"] = [
        os.path.join(theme_path, 'latex_templates', 'fonts', 'DejaVuSans.ttf'),
        os.path.join(theme_path, 'latex_templates', 'fonts', 'DejaVuSans-Bold.ttf'),
        os.path.join(theme_path, 'latex_templates', 'fonts', 'DejaVuSans-Oblique.ttf'),
        os.path.join(theme_path, 'latex_templates', 'fonts', 'SourceHanSansSC-Regular.otf')
        ]

    fontpkg = r'''\usepackage[UTF8, fontset=none]{ctex}
\usepackage{fontspec}

\setmainfont{DejaVuSans.ttf}[BoldFont=DejaVuSans-Bold.ttf, ItalicFont=DejaVuSans-Oblique.ttf]
\setsansfont{DejaVuSans.ttf}[BoldFont=DejaVuSans-Bold.ttf, ItalicFont=DejaVuSans-Oblique.ttf]
\setmonofont{DejaVuSans.ttf}[BoldFont=DejaVuSans-Bold.ttf, ItalicFont=DejaVuSans-Oblique.ttf]

\setCJKmainfont{SourceHanSansSC-Regular.otf}[AutoFakeBold,AutoFakeSlant]
\setCJKsansfont{SourceHanSansSC-Regular.otf}[AutoFakeBold,AutoFakeSlant]
\setCJKmonofont{SourceHanSansSC-Regular.otf}[AutoFakeBold,AutoFakeSlant]
'''

    preamble = ''
    with open(os.path.join(theme_path, 'latex_templates', 'preamble.tex')) as f:
        preamble = f.read()

    titlepage = ''
    with open(os.path.join(theme_path, 'latex_templates', 'titlepage.tex')) as f:
        titlepage = f.read()

    config["latex_elements"] = {
        'latex_engine': 'xelatex',

        'papersize': 'a4paper',

        'geometry': '\\usepackage[left=2cm, right=2cm, top=2.54cm, bottom=2.54cm]{geometry}',

        # Latex figure (float) alignment
        'figure_align': 'htbp',

        'pointsize': '10pt',

        # Additional stuff for the LaTeX preamble.
        'fncychap': '\\usepackage[Sonny]{fncychap}',

        'cmappkg': '',

        'fontenc': '\\usepackage[T1]{fontenc}',

        'fontpkg':  fontpkg,

        'preamble': preamble,

        'maketitle': titlepage,

        # change pagestyle back to normal to avoid toc display differnet style with main page
        'tableofcontents': r'''\pagestyle{normal}
    \sphinxtableofcontents''',

        'extraclassoptions': 'openany,fleqn',
    }

    slug = re.sub(r'\W+', '-', app.config.project.lower())

    config["latex_documents"] = [
    (app.config.master_doc, '{0}.tex'.format(slug), app.config.project, app.config.author, 'manual'),
    ]

    config["latex_table_style"] = []

    # read evas.sty from latex_templates and replace this new text
    latex_package = ''
    with open(os.path.join(theme_path, 'latex_templates/docinfo.sty'), 'r') as template:
        latex_package = template.read()
    latex_package = latex_package.replace('<subtitle>', config['subtitle'])
    latex_package = latex_package.replace('<draft_or_release>', config['draft_or_release'])

    if config.pdf_watermark is True:
        latex_package = latex_package.replace('<watermarktext>', config['watermarktext'])
    else:
        latex_package = latex_package.replace('<watermarktext>', '')

    # write/overwrite into evas.sty in output directory
    output_file = os.path.join(app.outdir, 'docinfo.sty')
    # create output directory is not existed
    os.makedirs(app.outdir, exist_ok=True)
    with open(output_file, 'w+', encoding="utf-8") as package:
        package.write(latex_package)