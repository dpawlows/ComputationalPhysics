# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Computational Physics'
copyright = '2020, David Pawlowski'
author = 'David Pawlowski'
master_doc = 'index'
# The full version, including alpha/beta/rc tags
release = '0.1'
html_logo = 'images/elogo1.png'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['nbsphinx','sphinx.ext.mathjax',
'sphinx.ext.intersphinx'
]
nbsphinx_execute = 'never'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

html_context = {
    'css_files': ['_static/computationalphysics.css'],
}
# List of patterns, relative to source directory, that match files and
# directories cssto ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
    '**.ipynb_checkpoints']
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }

#globaltoc makes it so sidebar doesn't change depending on page

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    "collapse_navigation" : False,
   'style_nav_header_background': '#0e6223',
    # 'style_nav_header_background': 'white',

}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/computationalphysics.css',
]

html_context = {
    # Enable the "Edit in GitHub link within the header of each page.
    'display_github': True,
    # Set the following variables to generate the resulting github URL for each page.
    # Format Template: https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    'github_user': 'dpawlows',
    'github_repo': 'site',
    'github_version': 'master/',
    'conf_py_path': '/source/'
}
