"""Put on the LaTeX gloves."""

from . import data as data
from .config.config import read_config as read_config
from .plot.plot import plot as plot
from .render import render, save
from .table.table import table as table

version_info = (0, 0, 2)
__version__ = ".".join([str(x) for x in version_info])
