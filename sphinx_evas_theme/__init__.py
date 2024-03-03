# -*- coding: utf-8 -*-
"""
EVAS Docs Sphinx theme.

From https://github.com/ryan-roemer/sphinx-bootstrap-theme.
"""

import os
from pathlib import Path
from datetime import datetime
from sys import version_info as python_version
from sphinx import version_info as sphinx_version
from sphinx.config import Config
from sphinx.locale import _
from sphinx.util.logging import getLogger


__version__ = '0.3.0'
__version_full__ = __version__

logger = getLogger(__name__)

def config_initiated(app, config):

    theme_path = os.path.abspath(os.path.dirname(__file__))

    if not config.language:
        config.language = 'en'

    if not config.project:
        config.project = u'EVAS Docs Template'

    if not config.author:
        if config.language == 'zh_CN':
            config.author = u'奕行智能科技有限公司'
        else:
            config.author = u'EVAS Intelligence Co., Ltd'

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    config.extensions = [
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

    if not config.source_suffix:
        config.source_suffix = {
            '.rst': 'restructuredtext',
            '.md': 'markdown',
            '.txt': 'markdown',
        }

    if not config.html_static_path:
        config.html_static_path = ['_static']

    if not config.templates_path:
        config.templates_path = ['_templates']

    if not config.html_logo:
        config.html_logo = os.path.join(theme_path, 'static', 'logo.svg')

    if not config.html_favicon:
        config.html_favicon = os.path.join(theme_path, 'static', 'favicon.ico')

    if not config.html_theme_options:
        config.html_theme_options = {
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

    if not config.master_doc:
        config.master_doc = 'index'

    builder_name = Path(app.outdir).parts[-1]
    if builder_name == "pdf" or builder_name == "latex" or builder_name == "latexpdf":
        # read evas.sty from latex_templates and replace this new text
        latex_package = ''
        with open(os.path.join(theme_path, 'latex_templates/docinfo.sty'), 'r') as template:
            latex_package = template.read()
        latex_package = latex_package.replace('<subtitle>', config.subtitle)
        latex_package = latex_package.replace('<draft_or_release>', config.draft_or_release)

        if config.pdf_watermark is True:
            latex_package = latex_package.replace('<watermarktext>', config.watermarktext)
        else:
            latex_package = latex_package.replace('<watermarktext>', '')

        # write/overwrite into evas.sty in output directory
        output_file = os.path.join(app.outdir, 'docinfo.sty')
        # create output directory is not existed
        os.makedirs(app.outdir, exist_ok=True)
        with open(output_file, 'w+', encoding="utf-8") as package:
            package.write(latex_package)
    

def extend_html_context(app, pagename, templatename, context, doctree):
    # Add ``sphinx_version_info`` tuple for use in Jinja templates
    context['sphinx_version_info'] = sphinx_version
    context['pdf_file'] = app.config.project

# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app: "Sphinx"):

    """The sphinx entry-point for the extension."""
    from .events import override_latex_config
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
    
    # add config value for this theme
    app.add_config_value('subtitle', "", 'env', [str])
    app.add_config_value('draft_or_release', u'Release', 'env', [str])
    app.add_config_value('watermarktext', u'EVAS Intelligence Confidential', 'env', [str])
    app.add_config_value('pdf_watermark', True, 'env', [bool])

    # Add Sphinx message catalog for newer versions of Sphinx
    # See http://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_message_catalog
    evas_locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    app.add_message_catalog('sphinx', evas_locale_path)
    app.connect('config-inited', config_initiated)

    # sphinx emits the permalink icon for headers, so choose one more in keeping with our theme
    app.config.html_permalinks_icon = "\uf0c1"

    # Extend the default context when rendering the templates.
    app.connect("html-page-context", extend_html_context)
    app.connect("config-inited", override_latex_config)

    return {'parallel_read_safe': True, 'parallel_write_safe': True}