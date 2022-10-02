import os
import subprocess

CONFIG = {"path": "build/", "name": "report"}


def build(
    outfile: str = "",
    projectiles: bool = False,
    quick: bool = False,
    verbose: bool = False,
) -> None:
    aux_list = (".aux", ".log", ".out", ".synctex.gz")

    tex_path = f"{CONFIG['path']}"
    tex_file = f"{CONFIG['name']}.tex"

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
