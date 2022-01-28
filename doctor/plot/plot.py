from dataclasses import dataclass, field
from typing import Dict, Iterable, List

from ..constants import Formatting


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
