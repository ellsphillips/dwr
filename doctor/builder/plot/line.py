from typing import Optional, Tuple, Union

import pandas as pd

from ...utils.cli import *
from ...utils.tex import TeXDefaults as tex


class Line:
    """ """

    tab_space = " " * 4
    double_backslash = "\\\\"

    colours = [
        "ons-blue",
        "ons-green",
        "ons-pink",
        "ons-orange",
        "ons-yellow",
    ]

    def __init__(self, data: dict = None, options: dict = None):
        self.data = data
        self.options = options
        self.plot_declarations: list = []

        if data is None:
            log.warning("I'm not much good without data, you know...")

    def bound_converter(self, bounds: Tuple[str, str]) -> str:
        acceptance = ("x_min", "x_max", "y_min", "y_max")

        return [
            self.axis_bound(*(bound.split("_"))) if bound in acceptance else bound
            for bound in bounds
        ]

    def axis_bound(self, axis: str, extrema: str) -> str:
        return f"\pgfkeysvalueof{{/pgfplots/{axis}{extrema}}}"

    def pluck(opts: dict, *args) -> list:
        return [opts[arg] for arg in args]

    def id_data(self) -> list:
        return [(name, series) for name, series in self.data.items()]

    def build_dataframe(self) -> pd.DataFrame:
        time_points = max([len(ts[1]) for ts in self.id_data()])
        log.comment(f"Built dataframe of dimension [{len(self.data), time_points}]")

        output = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in self.data.items()]))
        output["time"] = range(time_points)

        return output[["time"] + [c for c in output.columns if c != "time"]]

    def plot_state(func):
        def wrapper(*args, **kwargs):
            wrapper.colour_index += 1
            return func(*args, **kwargs)

        wrapper.colour_index = 0
        return wrapper

    @plot_state
    def add_plot(self) -> str:
        args = [
            self.colours[(self.add_plot.colour_index - 1) % len(self.colours)],
            "thick",
            "mark=none",
        ]

        elements = [
            f"{self.tab_space}\\addplot[",
            ",\n".join([f"{self.tab_space * 2}{arg}" for arg in args]),
            f"{self.tab_space}] table[x=time, y={list(self.data)[self.add_plot.colour_index - 1]}]",
            f"{self.tab_space}{{src/graphs/timeseries.dat}};%",
        ]

        res = "%\n".join(e for e in elements)
        self.plot_declarations.append(res)

        return res

    def add_shade(
        self,
        domain: Tuple[Union[str, int], Union[str, int]],
        range: Tuple[Union[str, int], Union[str, int]],
        colour: Optional[str] = "black!2",
        fill: str = "solid",
    ) -> None:
        if not fill or fill not in ("hatch", "solid"):
            log.warning("doctor.plot.add_shade('solid' | 'hatch')")
            raise ValueError("Fill type must be solid or hatch.")

        args = [
            f"{self.tab_space}draw=none",
            f",\n{self.tab_space * 2}".join(
                [
                    "pattern=flexible hatch",
                    "hatch distance=10pt",
                    "hatch thickness=.5pt",
                    f"pattern color={str(colour if colour else 'gray')}!10",
                ]
            )
            if fill == "hatch"
            else "",
            f",\n{self.tab_space * 2}".join(
                [
                    f"fill={str(colour if colour else 'gray')}",
                    "opacity=0.1",
                ]
            )
            if fill == "solid"
            else "",
        ]

        out = (
            f"%\n{self.tab_space}".join(
                [
                    f"{self.tab_space}\\addplot[",
                    f",\n{self.tab_space * 2}".join(arg for arg in args if arg),
                    "]",
                    f"({domain[0]}, {domain[1]})",
                    "rectangle",
                    f"({range[0]}, {range[1]})",
                ]
            )
            + ";%"
        )

        self.plot_declarations.insert(0, out)

    def apply_shading(self) -> None:
        obj = self.options["shade"] if "shade" in self.options else ""

        self.add_shade(
            domain=(self.bound_converter(obj["domain"])),
            range=(self.bound_converter(obj["range"])),
            fill=obj["fill"],
            colour=obj["colour"],
        )

    @property
    def env_begin(self) -> str:
        return r"\begin{doctor-plot}%"

    @property
    def env_end(self) -> str:
        return r"\end{doctor-plot}%"

    @property
    def env_body(self) -> str:
        [self.add_plot() for _ in list(self.data)]
        self.apply_shading()
        return "\n%\n".join(syn for syn in self.plot_declarations)

    def get_result(self) -> str:
        elements = [
            self.env_begin,
            self.env_body,
            self.env_end,
        ]
        result = "\n".join([item for item in elements])
        trailing_newline = "\n"
        result += trailing_newline

        log.comment(
            "[TeX source generated] for plotting timeseries:\n"
            + "\n".join(
                [
                    "{",
                    ",\n".join([f"{self.tab_space}[{ts}]" for ts in list(self.data)]),
                    "}",
                ]
            )
        )

        return result

    def export_data(self, out_path: str) -> None:
        destination = f"{tex.options['document']['path']}src/{out_path}.csv"
        dataframe = self.build_dataframe()
        dataframe.to_csv(destination, index=False, encoding="utf-8")
        log.output(destination)

    def export(self, out_path: str) -> None:
        destination = f"{tex.options['document']['path']}src/{out_path}.tex"
        with open(destination, "w") as f:
            f.write(self.get_result())

        self.export_data(out_path=out_path)

        log.output(destination)
