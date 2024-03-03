EVAS Docs Sphinx Theme
==========================

This Sphinx_ theme was designed to provide a great reader experience for
documentation users on both desktop and mobile devices. This theme is commonly
used with projects on `EVAS Docs`_ but can work with any Sphinx project.

.. _Sphinx: http://www.sphinx-doc.org
.. _EVAS Docs: https://github.com/ikiwihome/sphinx_evas_theme

Using this theme
----------------

:doc:`installing`
    How to install this theme on your Sphinx project.

:doc:`configuring`
    Theme configuration and customization options.

Development
-----------

:doc:`Demo documentation <demo/structure>`
    The theme's styleguide test environment, where new changes are tested.

.. Hidden TOCs

.. toctree::
   :caption: Theme Documentation
   :maxdepth: 2
   :hidden:

   installing
   configuring

.. toctree::
    :maxdepth: 2
    :numbered:
    :caption: Demo Documentation
    :hidden:

    demo/structure
    demo/demo
    demo/lists_tables
    demo/api

.. toctree::
    :maxdepth: 3
    :numbered:
    :caption: This is an incredibly long caption for a long menu
    :hidden:

    demo/long

.. toctree::
    :maxdepth: 3
    :caption: Breadcrumbs

    demo/level1/index.rst
