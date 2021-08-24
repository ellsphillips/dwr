import plotly.express as px
import pandas as pd
import numpy as np
import geojson
import os


def load_geojson(file_path: str):
  with open(file_path) as f:
      return geojson.load(f)

def generate_ids(
    geog: geojson.feature.FeatureCollection,
    area_code: str = "LAD21CD",
    area_name: str = "LAD21NM"
) -> pd.DataFrame:
  id_map = {}
  for _dict in geog['features']:
      id_map[_dict["properties"][area_name]] = _dict["properties"][area_code]

  return pd.DataFrame(
    id_map.items(),
    columns=['area', 'code']
  )

geography = load_geojson("GeoJSON/nuts3_uk_buc-la.geojson")

test_data = generate_ids(geog=geography)

test_data['values'] = [np.random.randint(1, 100) for _ in range(len(test_data))]
