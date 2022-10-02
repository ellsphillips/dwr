from dataclasses import dataclass
from typing import List, Tuple, Union

from pandas import DataFrame

from dwr.constants import Formatting


@dataclass
class TableBody:

    dataframe: DataFrame

    def create(self) -> str:
        export: List[str] = []
        for _, row in self.dataframe.iterrows():  # type: ignore
            export.append(
                Formatting.TAB
                + " & ".join(
                    [
                        self.pad_spaces(cell, col_index)
                        for col_index, cell in enumerate(row.values)  # type: ignore
                    ]
                )
                + f" {Formatting.NEWLINE}"
            )
        return "\n".join([item for item in export if item])

    @property
    def column_widths(self) -> List[Tuple[int, int]]:
        return [
            (i, max(self.dataframe[col].astype(str).map(len)))  # type: ignore
            for i, col in enumerate(self.dataframe)
        ]

    def pad_spaces(self, cell_value: Union[int, str], col_index: int) -> str:
        _cell = str(cell_value)

        if len(_cell) >= self.column_widths[col_index][1]:
            return _cell

        if isinstance(cell_value, str):
            return _cell.ljust(self.column_widths[col_index][1])

        return _cell.rjust(self.column_widths[col_index][1])
