"""
EVAS Docs Sphinx theme.

From https://github.com/ryan-roemer/sphinx-bootstrap-theme.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from sys import version_info as python_version
from sphinx import version_info as sphinx_version
from sphinx.locale import _
from sphinx.util.logging import getLogger


__version__ = '0.1.0'
__version_full__ = __version__

logger = getLogger(__name__)


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir


def config_initiated(app, config):
    theme_options = config.html_theme_options or {}
    if theme_options.get('canonical_url'):
        logger.warning(
            _('The canonical_url option is deprecated, use the html_baseurl option from Sphinx instead.')
        )


def extend_html_context(app, pagename, templatename, context, doctree):
    # Add ``sphinx_version_info`` tuple for use in Jinja templates
    context['sphinx_version_info'] = sphinx_version
    context['pdf_file'] = app.config.project


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    if python_version[0] < 3:
        logger.error("Python 2 is not supported with sphinx_evas_theme, update to Python 3.")

    app.require_sphinx('5.0')
    if app.config.html4_writer:
        logger.error("'html4_writer' is not supported with sphinx_evas_theme.")

    # Since Sphinx 6, jquery isn't bundled anymore and we need to ensure that
    # the sphinxcontrib-jquery extension is enabled.
    # See: https://dev.readthedocs.io/en/latest/design/sphinx-jquery.html
    if sphinx_version >= (6, 0, 0):
        # Documentation of Sphinx guarantees that an extension is added and
        # enabled at most once.
        # See: https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.setup_extension
        app.setup_extension("sphinxcontrib.jquery")
        # However, we need to call the extension's callback since setup_extension doesn't do it
        # See: https://github.com/sphinx-contrib/jquery/issues/23
        from sphinxcontrib.jquery import add_js_files as jquery_add_js_files
        jquery_add_js_files(app, app.config)

    # Register the theme that can be referenced without adding a theme path
    app.add_html_theme('sphinx_evas_theme', os.path.abspath(os.path.dirname(__file__)))

    # Add Sphinx message catalog for newer versions of Sphinx
    # See http://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_message_catalog
    evas_locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    app.add_message_catalog('sphinx', evas_locale_path)
    app.connect('config-inited', config_initiated)

    # sphinx emits the permalink icon for headers, so choose one more in keeping with our theme
    app.config.html_permalinks_icon = "\uf0c1"

    # Extend the default context when rendering the templates.
    app.connect("html-page-context", extend_html_context)

    # ----------------------------------------------------------------------------
    # ----------------------------------------------------------------------------
    # -- New configuration -------------------------------------------------------
    # ----------------------------------------------------------------------------
    # ----------------------------------------------------------------------------

    theme_path = os.path.abspath(os.path.dirname(__file__))

    if app.config.language == 'zh_CN':
        app.config.author = u'奕行智能科技有限公司'
    else:
        app.config.author = u'EVAS Intelligence Co., Ltd'

    watermarktext = u'EVAS Intelligence Confidential'

    # -- General configuration ---------------------------------------------------

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    extensions = [
        'recommonmark',
        'sphinx_markdown_tables',
        # Auto-generate section labels.
        # 'sphinx.ext.autosectionlabel',
        'sphinx.ext.intersphinx',
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.mathjax',
        'sphinx.ext.viewcode',
        'sphinx_copybutton',
        'sphinx_evas_theme'
        #'docxbuilder' # used to generate word docx file
    ]

    source_suffix = {
        '.rst': 'restructuredtext',
        '.md': 'markdown',
        '.txt': 'markdown',
    }

    html_logo = os.path.join(theme_path, 'static', 'logo.svg')
    html_favicon = os.path.join(theme_path, 'static', 'favicon.ico')

    html_theme_options = {
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

    # The name of an image file (relative to this directory) to place at the bottom of
    # the title page.

    latex_logo = os.path.join(theme_path, 'latex_templates', 'logo.pdf')
    latex_engine = 'xelatex'

    latex_additional_files = [
        os.path.join(theme_path, 'latex_templates', 'fonts', 'DejaVuSans.ttf'),
        os.path.join(theme_path, 'latex_templates', 'fonts', 'SourceHanSansSC-Regular.otf')
        ]

    fontpkg = r'''
    \usepackage[UTF8]{ctex}

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

    latex_elements = {
        'latex_engine': 'xelatex',

        'papersize': 'a4paper',

        'geometry': '\\usepackage{geometry}',

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

    }

    latex_use_xindy = True
    
    # This script is used to import subtitle to evas.sty, then copy to output directory
    # the builder_name is split from the output directory path
    # since "read the docs" server use pdf as output directory, so "pdf" is also list here
    # in other case, "latex" is enough for local windows or linux environment
    builder_name = Path(app.outdir).parts[-1]
    if builder_name == "pdf" or builder_name == "latex":
        # read evas.sty from latex_templates and replace this new text
        latex_package = ''
        with open(os.path.join(theme_path, 'latex_templates', 'docinfo.sty'), 'r') as template:
            latex_package = template.read()
        latex_package = latex_package.replace('<subtitle>', app.config.subtitle)
        latex_package = latex_package.replace('<draft_or_release>', app.config.draft_or_release)

        if pdf_watermark is True:
            latex_package = latex_package.replace('<watermarktext>', app.config.watermarktext)
        else:
            latex_package = latex_package.replace('<watermarktext>', '')

        # write/overwrite into evas.sty in output directory
        output_file = os.path.join(app.outdir, 'docinfo.sty')
        # create output directory is not existed
        os.makedirs(app.outdir, exist_ok=True)
        with open(output_file, 'w+', encoding="utf-8") as package:
            package.write(latex_package)

    return {'parallel_read_safe': True, 'parallel_write_safe': True}