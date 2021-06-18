"""
Put on the LaTeX gloves.
"""

from .doctor import *

from .table import TabularBuilder as table
from .plot import PlotBuilder as plot

version_info = (0, 0, 1)
__version__ = ".".join([str(x) for x in version_info])