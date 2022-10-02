import os
import subprocess

from dwr.utils.cli import Loader, Style
from dwr.utils.tex import TeXDefaults as tex


def build(
    outfile: str = "",
    projectiles: bool = False,
    quick: bool = False,
    verbose: bool = False,
) -> None:
    aux_list = (".aux", ".log", ".out", ".synctex.gz")

    tex_path = f"{tex.document['path']}"
    tex_file = f"{tex.document['name']}.tex"

    loader = Loader(
        "Building your report...",
        f"Report generated at {Style.announce}{tex_path}{outfile}.pdf{Style.end}\n",
        0.05,
    ).start()

    shell_cmd = " ".join(
        [
            "pdflatex",
            "-interaction nonstopmode",
            "" if verbose else "-quiet",
            f"-job-name={outfile}" if outfile else "",
            "-output-directory",
            f"{tex_path} {tex_file}",
        ]
    )

    for _ in range(1 if quick else 3):
        subprocess.run(shell_cmd, check=False)

    if not projectiles:
        for _file in os.listdir(tex_path):
            if _file.endswith(aux_list):
                os.remove(os.path.join(tex_path, _file))

    loader.stop()
