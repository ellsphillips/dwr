from dataclasses import dataclass
from typing import List

from doctor.constants import Formatting


@dataclass
class TableHeader:

    column_names: List[str]

    def create(self) -> str:
        bold_headers = [f"\\bfseries{{{col}}}" for col in self.column_names]
        return " & ".join([head for head in bold_headers]) + f" {Formatting.NEWLINE}"

    @property
    def table_column_headers(self) -> str:
        return "".join(
            [
                "{% Column headers\n",
                " &\n".join(
                    [
                        f"{Formatting.TAB * 2}\\bfseries {col}"
                        for col in self.column_names
                    ]
                )
                + f" {Formatting.NEWLINE}\n",
                f"{Formatting.TAB}" + "}",
            ]
        )
