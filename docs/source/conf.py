import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "OC Lettings Site"
copyright = "2025"
author = "Your Name"
release = "1.0"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

html_theme = "sphinx_rtd_theme"
