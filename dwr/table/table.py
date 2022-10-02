from dataclasses import dataclass
from typing import Iterable, List, Protocol

from pandas import DataFrame

from dwr.table.body import TableBody
from dwr.table.header import TableHeader


class TableElement(Protocol):
    def create(self) -> str:
        ...


def compile_table(elements: Iterable[TableElement]) -> List[str]:
    return [e.create() for e in elements]


@dataclass
class Table:

    dataframe: DataFrame
    header: bool = True

    @property
    def begin(self) -> str:
        return "\\begin{dwr-table}"

    @property
    def options(self) -> str:
        return ""

    @property
    def body(self) -> str:
        return "\n".join(
            compile_table(
                [
                    TableHeader(self.dataframe.columns.values),  # type: ignore
                    TableBody(self.dataframe),
                ]
            )
        )

    @property
    def end(self) -> str:
        return "\\end{dwr-table}"


def table(dataframe: DataFrame) -> Table:
    return Table(dataframe)
