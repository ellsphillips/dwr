from typing import Any, Iterable, List

from pandas import DataFrame


def table(data: List[Iterable[Any]]) -> DataFrame:
    columns = [f"C_{i + 1}" for i in range(len(data))]
    body = {k: v for k, v in zip(columns, data)}
    return DataFrame(body, columns=columns)
