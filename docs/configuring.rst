*************
Configuration
*************

Theme options
=============

For example:

.. code:: python

    html_theme_options = {
        'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
        'analytics_anonymize_ip': False,
        'logo_only': False,
        'display_version': True,
        'prev_next_buttons_location': 'bottom',
        'style_external_links': False,
        'vcs_pageview_mode': '',
        'style_nav_header_background': 'white',
        # Toc options
        'collapse_navigation': True,
        'sticky_navigation': True,
        'navigation_depth': 4,
        'includehidden': True,
        'titles_only': False
    }

Table of contents options
-------------------------

The following options change how :rst:dir:`sphinx:toctree` directives generate
documentation navigation.

..
    TODO
    .
    HTML context options
    ~~~~~~~~~~~~~~~~~~~~

Other configuration
===================

Adding a logo
-------------

Using the Sphinx standard option,
you can set an image file to be used as a logo at the top of the sidebar. The
theme option also allows for *only* the logo to be shown
at the top of the sidebar.

Adding custom CSS or Javascript
-------------------------------

Adding custom CSS or Javascript can help you alter the look and feel of this
theme without forking the theme for local use.

In order to add custom CSS or Javascript without disrupting the existing theme
files, you can :doc:`add files to be included in your documentation output
<rtd:guides/adding-custom-css>`.

How the table of contents displays
==================================

Currently the left menu will build based upon any ``toctree`` directives defined
in your source files.  It outputs 4 levels of depth by default, to allow for
quick navigation through topics. If no TOC trees are defined, Sphinx's default
behavior is to use the page headings instead.

It's important to note that if you don't follow the same styling for your reST
headings across your documents, the TOC tree will build incorrectly, and the
resulting menu might not show the correct depth when it renders.

Also note that by default the table of contents is set with
``includehidden=True``. This allows you to set a hidden TOC in your index file
with the :ref:`:hidden: <sphinx:toctree-directive>` property that will allow you
to build a TOC without it rendering in your index.

By default, the navigation will "stick" to the screen as you scroll. However if
your TOC is not tall enough, it will revert to static positioning. To disable the
sticky navigation altogether.
