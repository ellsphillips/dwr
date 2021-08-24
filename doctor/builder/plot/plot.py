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
    data: dict = None,
    options: dict = None
  ):
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

    for _type, terms in lut.items():
      print(
        f"_type: {_type}",
        f"terms: {terms}",
      )
      if self.options["type"] in terms:
        return _type()

    raise ValueError("Provide a valid plot type from below:")