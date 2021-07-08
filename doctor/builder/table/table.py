import os
import pandas as pd
import numpy as np
from typing import (
  List,
  Optional,
  Union
)

from ...utils.tex import TeXDefaults as tex

class TabularBuilder:
  """
  Comprehensive table builder that outputs LaTeX markup
  from Python data input.

  Outputs inherently colour alternating rows, break over
  pages with custom message and span PDF page widths with
  user-defined column behaviour.
  """

  tab_space = " "*4
  double_backslash = "\\\\"

  def __init__(
    self,
    dataframe: pd.DataFrame = None,
    column_format: Optional[List[float]] = None,
    caption: Optional[str] = r"\textcolor{red}{Tabular caption not provided.}",
    short_caption: Optional[str] = r"\textcolor{red}{Tabular caption not provided.}",
    label: Optional[str] = None,
  ):
    self.dataframe = dataframe
    self.column_format = column_format
    self.caption = caption
    self.short_caption = short_caption
    self.label = label

  @property
  def caption_macro(self) -> str:
    r"""
    Caption macro, extracted from self.caption.
    With short caption:
        \caption[short_caption]{caption_string}.
    Without short caption:
        \caption{caption_string}.
    """
    if self.caption:
      return "".join(
        [
          r"\caption",
          f"[{self.short_caption}]" if self.short_caption else "",
          f"{{{self.caption}}}",
        ]
      )
    return ""

  @property
  def label_macro(self) -> str:
    r"""
    Label macro, extracted from self.label, like \label{ref}.
    """
    return f"\\label{{{self.label}}}" if self.label else ""

  def caption_and_label(self) -> str:
    if self.caption or self.label:
      elements = [f"{self.caption_macro}", f"{self.label_macro}"]
      caption_and_label = "\n".join([item for item in elements if item])
      caption_and_label += " \\\\"
      return caption_and_label
    else:
      return ""

  @property
  def table_caption_and_label(self) -> str:
    r"""
    Caption macro, extracted from self.caption.
      {% Caption
        {short_caption_string}, {caption_string}
      }{% Label
        label_string
      }
    """
    if self.caption:
      return "\n".join(
        [
          r"{% Caption",
          f"{self.tab_space * 2}{{{self.short_caption}}}," if self.short_caption else "{{}},",
          f"{self.tab_space * 2}{{{self.caption}}}",
          f"{self.tab_space}" + r"}{% Label",
          f"{self.tab_space * 2}{self.label}" if self.label else "%",
          f"{self.tab_space}" + "}"
        ]
      )
    return ""

  @property
  def table_column_format(self) -> str:
    r"""
    Column formatting macro.
      {% Column format
        >{}X
        ...
        >{}X
      }
    """
    if self.column_format:
      return (
        f"{self.tab_space}{{% Column format\n"
        + "\n".join(
          [
            f"{self.tab_space * 2 }>{{\\raggedleft\\arraybackslash\\hsize={w}\\hsize}}X"
            for w in self.column_format
          ]
        )
        + f"\n{self.tab_space}}}"
      )

    return "".join(
      [
        f"{self.tab_space}{{% Column format\n",
        f"{self.tab_space * 2}>{{\\raggedleft\\arraybackslash\\hsize=\\hsize}}X\n" * self.dataframe.shape[1],
        f"{self.tab_space}}}"
      ]
    )

  @property
  def table_column_headers(self) -> str:
    r"""
    Column formatting macro.
      {% Column headers
        col1 &
        ...
        coln &
        colm \\
      }
    """
    return "".join(
      [
        "{% Column headers\n",
        " &\n".join(
          [
            f"{self.tab_space * 2}\\bfseries {col}"
            for col in list(self.dataframe.columns.values)
          ]
        ) + f" {self.double_backslash}\n",
        f"{self.tab_space}" + "}"
      ]
    )

  @property
  def env_begin(self) -> str:
    r"""
    Initialise the table environment with \begin{}
    declaration, column headers and defined captions.
    """
    elements = [
      f"\\begin{{plutotable}}{{{int(self.dataframe.shape[1])}}}\n",
      f"{self.table_column_format}",
      f"{self.table_column_headers}"
      f"{self.table_caption_and_label}"
    ]
    return "".join([item for item in elements if item])

  @property
  def env_end(self) -> str:
    r"""
    Close the table environment with \end{}.
    """
    return "\end{plutotable}"
  
  @property
  def header(self) -> str:
    """
    Method for column headers' bolding markup.
    """
    bold_headers = [f"\\bfseries{{{col}}}" for col in list(self.dataframe.columns.values)]
    return " & ".join([head for head in bold_headers]) + " \\\\"

  @property
  def find_minmax_cell_length(self):
    measurer = np.vectorize(len)
    vectoriser = measurer(self.dataframe.values.astype(str))
    _min, _max = vectoriser.min(), vectoriser.max()
    return _min, _max

  def pad_spaces(self, input_number, col_index):
    num = str(input_number)
    lengths = [
      self.dataframe[col].astype(str).str.len().max()
      for col in self.dataframe.columns
    ]

    #

    if len(num) < lengths[col_index]:
      return " "*(lengths[col_index] - len(num)) + num
    return input_number

  @property
  def env_body(self) -> List[str]:
    r"""
    Return a str-type matrix of each row and column of the
    input dataframe. Rows end with "\\" to begin a new table
    row entry, and each cell is space-padded to the length
    of the longest cell's contents, separated with an "&".
    """
    export = []
    for i, row in self.dataframe.iterrows():
      export.append(
        self.tab_space
        + " & ".join([
          self.pad_spaces(str(cell), col_index)
          for col_index, cell in enumerate(row.values)
        ])
        + f" {self.double_backslash}"
      )
    return "\n".join([item for item in export if item])

  def get_result(self) -> str:
    """
    Compile the complete string representation of a LaTeX table.
    """
    elements = [
      self.env_begin,
      self.env_body,
      self.env_end,
    ]
    result = "\n".join([item for item in elements if item])
    trailing_newline = "\n"
    result += trailing_newline
    return result
