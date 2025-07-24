# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Onset documentation"
copyright = "2024-2025, Onset"
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
html_extra_path = ["assets/onset_logo_no_bg.png", "assets/SurgeryFlow.png"]
# -- Options for HTML output

html_theme = "furo"

html_logo = "assets/onset_logo_no_bg.png"

html_theme_options = {}

html_title = "Onset Lab Manual"

extensions = ["myst_parser"]

source_suffix = [".rst", ".md"]
