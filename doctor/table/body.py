from dataclasses import dataclass
from typing import List, Tuple, Union

from pandas import DataFrame


@dataclass
class TableBody:

    dataframe: DataFrame

    @property
    def column_widths(self) -> List[Tuple[int, int]]:
        return [
            (i, max(self.dataframe[col].astype(str).map(len)))  # type: ignore
            for i, col in enumerate(self.dataframe)  # type: ignore
        ]

    def pad_spaces(self, cell_value: Union[int, str], col_index: int) -> str:
        _cell = str(cell_value)

        if len(_cell) >= self.column_widths[col_index][1]:
            return _cell

        if isinstance(cell_value, str):
            return _cell.ljust(self.column_widths[col_index][1])

        return _cell.rjust(self.column_widths[col_index][1])
