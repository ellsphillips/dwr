from dataclasses import dataclass

from pandas import DataFrame

from ..table.body import TableBody


@dataclass
class Table:

    dataframe: DataFrame
    header: bool = True

    @property
    def begin(self) -> str:
        return "\\begin{doctor-table}"

    @property
    def options(self) -> str:
        return ""

    @property
    def body(self) -> str:
        return TableBody(self.dataframe).create()

    @property
    def end(self) -> str:
        return "\\end{doctor-table}"


def table(dataframe: DataFrame) -> Table:
    return Table(dataframe)
