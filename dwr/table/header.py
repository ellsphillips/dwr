from dataclasses import dataclass
from typing import List

from dwr.constants import Formatting


@dataclass
class TableHeader:

    column_names: List[str]

    def create(self) -> str:
        bold_headers = [f"\\textbf{{{col}}}" for col in self.column_names]
        return (
            Formatting.TAB
            + " & ".join([head for head in bold_headers])
            + f" {Formatting.NEWLINE}"
        )
