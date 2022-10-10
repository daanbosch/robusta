#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Robusta documentation build configuration file, created by
# sphinx-quickstart on Wed Apr 28 13:48:20 2021.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# add the root robusta directory to the path so that playbooks/ becomes importable
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / Path("_ext")))
sys.path.insert(0, str(Path(__file__).parent.parent))  # so we can import the playbooks

# -- General configuration ------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.autosummary",
    "sphinxcontrib.mermaid",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.images",
    "autorobusta",
    "sphinx_immaterial",
]
# for sphinx.ext.inheritance_diagram
# inheritance_graph_attrs = dict(rankdir="TB", size='""')

images_config = {
    "override_image_directive": True,
}

smartquotes = False

autodoc_mock_imports = ["prometheus_api_client"]
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    #'special-members': '__init__',
    "undoc-members": True,
    #'exclude-members': '__weakref__'
}
autoclass_content = "both"
add_module_names = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Robusta"
copyright = "2022, Robusta"
author = "Natan Yellin"

# The short X.Y version.
# version = "DOCS_VERSION_PLACEHOLDER"
# The full version, including alpha/beta/rc tags.
# release = "DOCS_RELEASE_PLACEHOLDER"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = "manni"
# pygments_dark_style = "monokai"
pygments_style = "witchhazel.WitchHazelStyle"
pygments_dark_style = "witchhazel.WitchHazelStyle"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# html_theme_path = [furo.get_pygments_stylesheet()]
html_theme = "sphinx_immaterial"
# html_theme = "sphinx_material"

html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "repo_url": "https://github.com/robusta-dev/robusta",
    "repo_name": "Robusta",
    "edit_uri": "tree/docsimmaterial/docs",   ##### Modify to the Master Branch ###########
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "deep-purple",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-purple",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "features": [
        # "navigation.expand",
        "navigation.tabs",
        "navigation.tabs.sticky",
        # "toc.integrate",
        "navigation.sections",
        "navigation.indexes",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
    ],
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/robusta-dev/robusta",
        },
        {
            "icon": "fontawesome/brands/slack",
            "link": "https://bit.ly/robusta-slack",
        },   
        {
            "icon": "fontawesome/brands/twitter",
            "link": "https://twitter.com/RobustaDev",
        },
        {
            "icon": "fontawesome/brands/linkedin",
            "link": "https://www.linkedin.com/company/robusta-dev/",
        },
    ],

}

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# html_title = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "custom.css",
]

html_js_files = ["analytics.js"]

html_favicon = "_static/favicon.png"

# html_logo = "_static/logo.png"


def setup(app):
    app.add_css_file("custom.css")
