import sys
import subprocess


if sys.version_info < (3, 6):
  raise RuntimeError("This module requires Python 3.6 or higher")


def build():
  """
  Run pdflatex shell to build the report.
  """
  pass
