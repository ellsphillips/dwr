from dataclasses import dataclass, field
from typing import List

from dwr.plot.charts.chart import Chart


@dataclass
class Canvas:

    charts: List[Chart] = field(default_factory=list)

    def add_charts(self, new_charts: List[Chart]) -> None:
        self.charts.extend(new_charts)

    @property
    def result(self) -> str:
        return "\n%\n".join([chart.draw() for chart in self.charts])
