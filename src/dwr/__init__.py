"""Put on the LaTeX gloves."""

from dwr import data
from dwr.config.config import read_config
from dwr.plot.plot import plot
from dwr.render import render
from dwr.table.table import table

version_info = (0, 1, 0)
__version__ = ".".join([str(x) for x in version_info])
