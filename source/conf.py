import sys
sys.path.append(".")

from princess import PrincessLexer
from sphinx.highlighting import lexers

lexers["princess"] = PrincessLexer(startinline = True)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Princess'
copyright = '2023, Vic Nightfall'
author = 'Vic Nightfall'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme_options = {
    'github_user': 'Princess-org',
    'github_repo': 'Princess',
    'description': 'A modern C-like Programming language with focus on structural typing.'
}

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html'
    ],
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
