# -*- coding: utf-8 -*-
"""
EVAS Docs Sphinx theme.

From https://github.com/ryan-roemer/sphinx-bootstrap-theme.
"""

import os
from pathlib import Path
from sys import version_info as python_version
from sphinx.application import Sphinx
from sphinx import version_info as sphinx_version
from sphinx.util.logging import getLogger

__version__ = '2.0.2'
__version_full__ = __version__

logger = getLogger(__name__)


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app: "Sphinx"):

    """The sphinx entry-point for the extension."""
    builder_name = Path(app.outdir).parts[-1]

    if python_version[0] < 3:
        logger.error("Python 2 is not supported with sphinx_evas_theme, update to Python 3.")

    # add config value for this theme
    app.add_config_value('subtitle', "", 'env', [str])
    app.add_config_value('company', "", 'env', [str])
    app.add_config_value('draft_or_release', u'Release', 'env', [str])
    app.add_config_value('watermarktext', u'EVAS Intelligence Confidential', 'env', [str])
    app.add_config_value('pdf_watermark', True, 'env', [bool])

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    # app.setup_extension('recommonmark')
    app.setup_extension('myst_parser')
    app.setup_extension('sphinx_markdown_tables')
    app.setup_extension('sphinx_markdown_checkbox')
    app.setup_extension('sphinx_copybutton')
    if builder_name == "html":
        app.setup_extension('sphinx_design')
    app.setup_extension('sphinx.ext.intersphinx')
    app.setup_extension('sphinx.ext.autodoc')
    app.setup_extension('sphinx.ext.autosummary')
    app.setup_extension('sphinx.ext.mathjax')
    app.setup_extension('sphinx.ext.viewcode')
    app.setup_extension('sphinx.ext.githubpages')
    app.setup_extension('sphinx.ext.napoleon')
    # app.setup_extension('sphinx_sitemap')
    app.setup_extension('sphinx_togglebutton')
    if builder_name == "docx":
        app.setup_extension('docxbuilder')

    app.add_source_suffix('.rst', 'restructuredtext', True)
    app.add_source_suffix('.md', 'markdown', True)
    app.add_source_suffix('.txt', 'markdown', True)

    # Add Sphinx message catalog for newer versions of Sphinx
    # See http://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_message_catalog
    evas_locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    app.add_message_catalog('sphinx', evas_locale_path)

    from .events import config_initiated
    app.connect('config-inited', config_initiated)

    if builder_name == "html":

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

        from .events import extend_html_context
        from .events import override_html_config

        app.connect("config-inited", override_html_config)

        # Extend the default context when rendering the templates.
        app.connect("html-page-context", extend_html_context)

        # sphinx emits the permalink icon for headers, so choose one more in keeping with our theme
        app.config.html_permalinks_icon = "\uf0c1"

    if builder_name == "docx":
        from .events import override_docx_config
        app.connect("config-inited", override_docx_config)

    if builder_name == "pdf" or builder_name == "latex" or builder_name == "latexpdf":
        from .events import override_latex_config
        app.connect("config-inited", override_latex_config)

    return {'parallel_read_safe': True, 'parallel_write_safe': True}
