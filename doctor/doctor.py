import sys
import pandas as pd
from typing import (
  Union
)


if sys.version_info < (3, 6):
  raise RuntimeError("This module requires Python 3.6 or higher")


def build(
  data_object: Union[pd.DataFrame, dict]
):
  """
  Select the appropraite TeX builder for Python data.
  """
  pass
