"""Sphinx configuration."""
project = "CinemAIRecommender"
author = "Dwaraknaath Varadharajan"
copyright = "2024, Dwaraknaath Varadharajan"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
