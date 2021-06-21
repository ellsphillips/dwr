import sys
import subprocess

from .utils.tex import TeXDefaults as tex


if sys.version_info < (3, 6):
  raise RuntimeError("This module requires Python 3.6 or higher")


def build(verbose=False):
  """
  Run pdflatex shell to build the report.
  """
  shell_cmd = " ".join([
    "pdflatex",
    "-halt-on-error",
    "" if verbose else "-quiet",
    "-output-directory",
    f"{tex.options['document']['path']}",
    f"{tex.options['document']['name']}.tex"
  ])

  subprocess.run(shell_cmd)
