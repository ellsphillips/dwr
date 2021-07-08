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
      print(f"{colour.CRED}{colour.CBOLD}I'm not much good without data, you know...{colour.CEND}")

  def id_data(self) -> list:
    return [(name, series) for name, series in self.data.items()]

  def build_dataframe():
    pass
    
  # @property
  # def export_data(
  #   data: pd.Dataframe,
  #   out_path: str
  # ) -> None:
  #   destination = f"{tex.get_tex_source}\\{out_path}.tex"
  #   data.to_csv(file_name, sep='\t', encoding='utf-8')
