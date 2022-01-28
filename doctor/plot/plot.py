from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional

from ..constants import Formatting

from .charts.chart import read_chart_factory


@dataclass
class Plot:

    chart_type: str
    data: List[Iterable[float]] = field(default_factory=list)
    chart_list: List[str] = field(default_factory=list)
    plot_options: Dict[str, str] = field(default_factory=dict)

    @property
    def begin(self) -> str:
        return "\\begin{doctor-plot}"

    @property
    def options(self) -> str:
        if not self.plot_options:
            return ""

        return "%\n".join(
            [
                "[",
                ",\n".join(
                    [
                        f"{Formatting.TAB}{k}={{{v}}}"
                        for k, v in self.plot_options.items()
                    ]
                ),
                "]",
            ]
        )

    @property
    def body(self) -> str:
        return "\n%\n".join(self.chart_list)

    @property
    def end(self) -> str:
        return "\\end{doctor-plot}"


def plot(
    choice: str, data: List[Iterable[float]], options: Optional[Dict[str, str]] = None
) -> Plot:
    if options is None:
        options = {}
    chart = read_chart_factory(choice)

    list_of_charts = [chart.draw() for _ in data]

    for chart_data in data:
        chart.handle_data(chart_data)

    return Plot(
        chart_type=choice,
        data=data,
        chart_list=list_of_charts,
        plot_options=options,
    )
