import os
import sys
import subprocess

from .utils.tex import TeXDefaults as tex


if sys.version_info < (3, 6):
  raise RuntimeError("This module requires Python 3.6 or higher")


def build(
  outfile: str = "",
  projectiles: bool = False,
  verbose: bool = False
):
  """
  Run pdflatex shell to build the report.
  """
  aux_list = (".aux", ".log", ".out")

  tex_path = f"{tex.options['document']['path']}"
  tex_file = f"{tex.options['document']['name']}.tex"

  shell_cmd = " ".join([
    "pdflatex",
    "-interaction=nonstopmode",
    "" if verbose else "-quiet",
    f"-job-name={outfile}" if outfile else "",
    "-output-directory",
    f"{tex_path} {tex_file}",
  ])

  subprocess.run(shell_cmd)

  print(
    "Report generated at",
    f"\033[1m\033[93m{tex_path}{outfile}.pdf\033[0m",
    "\n"
  )

  if not projectiles:
    for _file in os.listdir(tex_path):
      if _file.endswith(aux_list):
        os.remove(os.path.join(tex_path, _file))
