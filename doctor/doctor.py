import os
import sys
import time
import subprocess

from .utils.cli import *
from .utils.tex import TeXDefaults as tex


if sys.version_info < (3, 6):
  raise RuntimeError("This module requires Python 3.6 or higher")


def build(
  outfile: str = "",
  projectiles: bool = False,
  quick: bool = False,
  verbose: bool = False
):
  """
  Run pdflatex shell to build the report.
  """

  aux_list = (".aux", ".log", ".out")

  tex_path = f"{tex.options['document']['path']}"
  tex_file = f"{tex.options['document']['name']}.tex"

  loader = Loader(
    "Building your report...",
    f"Report generated at {colour.CBOLD}{colour.CYELLOW}{tex_path}{outfile}.pdf{colour.CEND}\n",
    0.05
  ).start()

  shell_cmd = " ".join([
    "pdflatex",
    "-interaction=nonstopmode",
    "" if verbose else "-quiet",
    f"-job-name={outfile}" if outfile else "",
    "-output-directory",
    f"{tex_path} {tex_file}",
  ])

  for _ in range(1 if quick else 3):
    subprocess.run(shell_cmd)

  if not projectiles:
    for _file in os.listdir(tex_path):
      if _file.endswith(aux_list):
        os.remove(os.path.join(tex_path, _file))

  loader.stop()
