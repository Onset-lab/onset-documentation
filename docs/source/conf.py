# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Onset documentation"
copyright = "2024-, Onset"
author = "Onset"

release = ""
version = ""

# -- General configuration

extensions = [
    "sphinx.ext.autodoc",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]
html_extra_path = ["data/onset_logo_no_bg.png"]
# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

html_logo = "data/onset_logo_no_bg.png"

html_theme_options = {
    "logo_only": True,
    "display_version": True,
    "style_nav_header_background": "#f0f2f5",
}

# -- Options for EPUB output
epub_show_urls = "footnote"
