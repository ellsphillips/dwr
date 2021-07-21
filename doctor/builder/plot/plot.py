import pandas as pd

from ...utils.tex import TeXDefaults as tex
from ...utils.cli import *

class PlotBuilder():
  """
  """

  tab_space = " "*4
  double_backslash = "\\\\"

  def __init__(
    self,
    data: dict = None,
    options: dict = None
  ):
    self.data = data
    self.options = options

    if data is None:
      log.warning("I'm not much good without data, you know...")

  def pluck(opts: dict, *args):
    return [opts[arg] for arg in args]

  def id_data(self) -> list:
    return [(name, series) for name, series in self.data.items()]

  def build_dataframe(self) -> pd.DataFrame:
    time_points = max([len(ts[1]) for ts in self.id_data()])
    log.comment(f"Built dataframe of dimension [{len(self.data), time_points}]")

    output = pd.DataFrame(
      dict(
        [(k, pd.Series(v)) for k,v in self.data.items()]
      )
    )
    output["time"] = range(time_points)

    return output[["time"] + [c for c in output.columns if c != "time" ] ]

  def add_plot(self) -> str:
    args = ["ons-blue","thick","mark=none"]
    elements = [
      r"\addplot[",
      ",\n".join([f"{self.tab_space}{arg}" for arg in args]),
		  "] table[x=time, y=data1] {src/graphs/timeseries.dat};"
    ]

    return "\n".join(e for e in elements) 
    
  #
  
  def export_data(self, out_path: str) -> None:
    destination = f"{tex.options['document']['path']}src/{out_path}.csv"
    dataframe = self.build_dataframe()
    dataframe.to_csv(destination, index=False, encoding='utf-8')
    log.output(destination)
