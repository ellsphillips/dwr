from dataclasses import dataclass, field, fields
from typing import Iterable, List

from ...constants import Formatting

# from doctor.exceptions import NoDataSuppliedError


@dataclass
class ChartModelDefaults:
    colour: str = "black"
    line_width: str = "thick"
    mark: str = "mark=none"


@dataclass
class Line:

    options: List[str] = field(
        default_factory=lambda: [field.default for field in fields(ChartModelDefaults)]
    )

    def draw(self) -> str:
        # if not data:
        #     raise NoDataSuppliedError

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

    options: List[str] = field(
        default_factory=lambda: [field.default for field in fields(ChartModelDefaults)]
    )

    def draw(self) -> str:
        # if not data:
        #     raise NoDataSuppliedError

        return f"{Formatting.TAB}SCATTER chart with data"

    def handle_data(self, data: Iterable[float]) -> str:
        return f"{data}"


@dataclass
class Scatter:

    options: List[str] = field(
        default_factory=lambda: [field.default for field in fields(ChartModelDefaults)]
    )

    def draw(self) -> str:
        # if not data:
        #     raise NoDataSuppliedError

        return f"{Formatting.TAB}SCATTER chart with data"

    def handle_data(self, data: Iterable[float]) -> str:
        return f"{data}"
