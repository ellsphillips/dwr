import plotly.express as px
import pandas as pd
import numpy as np
import geojson
import os


def load_geojson(file_path: str):
  with open(file_path) as f:
      return geojson.load(f)
