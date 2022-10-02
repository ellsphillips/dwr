from dataclasses import dataclass, field
from typing import Iterable, List

from dwr.constants import Formatting

CHART_MODEL_DEFAULT_STYLING = ["black", "thick", "mark=none"]


@dataclass
class Line:

    options: List[str] = field(default_factory=list)

    def draw(self) -> str:
        elements = [
            f"{Formatting.TAB}\\addplot+[",
            ",\n".join([f"{Formatting.TAB * 2}{opt}" for opt in self.options]),
            f"{Formatting.TAB}] table[x=time, y=some_data]",
            f"{Formatting.TAB}{{src/graphs/timeseries.dat}};",
        ]

        return "%\n".join(e for e in elements)

    def handle_data(self, data: Iterable[float]) -> str:
        return f"{data}"


@dataclass
class Bar:

    options: List[str] = field(default_factory=list)

    def draw(self) -> str:
        return f"{Formatting.TAB}SCATTER chart with data"

    def handle_data(self, data: Iterable[float]) -> str:
        return f"{data}"


@dataclass
class Scatter:

    options: List[str] = field(default_factory=list)

    def draw(self) -> str:
        return f"{Formatting.TAB}SCATTER chart with data"

    def handle_data(self, data: Iterable[float]) -> str:
        return f"{data}"
