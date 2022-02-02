from dataclasses import dataclass
from typing import List, Optional

import pandas as pd

from ..constants import Formatting


@dataclass
class Column:

    dataframe: pd.DataFrame
    column_format: Optional[List[float]] = None

    @property
    def table_column_format(self) -> str:
        if self.column_format:
            return (
                f"{Formatting.TAB}{{% Column format\n"
                + "\n".join(
                    [
                        f"{Formatting.TAB * 2 }>{{\\raggedleft\\arraybackslash\\hsize={w}\\hsize}}X"
                        for w in self.column_format
                    ]
                )
                + f"\n{Formatting.TAB}}}"
            )

        return "".join(
            [
                f"{Formatting.TAB}{{% Column format\n",
                f"{Formatting.TAB * 2}>{{\\raggedleft\\arraybackslash\\hsize=\\hsize}}X\n"
                * self.dataframe.shape[1],
                f"{Formatting.TAB}}}",
            ]
        )
