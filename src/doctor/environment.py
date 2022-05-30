from typing import Protocol


class Environment(Protocol):
    @property
    def begin(self) -> str:
        ...

    @property
    def options(self) -> str:
        ...

    @property
    def body(self) -> str:
        ...

    @property
    def end(self) -> str:
        ...
