from dataclasses import dataclass, field
from typing import List


@dataclass
class Canvas:

    charts: List[str] = field(default_factory=list)
