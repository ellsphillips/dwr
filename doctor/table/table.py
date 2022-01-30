from dataclasses import dataclass, field
from pandas import DataFrame

from ..constants import Formatting


@dataclass
class Table:

    dataframe: DataFrame

    @property
    def begin(self) -> str:
        return "\\begin{doctor-table}"

    @property
    def options(self) -> str:
        return ""

    @property
    def body(self) -> str:
        return ""

    @property
    def end(self) -> str:
        return "\\end{doctor-table}"


def table(dataframe: DataFrame) -> Table:
    return Table(dataframe)
