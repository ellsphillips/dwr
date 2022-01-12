from typing import Union

from doctor.utils.cli import *

from .bar import Bar
from .line import Line


def plot_builder(
    type: str,
    data: dict = None,
    options: dict = None
) -> Union[Line, Bar]:
    lut = {
        Line: ["line", "timeseries"],
        Bar: ["bar", "stacked-bar", "grouped-bar", "histogram"]
    }

    for constructor, terms in lut.items():
        if type in terms:
            return constructor(data, options)

    log.warning(
        "Available plotting types:\n"
        + log.prettify(lut)
    )

    raise ValueError("Provide a valid plot type from above.")
