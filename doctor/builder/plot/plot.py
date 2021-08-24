from doctor.builder.plot.line import Line
from typing import Union
from . import (
  Line,
  Bar
)


class Plot:
  """
  """
  def __init__(
    self,
    type: str,
    data: dict = None,
    options: dict = None
  ):
    self.type = type
    self.data = data
    self.options = options

  def builder(self) -> Union[
    Line,
    Bar
  ]:
    lut = {
      Line: ["line", "timeseries"],
      Bar: ["bar", "stacked-bar", "grouped-bar", "histogram"]
    }

    for builder, terms in lut.items():
      if self.type in terms:
        return builder()

    raise ValueError("Provide a valid plot type from below:")