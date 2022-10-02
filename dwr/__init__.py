"""Put on the LaTeX gloves."""

from . import data
from .plot.plot import plot
from .render import render
from .table.table import table

version_info = (0, 1, 0)
__version__ = ".".join([str(x) for x in version_info])
