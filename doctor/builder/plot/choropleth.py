import os

import geojson
import numpy as np
import pandas as pd
import plotly.express as px
from doctor.utils.cli import log


class Choropleth:
    """
    """
    def __init__(self):
        pass
    
    def load_geojson(
        self,
        file_path: str
    ):
        with open(file_path) as f:
            return geojson.load(f)
    
    def select_matching(
        self,
        geog: geojson.feature.FeatureCollection,
        lookup: str
    ) -> str:
        for value in geog['features'][0]['properties']:
            if lookup.lower() in value.lower():
                return value
    
    def generate_ids(
        self,
        geog:geojson.feature.FeatureCollection,
        area_code: str = "",
        area_name: str = ""
    ) -> pd.DataFrame:
        code = area_code if area_code else self.select_matching(geog,'CD')
        name = area_name if area_name else self.select_matching(geog,'NM')
        
        id_map={}
        for _dict in geog['features']:
        id_map[_dict["properties"][name]] = _dict["properties"][code]
        
        return pd.DataFrame(
            id_map.items(),
            columns=['area','code']
        )
        
    def map_plot(
        self,
        data=None,
        geog=None
    ) -> None:
        fig = px.choropleth(
            data,
            locations='code',
            geojson=geog,
            featureidkey = f"properties.{self.select_matching(geog,'CD')}",
            scope='europe',
            color='values',
            range_color=(0, 100),
            color_continuous_scale="YlGnBu",
            color_continuous_midpoint=0,
            labels={'values': ''},
            center={"lat": 55, "lon": 0}
        )
    
        fig.update_layout(
            margin={
                "r": 0,
                "t": 0,
                "l": 0,
                "b": 0,
                "autoexpand": False
            },
            width=800,
            height=600,
            legend_title_side='top'
        )
    
        fig.update_geos(
            fitbounds='locations',
            visible=False
        )
    
        fig.update_traces(
            marker_line_width=0.35
        )
    
        fig.update_coloraxes(
            # showscale=False,
            colorbar_len=.8,
            colorbar_thickness=20,
            colorbar_x=0,
            colorbar_xpad=0,
            colorbar_ypad=0
        )
    
        fig.write_image("projectile.pdf")
        fig.write_image("map.pdf")
        os.remove("projectile.pdf")


if __name__ == "__main__":
    choro = Choropleth()

    log.notice("Testing the choropleth script")
    geography = choro.load_geojson("data/geojson/nuts3_uk_buc-la.geojson")
    test_data = choro.generate_ids(geog=geography)
    test_data['values'] = [np.random.randint(1, 100) for _ in range(len(test_data))]
