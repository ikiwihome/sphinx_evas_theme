# -*- coding: utf-8 -*-
import os
import re
import sys

from sphinx.application import Sphinx
from sphinx.config import Config

from . import __version__, latex_templates

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    import importlib.resources as resources

def override_latex_config(app: Sphinx, config: Config) -> None:

    theme_path = os.path.abspath(os.path.dirname(__file__))

    # only allow latex builder to access rest of the features
    config["latex_logo"] = os.path.join(theme_path, 'latex_templates', 'logo.pdf')
    config["latex_engine"] = "xelatex"
    config["latex_additional_files"] = [
        os.path.join(theme_path, 'latex_templates', 'fonts', 'DejaVuSans.ttf'),
        os.path.join(theme_path, 'latex_templates', 'fonts', 'SourceHanSansSC-Regular.otf')
        ]

    fontpkg = r'''\usepackage[UTF8]{ctex}
\setCJKmainfont{SourceHanSansSC-Regular.otf}[AutoFakeBold,AutoFakeSlant]
\setCJKsansfont{SourceHanSansSC-Regular.otf}[AutoFakeBold,AutoFakeSlant]
\setCJKmonofont{SourceHanSansSC-Regular.otf}[AutoFakeBold,AutoFakeSlant]

\setmainfont{DejaVuSans.ttf}[AutoFakeBold,AutoFakeSlant]
\setsansfont{DejaVuSans.ttf}[AutoFakeBold,AutoFakeSlant]
\setmonofont{DejaVuSans.ttf}[AutoFakeBold,AutoFakeSlant]
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

        'geometry': '\\usepackage[twoside, asymmetric, left=2cm, right=2cm, top=2.54cm, bottom=2cm]{geometry}',

        # Latex figure (float) alignment
        'figure_align': 'htbp',

        'pointsize': '10pt',

        # Additional stuff for the LaTeX preamble.
        'fncychap': '\\usepackage[Sonny]{fncychap}',

        'fontpkg':  fontpkg,

        'preamble': preamble,

        'maketitle': titlepage,

        # change pagestyle back to normal to avoid toc display differnet style with main page
        'tableofcontents': r'''\pagestyle{normal}
    \sphinxtableofcontents''',

        'extraclassoptions': 'openany,oneside,fleqn',
    }

    slug = re.sub(r'\W+', '-', app.config.project.lower())

    config["latex_documents"] = [
    (app.config.master_doc, '{0}.tex'.format(slug), app.config.project, app.config.author, 'manual'),
    ]

    config["latex_table_style"] = []
