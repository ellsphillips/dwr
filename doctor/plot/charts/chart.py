from typing import Iterable, Protocol


class Chart(Protocol):
    def draw(self) -> str:
        ...

    def handle_data(self, data: Iterable[float]) -> str:
        ...
