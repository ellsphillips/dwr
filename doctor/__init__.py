"""
Put on the LaTeX gloves.
"""

from .config.config import read_config as read_config
from . import data as data
from .plot.plot import plot as plot
from .render import render as render

version_info = (0, 0, 2)
__version__ = ".".join([str(x) for x in version_info])
