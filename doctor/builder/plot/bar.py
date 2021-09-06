from typing import Tuple, Union, Optional
import pandas as pd

from ...utils.tex import TeXDefaults as tex
from ...utils.cli import *

class Bar():
  """
  """
  def __init__(
    self,
    data: dict = None,
    options: dict = None
  ) -> None:
    self.data = data
    self.options = options
    self.plot_declarations: list = []

    if data is None:
      log.warning("I'm not much good without data, you know...")

  @staticmethod
  def _template() -> None:
    r"""
    \begin{doctor-bar}[%
      plot type={ybar},
      data source={src/plots/bar.dat},
      somebool=false,
      caption={Hello, world!},
      label={bar-test},
      xmin=0,
      xmax=12,
      ymin=0,
      ymax=35,
    ]%
      \addplot+[%
        nodes near coords,
        point meta=explicit symbolic,
        mark=none,
        ons-blue,
        very thick
      ] table [x=index, y=values, meta=values]%
      {\doctordatasource};
    \end{doctor-bar}
    """
    pass
