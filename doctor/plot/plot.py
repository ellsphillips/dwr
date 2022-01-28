from dataclasses import dataclass, field
from typing import Dict, Iterable, List


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
        return ""

    @property
    def body(self) -> str:
        return ""

    @property
    def end(self) -> str:
        return "\\end{doctor-plot}"
