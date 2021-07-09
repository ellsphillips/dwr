import pandas as pd

from ...utils.tex import TeXDefaults as tex
from ...utils.cli import *

class PlotBuilder():
  """
  """
  def __init__(
    self,
    data: dict = None,
    options: dict = None
  ):
    self.data = data
    self.options = options

    if data is None:
      print(f"{style.warning}I'm not much good without data, you know...{style.end}")

  def id_data(self) -> list:
    return [(name, series) for name, series in self.data.items()]

  def build_dataframe(self) -> pd.DataFrame:
    time_points = max([len(ts[1]) for ts in self.id_data()])
    print(f"Built dataframe of dimension {style.announce}{len(self.data), time_points}{style.end}\n")

    return pd.DataFrame(
      dict([(k, pd.Series(v)) for k,v in self.data.items()])
    )
  
  def export_data(self, out_path: str) -> None:
    destination = f"{tex.options['document']['path']}src/{out_path}.csv"
    dataframe = self.build_dataframe()
    dataframe.to_csv(destination, index=False, encoding='utf-8')
    print(f"Data file generated at {style.announce}{destination}{style.end}\n")
