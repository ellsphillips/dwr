from dataclasses import dataclass
from typing import Dict, Iterable, Protocol, Type

from ...exceptions import InvalidChartTypeError
from . import models


class Chart(Protocol):
    def draw(self) -> str:
        ...

    def handle_data(self, data: Iterable[float]) -> str:
        ...


@dataclass
class ChartFactory:

    chart_class: Type[Chart]

    def __call__(self) -> Chart:
        return self.chart_class()


CHART_FACTORIES: Dict[str, ChartFactory] = {
    "line": ChartFactory(models.Line),
    "bar": ChartFactory(models.Bar),
    "scatter": ChartFactory(models.Scatter),
}


def read_chart_factory(choice: str) -> Chart:
    try:
        return CHART_FACTORIES[choice].chart_class()
    except KeyError as err:
        raise InvalidChartTypeError from err
